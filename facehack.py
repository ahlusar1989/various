#!/usr/bin/env python

'''
FaceHack 0.2
##for redesigned homepage##
Created by Jared Forsyth
offered w/o any warranty of any sort, etc.
email questions/comments to jabapyth@gmail.com

EXAMPLE:

import facehack
fh = facehack.FaceHack("me@example.com","secret")
print "Current status: %s"%fh.status()
fh.status("Hakkin up facebook")
fh.wall_post("Jane Doe","Heya!")
fh.message(["John Doe","Joe Schmo"],"So..","Whats chillin, folks?")

print "You have %d friends"%len(fh.friends)
'''
debug = True

import urllib
import cookielib, urllib2
import re
import time
import random
import math
from HTMLParser import HTMLParser

headers = {'User-agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}

debug = True

### stuff ###

def get_page(url,data=None,xheaders=None):
    req = urllib2.Request(url, urllib.urlencode(data), xheaders or headers)
    handle = urllib2.urlopen(req)
    return handle

def get_forms(txt):
    forms = re.findall("(<form[^>]*>)(.+?)</form>",txt,re.S|re.I)
    for head,data in forms:
        yield parse_tags(head)[0][1],get_form_data(data)

def get_form_data(txt):
    res = {}
    texts = re.findall("(<textarea[^>]*>)(.*?)</textarea>",txt,re.S|re.I)
    for head,text in texts:
        attrs = parse_tags(head)[0][1]
        attrs["value"] = text
        if attrs.has_key("name"):
            res[attrs['name']] = attrs
    
    inputs = re.findall("<input[^>]*>",txt,re.S|re.I)
    for text in inputs:
        attrs = parse_tags(text)[0][1]
        if attrs.has_key("name"):
            res[attrs['name']] = attrs
    
    buttons = re.findall("(<button[^>]*>)(.*?)</button>",txt,re.S|re.I)
    for head,text in buttons:
        attrs = parse_tags(head)[0][1]
        if text and not attrs.has_key("value"):
            attrs["value"] = text
        if attrs.has_key("name"):
            res[attrs['name']] = attrs
    return res

def parse_tags(txt):
    tags = []
    class Ps(HTMLParser):
        def handle_starttag(self,tag,attrs):
            tags.append([tag,dict(attrs)])
    Ps().feed(txt)
    return tags

### accessible functions ###

class Friend_Error(Exception):
    pass


'''
FaceHack:
    __init__(self,user=None,passw=None)
        initialize, optionally login
    
    login(self,userr,passw)
        login
    
    status(self,new=None)
        if new is given, set status
        otherwise, get status
    
    wall_post(self,name_or_id,text)
    
    send_message(self,names,subject,message)
        if names is a string, just send to one person
        if its a list, send to all in the list
    

working:

login
get_friends
status

'''


class FaceHack:
    debug = True
    def __init__(self,user=None,passw=None):
        self.setup()
        self.name = ''
        if user and passw:
            self.login(user,passw)
    
    def get_page(self,url,data={}):
        req = urllib2.Request(url, urllib.urlencode(data), {'User-agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'})
        try:
            handle = urllib2.urlopen(req)
        except:
            try:handle = urllib2.urlopen(req)
            except:handle = urllib2.urlopen(req)
        text = handle.read()
        redirect_pattern = re.escape('window.location.replace("') + '([^"]+)' + re.escape('");')
        result = re.findall(redirect_pattern,text)
        if result:
            if self.debug:print "Redirecting to ",result[0].replace('\\\\/','/').replace('\\/','/')
            return self.get_page(result[0].replace('\\\\/','/').replace('\\/','/'))
        if self.debug:
            open('facehack-'+url.split('/')[-1].split('?')[0],'w').write(text)
        return text
    
    def setup(self):
        cj = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        urllib2.install_opener(opener)
    
    def login(self,email,passw):
        dct = {}
        dct["persistent"] = "1"
        dct["login"] = "Login"
        dct["charset_test"] = "%u20AC,%uFFFD,%u20AC,%uFFFD,%u6C34,%u0414,%u0404"
        dct["email"] = email
        dct["pass"] = passw
        
        self.get_page("http://facebook.com/login.php")
        self.get_page("https://login.facebook.com/login.php", dct)
        text = self.get_page("http://www.facebook.com/home.php?")
        stories = re.findall('<h3 class="UIIntentionalStory_Message"><span class="UIIntentionalStory_Names"><a href="([^"]+)" onclick="[^"]+">([^<]+)</a></span>([^<]+)</h3><div class="UIIntentionalStory_Info"><div class="UIIntentionalStory_InfoText"><span class="UIIntentionalStory_Time">([^<]+)</span>', text)
        
        pattern = re.escape('window.presence = new Presence("') + '(\d+)' + re.escape('", "') + '([^"]+)' + '"'
        
        result = re.findall(pattern,text)
        if not result:
            raise Exception('Invalid Username/Password')
        
        self.id,self.name = result[0]
        self.friend_ids = self.get_friends()
        self.friends = self.friend_ids.keys()
        self.front_stories = stories
        #### alternate way to get name, id
        '''
        window.presence = new Presence("600656022", "Jared Forsyth", "Jared", 1237374870000, 0, 
        '''
        
    def wall_post(self,name,wall_text):
        id = self.get_id(name)
        url = "http://www.facebook.com/wall.php?id=%s"%id
        text = self.get_page(url)
        form = list(get_forms(text))[1]
        
        url = "http://www.facebook.com/wallpost.php"
        dct={}
        for key in form[1]:
            dct[key] = form[1][key]["value"]
        dct["wall_text"] = wall_text
        res = self.get_page(url, dct)
    
    def message(self,names,subject,message):
        if type(names)==str:names = [names]
        ids = [self.get_id(name) for name in names]
        url = "http://www.facebook.com/inbox/?compose="
        text = self.get_page(url)
        form = list(get_forms(text))[1]
        
        url = "http://www.facebook.com/inbox/"
        dct = {}
        for key in form[1]:
            dct[key] = form[1][key]["value"]
        dct["subject"] = subject
        dct["message"] = message
        dct["rand_id"] = str(int(random.random()*100000000))
        data = dct.items()
        for id in ids:
            data.append(("ids[]",id))
            
        res = self.get_page(url, data)

    def status(self,new=None):
        url = "http://www.facebook.com/profile.php?id=%s"%self.id
        txt = self.get_page(url)
        #return txt
        
        '''id="post_form_id" name="post_form_id" value="461ab658eaa140c9b1314b5ecd9dcd3b"'''
        
        ## rgx = re.escape('new ChatDisplay({"%s":{"name":"'%self.id) + '([^"]+)' + re.escape('","firstName":"') + '([^"]+)' + re.escape('","thumbSrc":"') + '([^"]+)' + re.escape('","status":"') + '([^"]+)' + re.escape('","statusTime":') + '\d+' + re.escape(',"statusTimeRel":"') + '([^"]+)' + '"'
        ## bomb
        ## name,firstname,thumb,status,time = re.findall(rgx,txt)[0]
        status_pattern = re.escape('<span id="profile_status"><span id="status_text">') + '([^<]+)' + re.escape('</span><small><span id="status_time"><span id="status_time_inner">') + '([^<]+)' + re.escape('</span>')
        ## rgx = '''<span id="status_text">([^<]+)</span><small><span id="status_time"><span id="status_time_inner">([^<]+)</span>'''
        
        ## status = re.findall('<span class="status_text">([^<]+)</span>',txt)[0]
        status,time = re.findall(status_pattern,txt)[0]
        if new:
            pid = re.findall('id="post_form_id" name="post_form_id" value="(.+?)"',txt)[0]
            if not pid:raise Exception("No Post Form ID")
            if debug:print "FormID: ",pid,'<br>'
            
            url = 'http://www.facebook.com/updatestatus.php'
            dct = {"status":new,"post_form_id":pid,'home_tab_id':1,
                'post_form_id_source':'AsyncRequest',
                'profile_id':self.id,
                'test_name':'INLINE_STATUS_EDITOR'}
            
            res = self.get_page(url, dct)
            ntxt = res.read()
            status = re.findall('"status":"([^"]+)"',ntxt)[0]
        return status,time#,thumb
            
    def get_id(self,id):
        if type(id)==int or id.isdigit():return str(id)
        if id in self.friends:
            return self.friend_ids[id]
        raise Friend_Error("Friend %s not found"%id)
    
    def get_profile_pics(self,id):
        data = self.get_page('http://www.facebook.com/album.php?profile&id=%s'%self.get_id(id))
        pics = re.findall('"([^"]+)" alt="" class="UIPhotoGrid_Image"',data)
        return pics
        ## data = self.get_page("http://www.facebook.com/profile.php?id=%s"%self.get_id(id)).read()
        ## return re.findall('<img src="([^"]+)" alt="" id="profile_pic" />',data)[0]
    
    def get_friends(self,id=None):
        if id is None: id = self.id
        id = self.get_id(id)
        url = "http://www.facebook.com/friends/ajax/friends.php?id=%s"%id
        text = self.get_page(url)
        front,main = text.split(");",1)
        main = main.replace("null","None").replace("false","False").replace("true","True")
        stuff=eval(main)
        fps = stuff["payload"]["friend_pages"]
        ## friends = [self.name]
        friend_ids = {self.name:self.id}
        rgx = 'id=(\d*)" class="fname">(.+?)<'
        for fpage in fps:
            for id,f in re.findall(rgx,fpage):
                ## friends.append(f)
                friend_ids[f] = id
        return friend_ids
        #if id==self.id:
        #    self.friends = friends
        #    self.friend_ids = friend_ids
        
        ## http://www.facebook.com/friends/ajax/friends.php?id=600656022&flid=10272221022&view=everyone&q=&nt=0&nk=0&st=0&ps=50&s=0
        ## http://www.facebook.com/friends/ajax/friends.php?id=600656022&flid=0&view=network&q=&nt=0&nk=33572501&st=0&ps=50&s=0

    def get_wall(self,id=None,start=0,num=10):
        if id is None: id = self.id
        id = self.get_id(id)
        url = 'http://www.facebook.com/ajax/stream/profile.php?profile_id=%s'%id
        rz = self.get_page(url)
        nextmax = re.findall('"payload":{"max_time":(\d+)',rz)[0]
        
        rz = rz.replace('\\n','').replace('\\','')
        ret = []
        for them in re.findall('<div class="UIIntentionalStory_Content"><a[^>]+><span class="UIRoundedImage UIRoundedImage_WHITE UIRoundedImage_LARGE"><img src="([^"]+)" alt="([^"]+)" class="UIRoundedImage_Image" /><span class="UIRoundedImage_Corners"><img[^>]+></span></span></a><div class="UIIntentionalStory_Body"><div class="UIIntentionalStory_Header"><h3 class="UIIntentionalStory_Message">\s+<span class="UIIntentionalStory_Names"><a href="([^"]+)" >([^<]+)</a>\s+</span>(.*?)</h3></div><div class="UIIntentionalStory_Info"><div class="UIIntentionalStory_InfoText"><span class="UIIntentionalStory_Time"><a[^>]+>([^<]+)</a></span> &#183; .+?<div class="wall_posts"[^>]+>(?:<div id="[^"]+"  class="wallpost"><div class="wallimage"><a href="[^"]+" title="[^"]+"><span class="UIRoundedImage UIRoundedImage_GIRLIE UIRoundedImage_SMALL"><img src="([^"]+)" alt="([^"]+)" class="UIRoundedImage_Image" /><span class="UIRoundedImage_Corners"><img[^>]+></span></span></a></div><div class="wallcontent" id="[^"]+" ><div class="wallfrom"><span class="wallmeta"></span><a href="([^"]+)">Dani Pocock</a><span class="wallmeta">([^<]+)</span><span class="wallcredits"></span></div><div class="walltext"><div id="[^"]+" class="wall_actual_text">(.+?)</div></div></div></div>)*</div>.+?</div></div></div></div></form></div></div></div></div></div>',rz):
            pic,name,prof,name,txt,time = them[:6]
            comments = them[6:]
            ret.append(them[:6])
        return rz
        
    def get_networks(self):
        url = "http://www.facebook.com/friends/ajax/filters.php?id=%s"%self.id
        text = self.get_page(url)
        front,main = text.split(");",1)
        main = main.replace("null","None").replace("false","False").replace("true","True")
        stuff=eval(main)
        return stuff["payload"]
        
        
        '''text = self.get_page('http://www.facebook.com/friends/ajax/filters.php?id=%s'%self.id).read()
        main = text.replace("null","None").replace("false","False").replace("true","True")
        main = re.sub('/\*.+?\*/','',main)
        error = 'error'
        errorSummery = 'errorSummery%2'''
