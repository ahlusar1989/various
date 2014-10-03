<!DOCTYPE html>
<!-- saved from url=(0078)http://pythoninside.com/en/source-code/Facebook+SDK+0.4.0/facebook/facebook.py -->
<html lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"> <!--<base href="http://pythoninside.com/en/">--><base href="."> <title>facebook.py Source Code - facebook - Facebook SDK 0.4.0 | PythonInside.com</title> <meta charset="utf-8"> <meta name="viewport" content="width=device-width, initial-scale=1.0"> <script async="" src="./facebook_files/analytics.js"></script><script src="./facebook_files/jquery-2.0.3.min.js"></script><style type="text/css"></style> <link rel="stylesheet" href="http://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css"> <style> body { padding-top: 70px; }
            pre { -moz-tab-size: 4; -o-tab-size: 4; tab-size: 4; } </style> <link rel="stylesheet" href="http://pythoninside.com/res/css/style.css"> <link rel="stylesheet" type="text/css" href="./facebook_files/prettify.css"></head> <body style=""> <header class="navbar navbar-default navbar-fixed-top" role="banner"> <div class="container"> <div class="nav-header"> <button class="navbar-toggle" type="button" data-toggle="collapse" data-target=".navbar-collapse"> <span class="sr-only">Toggle navigation</span> <span class="icon-bar"></span> <span class="icon-bar"></span> <span class="icon-bar"></span> </button> <a href="" class="navbar-brand">PythonInside.com</a> </div> <nav class="collapse navbar-collapse" role="navigation"> <ul class="nav navbar-nav"> </ul> <ul class="nav navbar-nav navbar-right"> <li class="dropdown"> <a href="http://pythoninside.com/en/#" class="dropdown-toggle" data-toggle="dropdown" title="Change language"> <span class="flag flag-en"></span> English <b class="caret"></b> </a> <ul class="dropdown-menu"> <li> <a href="./facebook_files/facebook.py" title="Set language to : English"> <span class="flag flag-en"></span> English </a> </li> <li> <a href="http://pythoninside.com/fr/source-code/Facebook+SDK+0.4.0/facebook/facebook.py" title="Set language to : Français"> <span class="flag flag-fr"></span> Français </a> </li> </ul> </li> </ul> </nav> </div> </header> <article role="main" class="container"> <div class="form-group"> <input bind="global-search-distrib" name="d" type="hidden" value="Facebook SDK 0.4.0"> <div class="input-group"> <div class="input-group-btn"> <button class="btn btn-default dropdown-toggle" data-toggle="dropdown"> <span bind="search-range" data-d="">Facebook SDK 0.4.0</span> <span class="caret"></span> </button> <ul bind="search-range-selector" class="dropdown-menu"> <li><a href="http://pythoninside.com/en/#">All distributions</a></li> <li class="divider"></li> <li><a href="http://pythoninside.com/en/#" data-d="1.5.2">1.5.2</a></li> <li><a href="http://pythoninside.com/en/#" data-d="1.6.1">1.6.1</a></li> <li><a href="http://pythoninside.com/en/#" data-d="2.0.1">2.0.1</a></li> <li><a href="http://pythoninside.com/en/#" data-d="2.1.3">2.1.3</a></li> <li><a href="http://pythoninside.com/en/#" data-d="2.2.3">2.2.3</a></li> <li><a href="http://pythoninside.com/en/#" data-d="2.3.7">2.3.7</a></li> <li><a href="http://pythoninside.com/en/#" data-d="2.4.6">2.4.6</a></li> <li><a href="http://pythoninside.com/en/#" data-d="2.5.6">2.5.6</a></li> <li><a href="http://pythoninside.com/en/#" data-d="2.6.8">2.6.8</a></li> <li><a href="http://pythoninside.com/en/#" data-d="2.7.2">2.7.2</a></li> <li><a href="http://pythoninside.com/en/#" data-d="2.7.5">2.7.5</a></li> <li><a href="http://pythoninside.com/en/#" data-d="3.0.1">3.0.1</a></li> <li><a href="http://pythoninside.com/en/#" data-d="3.1.5">3.1.5</a></li> <li><a href="http://pythoninside.com/en/#" data-d="3.2.5">3.2.5</a></li> <li><a href="http://pythoninside.com/en/#" data-d="3.3.2">3.3.2</a></li> <li><a href="http://pythoninside.com/en/#" data-d="Django-1.5.4">Django-1.5.4</a></li> <li class="active"><a href="http://pythoninside.com/en/#" data-d="Facebook SDK 0.4.0">Facebook SDK 0.4.0</a></li> <li><a href="http://pythoninside.com/en/#" data-d="PyCrypto 2.6">PyCrypto 2.6</a></li> <li><a href="http://pythoninside.com/en/#" data-d="PyOpenGL-3.0.1">PyOpenGL-3.0.1</a></li> <li><a href="http://pythoninside.com/en/#" data-d="PyOpenGL-3.0.2">PyOpenGL-3.0.2</a></li> <li><a href="http://pythoninside.com/en/#" data-d="python-twitter 1.1">python-twitter 1.1</a></li> </ul> </div> <!-- .input-group-btn --> <input bind="global-search-text" name="q" type="text" class="form-control" placeholder="Search file name..." value=""> </div> <!-- .input-group --> </div> <!-- .form-group --> <ul class="breadcrumb"> <li><a href="">Home</a></li> <li><a href="http://pythoninside.com/en/distrib/Facebook+SDK+0.4.0">Facebook SDK 0.4.0</a></li> <li><a href="http://pythoninside.com/en/module/Facebook+SDK+0.4.0/facebook">facebook</a></li> <li class="active">facebook.py</li> </ul> <div class="row"> <div class="col-lg-4"> <script async="" src="http://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script> <ins class="adsbygoogle" style="display:inline-block;width:336px;height:280px" data-ad-client="ca-pub-7704156438452645" data-ad-slot="3165909391"></ins> <script> (adsbygoogle = window.adsbygoogle || []).push({}); </script> <h2>facebook files</h2> <div class="list-group"> <a class="list-group-item active" href="./facebook_files/facebook.py"> facebook.py </a> </div> <h2>Related Source Codes</h2> <div class="list-group"> <a class="list-group-item " href="http://megasnippets.com/en/source-codes/python/use_facebook_api"> Python Use of Facebook API </a> </div> <div class="alert alert-info">DEC 5TH 2013 CLUB 5STAR FORMERLY THE OLD CHARLIES CLUB SELECTA FAWTEEN BIRTHDAY CELEBRATION DOORS OPEN AT 9PM THE... <a rel="nofollow" href="http://t.co/MCRY5AaaDs">fb.me/1SfAnWRym</a> <small>2013-11-06 02:50</small></div><div class="alert alert-info">I posted a new photo to Facebook <a rel="nofollow" href="http://t.co/tZeKUxkQvE">fb.me/28DHz8jWr</a> <small>2013-11-06 02:50</small></div><div class="alert alert-info">Find more fun, photos and event news on our Facebook Page: <a rel="nofollow" href="http://t.co/hdcZq15Iz1">ow.ly/qwrtE</a> #winesister <small>2013-11-06 02:50</small></div><div class="alert alert-info">RT @DaHess1: Being thankful for a reliable coke dealer isn't exactly the theme they are going for on Facebook this month. <small>2013-11-06 02:50</small></div><div class="alert alert-info">Judy Garland. <a rel="nofollow" href="http://t.co/M6ozSa1l53">fb.me/27InHeJ1l</a> <small>2013-11-06 02:50</small></div><div class="alert alert-info">@OfficialGreggyJ fans I'm trying to get him to 500+ likes on Facebook comment Kailey sent me here or send me a screenshot! Thank you! 84♥ <small>2013-11-06 02:50</small></div><div class="alert alert-info">Assumption's cross country team has had two of their top runners injured most of the season but this fun group... <a rel="nofollow" href="http://t.co/FMNp0FD7Bf">fb.me/OcsYwwmz</a> <small>2013-11-06 02:50</small></div><div class="alert alert-info">It's bitches like you that made Facebook hashtags a real thing. #GoDie #AntiFacebookHashtags <small>2013-11-06 02:50</small></div> </div> <div class="col-lg-8"> <h1>facebook.py Source Code</h1> <script async="" src="http://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script> <ins class="adsbygoogle" style="display:inline-block;width:728px;height:90px" data-ad-client="ca-pub-7704156438452645" data-ad-slot="4642642597"></ins> <script> (adsbygoogle = window.adsbygoogle || []).push({}); </script> <pre class="prettyprint prettyprinted" style=""><code><span class="com">#!/usr/bin/env python</span><span class="pln">
</span><span class="com">#</span><span class="pln">
</span><span class="com"># Copyright 2010 Facebook</span><span class="pln">
</span><span class="com">#</span><span class="pln">
</span><span class="com"># Licensed under the Apache License, Version 2.0 (the "License"); you may</span><span class="pln">
</span><span class="com"># not use this file except in compliance with the License. You may obtain</span><span class="pln">
</span><span class="com"># a copy of the License at</span><span class="pln">
</span><span class="com">#</span><span class="pln">
</span><span class="com">#     http://www.apache.org/licenses/LICENSE-2.0</span><span class="pln">
</span><span class="com">#</span><span class="pln">
</span><span class="com"># Unless required by applicable law or agreed to in writing, software</span><span class="pln">
</span><span class="com"># distributed under the License is distributed on an "AS IS" BASIS, WITHOUT</span><span class="pln">
</span><span class="com"># WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the</span><span class="pln">
</span><span class="com"># License for the specific language governing permissions and limitations</span><span class="pln">
</span><span class="com"># under the License.</span><span class="pln">

</span><span class="str">"""Python client library for the Facebook Platform.

This client library is designed to support the Graph API and the
official Facebook JavaScript SDK, which is the canonical way to
implement Facebook authentication. Read more about the Graph API at
http://developers.facebook.com/docs/api. You can download the Facebook
JavaScript SDK at http://github.com/facebook/connect-js/.

If your application is using Google AppEngine's webapp framework, your
usage of this module might look like this:

user = facebook.get_user_from_cookie(self.request.cookies, key, secret)
if user:
    graph = facebook.GraphAPI(user["</span><span class="pln">access_token</span><span class="str">"])
    profile = graph.get_object("</span><span class="pln">me</span><span class="str">")
    friends = graph.get_connections("</span><span class="pln">me</span><span class="str">", "</span><span class="pln">friends</span><span class="str">")

"""</span><span class="pln">

</span><span class="kwd">import</span><span class="pln"> cgi
</span><span class="kwd">import</span><span class="pln"> time
</span><span class="kwd">import</span><span class="pln"> urllib
</span><span class="kwd">import</span><span class="pln"> urllib2
</span><span class="kwd">import</span><span class="pln"> httplib
</span><span class="kwd">import</span><span class="pln"> hashlib
</span><span class="kwd">import</span><span class="pln"> hmac
</span><span class="kwd">import</span><span class="pln"> base64
</span><span class="kwd">import</span><span class="pln"> logging
</span><span class="kwd">import</span><span class="pln"> socket

</span><span class="com"># Find a JSON parser</span><span class="pln">
</span><span class="kwd">try</span><span class="pun">:</span><span class="pln">
    </span><span class="kwd">import</span><span class="pln"> simplejson </span><span class="kwd">as</span><span class="pln"> json
</span><span class="kwd">except</span><span class="pln"> </span><span class="typ">ImportError</span><span class="pun">:</span><span class="pln">
    </span><span class="kwd">try</span><span class="pun">:</span><span class="pln">
        </span><span class="kwd">from</span><span class="pln"> django</span><span class="pun">.</span><span class="pln">utils </span><span class="kwd">import</span><span class="pln"> simplejson </span><span class="kwd">as</span><span class="pln"> json
    </span><span class="kwd">except</span><span class="pln"> </span><span class="typ">ImportError</span><span class="pun">:</span><span class="pln">
        </span><span class="kwd">import</span><span class="pln"> json
_parse_json </span><span class="pun">=</span><span class="pln"> json</span><span class="pun">.</span><span class="pln">loads

</span><span class="com"># Find a query string parser</span><span class="pln">
</span><span class="kwd">try</span><span class="pun">:</span><span class="pln">
    </span><span class="kwd">from</span><span class="pln"> urlparse </span><span class="kwd">import</span><span class="pln"> parse_qs
</span><span class="kwd">except</span><span class="pln"> </span><span class="typ">ImportError</span><span class="pun">:</span><span class="pln">
    </span><span class="kwd">from</span><span class="pln"> cgi </span><span class="kwd">import</span><span class="pln"> parse_qs


</span><span class="kwd">class</span><span class="pln"> </span><span class="typ">GraphAPI</span><span class="pun">(</span><span class="kwd">object</span><span class="pun">):</span><span class="pln">
    </span><span class="str">"""A client for the Facebook Graph API.

    See http://developers.facebook.com/docs/api for complete
    documentation for the API.

    The Graph API is made up of the objects in Facebook (e.g., people,
    pages, events, photos) and the connections between them (e.g.,
    friends, photo tags, and event RSVPs). This client provides access
    to those primitive types in a generic way. For example, given an
    OAuth access token, this will fetch the profile of the active user
    and the list of the user's friends:

       graph = facebook.GraphAPI(access_token)
       user = graph.get_object("</span><span class="pln">me</span><span class="str">")
       friends = graph.get_connections(user["</span><span class="pln">id</span><span class="str">"], "</span><span class="pln">friends</span><span class="str">")

    You can see a list of all of the objects and connections supported
    by the API at http://developers.facebook.com/docs/reference/api/.

    You can obtain an access token via OAuth or by using the Facebook
    JavaScript SDK. See
    http://developers.facebook.com/docs/authentication/ for details.

    If you are using the JavaScript SDK, you can use the
    get_user_from_cookie() method below to get the OAuth access token
    for the active user from the cookie saved by the SDK.

    """</span><span class="pln">
    </span><span class="kwd">def</span><span class="pln"> __init__</span><span class="pun">(</span><span class="kwd">self</span><span class="pun">,</span><span class="pln"> access_token</span><span class="pun">=</span><span class="kwd">None</span><span class="pun">,</span><span class="pln"> timeout</span><span class="pun">=</span><span class="kwd">None</span><span class="pun">):</span><span class="pln">
        </span><span class="kwd">self</span><span class="pun">.</span><span class="pln">access_token </span><span class="pun">=</span><span class="pln"> access_token
        </span><span class="kwd">self</span><span class="pun">.</span><span class="pln">timeout </span><span class="pun">=</span><span class="pln"> timeout

    </span><span class="kwd">def</span><span class="pln"> get_object</span><span class="pun">(</span><span class="kwd">self</span><span class="pun">,</span><span class="pln"> id</span><span class="pun">,</span><span class="pln"> </span><span class="pun">**</span><span class="pln">args</span><span class="pun">):</span><span class="pln">
        </span><span class="str">"""Fetchs the given object from the graph."""</span><span class="pln">
        </span><span class="kwd">return</span><span class="pln"> </span><span class="kwd">self</span><span class="pun">.</span><span class="pln">request</span><span class="pun">(</span><span class="pln">id</span><span class="pun">,</span><span class="pln"> args</span><span class="pun">)</span><span class="pln">

    </span><span class="kwd">def</span><span class="pln"> get_objects</span><span class="pun">(</span><span class="kwd">self</span><span class="pun">,</span><span class="pln"> ids</span><span class="pun">,</span><span class="pln"> </span><span class="pun">**</span><span class="pln">args</span><span class="pun">):</span><span class="pln">
        </span><span class="str">"""Fetchs all of the given object from the graph.

        We return a map from ID to object. If any of the IDs are
        invalid, we raise an exception.
        """</span><span class="pln">
        args</span><span class="pun">[</span><span class="str">"ids"</span><span class="pun">]</span><span class="pln"> </span><span class="pun">=</span><span class="pln"> </span><span class="str">","</span><span class="pun">.</span><span class="pln">join</span><span class="pun">(</span><span class="pln">ids</span><span class="pun">)</span><span class="pln">
        </span><span class="kwd">return</span><span class="pln"> </span><span class="kwd">self</span><span class="pun">.</span><span class="pln">request</span><span class="pun">(</span><span class="str">""</span><span class="pun">,</span><span class="pln"> args</span><span class="pun">)</span><span class="pln">

    </span><span class="kwd">def</span><span class="pln"> get_connections</span><span class="pun">(</span><span class="kwd">self</span><span class="pun">,</span><span class="pln"> id</span><span class="pun">,</span><span class="pln"> connection_name</span><span class="pun">,</span><span class="pln"> </span><span class="pun">**</span><span class="pln">args</span><span class="pun">):</span><span class="pln">
        </span><span class="str">"""Fetchs the connections for given object."""</span><span class="pln">
        </span><span class="kwd">return</span><span class="pln"> </span><span class="kwd">self</span><span class="pun">.</span><span class="pln">request</span><span class="pun">(</span><span class="pln">id </span><span class="pun">+</span><span class="pln"> </span><span class="str">"/"</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> connection_name</span><span class="pun">,</span><span class="pln"> args</span><span class="pun">)</span><span class="pln">

    </span><span class="kwd">def</span><span class="pln"> put_object</span><span class="pun">(</span><span class="kwd">self</span><span class="pun">,</span><span class="pln"> parent_object</span><span class="pun">,</span><span class="pln"> connection_name</span><span class="pun">,</span><span class="pln"> </span><span class="pun">**</span><span class="pln">data</span><span class="pun">):</span><span class="pln">
        </span><span class="str">"""Writes the given object to the graph, connected to the given parent.

        For example,

            graph.put_object("</span><span class="pln">me</span><span class="str">", "</span><span class="pln">feed</span><span class="str">", message="</span><span class="typ">Hello</span><span class="pun">,</span><span class="pln"> world</span><span class="str">")

        writes "</span><span class="typ">Hello</span><span class="pun">,</span><span class="pln"> world</span><span class="str">" to the active user's wall. Likewise, this
        will comment on a the first post of the active user's feed:

            feed = graph.get_connections("</span><span class="pln">me</span><span class="str">", "</span><span class="pln">feed</span><span class="str">")
            post = feed["</span><span class="pln">data</span><span class="str">"][0]
            graph.put_object(post["</span><span class="pln">id</span><span class="str">"], "</span><span class="pln">comments</span><span class="str">", message="</span><span class="typ">First</span><span class="pun">!</span><span class="str">")

        See http://developers.facebook.com/docs/api#publishing for all
        of the supported writeable objects.

        Certain write operations require extended permissions. For
        example, publishing to a user's feed requires the
        "</span><span class="pln">publish_actions</span><span class="str">" permission. See
        http://developers.facebook.com/docs/publishing/ for details
        about publishing permissions.

        """</span><span class="pln">
        </span><span class="kwd">assert</span><span class="pln"> </span><span class="kwd">self</span><span class="pun">.</span><span class="pln">access_token</span><span class="pun">,</span><span class="pln"> </span><span class="str">"Write operations require an access token"</span><span class="pln">
        </span><span class="kwd">return</span><span class="pln"> </span><span class="kwd">self</span><span class="pun">.</span><span class="pln">request</span><span class="pun">(</span><span class="pln">parent_object </span><span class="pun">+</span><span class="pln"> </span><span class="str">"/"</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> connection_name</span><span class="pun">,</span><span class="pln">
                            post_args</span><span class="pun">=</span><span class="pln">data</span><span class="pun">)</span><span class="pln">

    </span><span class="kwd">def</span><span class="pln"> put_wall_post</span><span class="pun">(</span><span class="kwd">self</span><span class="pun">,</span><span class="pln"> message</span><span class="pun">,</span><span class="pln"> attachment</span><span class="pun">={},</span><span class="pln"> profile_id</span><span class="pun">=</span><span class="str">"me"</span><span class="pun">):</span><span class="pln">
        </span><span class="str">"""Writes a wall post to the given profile's wall.

        We default to writing to the authenticated user's wall if no
        profile_id is specified.

        attachment adds a structured attachment to the status message
        being posted to the Wall. It should be a dictionary of the form:

            {"</span><span class="pln">name</span><span class="str">": "</span><span class="typ">Link</span><span class="pln"> name</span><span class="str">"
             "</span><span class="pln">link</span><span class="str">": "</span><span class="pln">http</span><span class="pun">:</span><span class="com">//www.example.com/",</span><span class="pln">
             </span><span class="str">"caption"</span><span class="pun">:</span><span class="pln"> </span><span class="str">"{*actor*} posted a new review"</span><span class="pun">,</span><span class="pln">
             </span><span class="str">"description"</span><span class="pun">:</span><span class="pln"> </span><span class="str">"This is a longer description of the attachment"</span><span class="pun">,</span><span class="pln">
             </span><span class="str">"picture"</span><span class="pun">:</span><span class="pln"> </span><span class="str">"http://www.example.com/thumbnail.jpg"</span><span class="pun">}</span><span class="pln">

        </span><span class="str">"""
        return self.put_object(profile_id, "</span><span class="pln">feed</span><span class="str">", message=message,
                               **attachment)

    def put_comment(self, object_id, message):
        """</span><span class="typ">Writes</span><span class="pln"> the given comment on the given post</span><span class="pun">.</span><span class="str">"""
        return self.put_object(object_id, "</span><span class="pln">comments</span><span class="str">", message=message)

    def put_like(self, object_id):
        """</span><span class="typ">Likes</span><span class="pln"> the given post</span><span class="pun">.</span><span class="str">"""
        return self.put_object(object_id, "</span><span class="pln">likes</span><span class="str">")

    def delete_object(self, id):
        """</span><span class="typ">Deletes</span><span class="pln"> the </span><span class="kwd">object</span><span class="pln"> </span><span class="kwd">with</span><span class="pln"> the given ID </span><span class="kwd">from</span><span class="pln"> the graph</span><span class="pun">.</span><span class="str">"""
        self.request(id, post_args={"</span><span class="pln">method</span><span class="str">": "</span><span class="kwd">delete</span><span class="str">"})

    def delete_request(self, user_id, request_id):
        """</span><span class="typ">Deletes</span><span class="pln"> the </span><span class="typ">Request</span><span class="pln"> </span><span class="kwd">with</span><span class="pln"> the given ID </span><span class="kwd">for</span><span class="pln"> the given user</span><span class="pun">.</span><span class="str">"""
        conn = httplib.HTTPSConnection('graph.facebook.com')

        url = '/%s_%s?%s' % (
            request_id,
            user_id,
            urllib.urlencode({'access_token': self.access_token}),
        )
        conn.request('DELETE', url)
        response = conn.getresponse()
        data = response.read()

        response = _parse_json(data)
        # Raise an error if we got one, but don't not if Facebook just
        # gave us a Bool value
        if (response and isinstance(response, dict) and
            response.get("</span><span class="pln">error</span><span class="str">")):
            raise GraphAPIError(response)

        conn.close()

    def put_photo(self, image, message=None, album_id=None, **kwargs):
        """</span><span class="typ">Uploads</span><span class="pln"> an image </span><span class="kwd">using</span><span class="pln"> multipart</span><span class="pun">/</span><span class="pln">form</span><span class="pun">-</span><span class="pln">data</span><span class="pun">.</span><span class="pln">

        image</span><span class="pun">=</span><span class="typ">File</span><span class="pln"> like </span><span class="kwd">object</span><span class="pln"> </span><span class="kwd">for</span><span class="pln"> the image
        message</span><span class="pun">=</span><span class="typ">Caption</span><span class="pln"> </span><span class="kwd">for</span><span class="pln"> your image
        album_id</span><span class="pun">=</span><span class="kwd">None</span><span class="pln"> posts to </span><span class="pun">/</span><span class="pln">me</span><span class="pun">/</span><span class="pln">photos which uses </span><span class="kwd">or</span><span class="pln"> creates </span><span class="kwd">and</span><span class="pln"> uses
        an album </span><span class="kwd">for</span><span class="pln"> your application</span><span class="pun">.</span><span class="pln">

        </span><span class="str">"""
        object_id = album_id or "</span><span class="pln">me</span><span class="str">"
        #it would have been nice to reuse self.request;
        #but multipart is messy in urllib
        post_args = {
                  'access_token': self.access_token,
                  'source': image,
                  'message': message
        }
        post_args.update(kwargs)
        content_type, body = self._encode_multipart_form(post_args)
        req = urllib2.Request(("</span><span class="pln">https</span><span class="pun">:</span><span class="com">//graph.facebook.com/%s/photos" %</span><span class="pln">
                               object_id</span><span class="pun">),</span><span class="pln">
                              data</span><span class="pun">=</span><span class="pln">body</span><span class="pun">)</span><span class="pln">
        req</span><span class="pun">.</span><span class="pln">add_header</span><span class="pun">(</span><span class="str">'Content-Type'</span><span class="pun">,</span><span class="pln"> content_type</span><span class="pun">)</span><span class="pln">
        </span><span class="kwd">try</span><span class="pun">:</span><span class="pln">
            data </span><span class="pun">=</span><span class="pln"> urllib2</span><span class="pun">.</span><span class="pln">urlopen</span><span class="pun">(</span><span class="pln">req</span><span class="pun">).</span><span class="pln">read</span><span class="pun">()</span><span class="pln">
        </span><span class="com">#For Python 3 use this:</span><span class="pln">
        </span><span class="com">#except urllib2.HTTPError as e:</span><span class="pln">
        </span><span class="kwd">except</span><span class="pln"> urllib2</span><span class="pun">.</span><span class="typ">HTTPError</span><span class="pun">,</span><span class="pln"> e</span><span class="pun">:</span><span class="pln">
            data </span><span class="pun">=</span><span class="pln"> e</span><span class="pun">.</span><span class="pln">read</span><span class="pun">()</span><span class="pln">  </span><span class="com"># Facebook sends OAuth errors as 400, and urllib2</span><span class="pln">
                             </span><span class="com"># throws an exception, we want a GraphAPIError</span><span class="pln">
        </span><span class="kwd">try</span><span class="pun">:</span><span class="pln">
            response </span><span class="pun">=</span><span class="pln"> _parse_json</span><span class="pun">(</span><span class="pln">data</span><span class="pun">)</span><span class="pln">
            </span><span class="com"># Raise an error if we got one, but don't not if Facebook just</span><span class="pln">
            </span><span class="com"># gave us a Bool value</span><span class="pln">
            </span><span class="kwd">if</span><span class="pln"> </span><span class="pun">(</span><span class="pln">response </span><span class="kwd">and</span><span class="pln"> isinstance</span><span class="pun">(</span><span class="pln">response</span><span class="pun">,</span><span class="pln"> dict</span><span class="pun">)</span><span class="pln"> </span><span class="kwd">and</span><span class="pln">
                response</span><span class="pun">.</span><span class="kwd">get</span><span class="pun">(</span><span class="str">"error"</span><span class="pun">)):</span><span class="pln">
                </span><span class="kwd">raise</span><span class="pln"> </span><span class="typ">GraphAPIError</span><span class="pun">(</span><span class="pln">response</span><span class="pun">)</span><span class="pln">
        </span><span class="kwd">except</span><span class="pln"> </span><span class="typ">ValueError</span><span class="pun">:</span><span class="pln">
            response </span><span class="pun">=</span><span class="pln"> data

        </span><span class="kwd">return</span><span class="pln"> response

    </span><span class="com"># based on: http://code.activestate.com/recipes/146306/</span><span class="pln">
    </span><span class="kwd">def</span><span class="pln"> _encode_multipart_form</span><span class="pun">(</span><span class="kwd">self</span><span class="pun">,</span><span class="pln"> fields</span><span class="pun">):</span><span class="pln">
        </span><span class="str">"""Encode files as 'multipart/form-data'.

        Fields are a dict of form name-&gt; value. For files, value should
        be a file object. Other file-like objects might work and a fake
        name will be chosen.

        Returns (content_type, body) ready for httplib.HTTP instance.

        """</span><span class="pln">
        BOUNDARY </span><span class="pun">=</span><span class="pln"> </span><span class="str">'----------ThIs_Is_tHe_bouNdaRY_$'</span><span class="pln">
        CRLF </span><span class="pun">=</span><span class="pln"> </span><span class="str">'\r\n'</span><span class="pln">
        L </span><span class="pun">=</span><span class="pln"> </span><span class="pun">[]</span><span class="pln">
        </span><span class="kwd">for</span><span class="pln"> </span><span class="pun">(</span><span class="pln">key</span><span class="pun">,</span><span class="pln"> value</span><span class="pun">)</span><span class="pln"> </span><span class="kwd">in</span><span class="pln"> fields</span><span class="pun">.</span><span class="pln">items</span><span class="pun">():</span><span class="pln">
            logging</span><span class="pun">.</span><span class="pln">debug</span><span class="pun">(</span><span class="str">"Encoding %s, (%s)%s"</span><span class="pln"> </span><span class="pun">%</span><span class="pln"> </span><span class="pun">(</span><span class="pln">key</span><span class="pun">,</span><span class="pln"> type</span><span class="pun">(</span><span class="pln">value</span><span class="pun">),</span><span class="pln"> value</span><span class="pun">))</span><span class="pln">
            </span><span class="kwd">if</span><span class="pln"> </span><span class="kwd">not</span><span class="pln"> value</span><span class="pun">:</span><span class="pln">
                </span><span class="kwd">continue</span><span class="pln">
            L</span><span class="pun">.</span><span class="pln">append</span><span class="pun">(</span><span class="str">'--'</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> BOUNDARY</span><span class="pun">)</span><span class="pln">
            </span><span class="kwd">if</span><span class="pln"> hasattr</span><span class="pun">(</span><span class="pln">value</span><span class="pun">,</span><span class="pln"> </span><span class="str">'read'</span><span class="pun">)</span><span class="pln"> </span><span class="kwd">and</span><span class="pln"> callable</span><span class="pun">(</span><span class="pln">value</span><span class="pun">.</span><span class="pln">read</span><span class="pun">):</span><span class="pln">
                filename </span><span class="pun">=</span><span class="pln"> getattr</span><span class="pun">(</span><span class="pln">value</span><span class="pun">,</span><span class="pln"> </span><span class="str">'name'</span><span class="pun">,</span><span class="pln"> </span><span class="str">'%s.jpg'</span><span class="pln"> </span><span class="pun">%</span><span class="pln"> key</span><span class="pun">)</span><span class="pln">
                L</span><span class="pun">.</span><span class="pln">append</span><span class="pun">((</span><span class="str">'Content-Disposition: form-data;'</span><span class="pln">
                          </span><span class="str">'name="%s";'</span><span class="pln">
                          </span><span class="str">'filename="%s"'</span><span class="pun">)</span><span class="pln"> </span><span class="pun">%</span><span class="pln"> </span><span class="pun">(</span><span class="pln">key</span><span class="pun">,</span><span class="pln"> filename</span><span class="pun">))</span><span class="pln">
                L</span><span class="pun">.</span><span class="pln">append</span><span class="pun">(</span><span class="str">'Content-Type: image/jpeg'</span><span class="pun">)</span><span class="pln">
                value </span><span class="pun">=</span><span class="pln"> value</span><span class="pun">.</span><span class="pln">read</span><span class="pun">()</span><span class="pln">
                logging</span><span class="pun">.</span><span class="pln">debug</span><span class="pun">(</span><span class="pln">type</span><span class="pun">(</span><span class="pln">value</span><span class="pun">))</span><span class="pln">
            </span><span class="kwd">else</span><span class="pun">:</span><span class="pln">
                L</span><span class="pun">.</span><span class="pln">append</span><span class="pun">(</span><span class="str">'Content-Disposition: form-data; name="%s"'</span><span class="pln"> </span><span class="pun">%</span><span class="pln"> key</span><span class="pun">)</span><span class="pln">
            L</span><span class="pun">.</span><span class="pln">append</span><span class="pun">(</span><span class="str">''</span><span class="pun">)</span><span class="pln">
            </span><span class="kwd">if</span><span class="pln"> isinstance</span><span class="pun">(</span><span class="pln">value</span><span class="pun">,</span><span class="pln"> unicode</span><span class="pun">):</span><span class="pln">
                logging</span><span class="pun">.</span><span class="pln">debug</span><span class="pun">(</span><span class="str">"Convert to ascii"</span><span class="pun">)</span><span class="pln">
                value </span><span class="pun">=</span><span class="pln"> value</span><span class="pun">.</span><span class="pln">encode</span><span class="pun">(</span><span class="str">'ascii'</span><span class="pun">)</span><span class="pln">
            L</span><span class="pun">.</span><span class="pln">append</span><span class="pun">(</span><span class="pln">value</span><span class="pun">)</span><span class="pln">
        L</span><span class="pun">.</span><span class="pln">append</span><span class="pun">(</span><span class="str">'--'</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> BOUNDARY </span><span class="pun">+</span><span class="pln"> </span><span class="str">'--'</span><span class="pun">)</span><span class="pln">
        L</span><span class="pun">.</span><span class="pln">append</span><span class="pun">(</span><span class="str">''</span><span class="pun">)</span><span class="pln">
        body </span><span class="pun">=</span><span class="pln"> CRLF</span><span class="pun">.</span><span class="pln">join</span><span class="pun">(</span><span class="pln">L</span><span class="pun">)</span><span class="pln">
        content_type </span><span class="pun">=</span><span class="pln"> </span><span class="str">'multipart/form-data; boundary=%s'</span><span class="pln"> </span><span class="pun">%</span><span class="pln"> BOUNDARY
        </span><span class="kwd">return</span><span class="pln"> content_type</span><span class="pun">,</span><span class="pln"> body

    </span><span class="kwd">def</span><span class="pln"> request</span><span class="pun">(</span><span class="kwd">self</span><span class="pun">,</span><span class="pln"> path</span><span class="pun">,</span><span class="pln"> args</span><span class="pun">=</span><span class="kwd">None</span><span class="pun">,</span><span class="pln"> post_args</span><span class="pun">=</span><span class="kwd">None</span><span class="pun">):</span><span class="pln">
        </span><span class="str">"""Fetches the given path in the Graph API.

        We translate args to a valid query string. If post_args is
        given, we send a POST request to the given path with the given
        arguments.

        """</span><span class="pln">
        args </span><span class="pun">=</span><span class="pln"> args </span><span class="kwd">or</span><span class="pln"> </span><span class="pun">{}</span><span class="pln">

        </span><span class="kwd">if</span><span class="pln"> </span><span class="kwd">self</span><span class="pun">.</span><span class="pln">access_token</span><span class="pun">:</span><span class="pln">
            </span><span class="kwd">if</span><span class="pln"> post_args </span><span class="kwd">is</span><span class="pln"> </span><span class="kwd">not</span><span class="pln"> </span><span class="kwd">None</span><span class="pun">:</span><span class="pln">
                post_args</span><span class="pun">[</span><span class="str">"access_token"</span><span class="pun">]</span><span class="pln"> </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">self</span><span class="pun">.</span><span class="pln">access_token
            </span><span class="kwd">else</span><span class="pun">:</span><span class="pln">
                args</span><span class="pun">[</span><span class="str">"access_token"</span><span class="pun">]</span><span class="pln"> </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">self</span><span class="pun">.</span><span class="pln">access_token
        post_data </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">None</span><span class="pln"> </span><span class="kwd">if</span><span class="pln"> post_args </span><span class="kwd">is</span><span class="pln"> </span><span class="kwd">None</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> urllib</span><span class="pun">.</span><span class="pln">urlencode</span><span class="pun">(</span><span class="pln">post_args</span><span class="pun">)</span><span class="pln">
        </span><span class="kwd">try</span><span class="pun">:</span><span class="pln">
            file </span><span class="pun">=</span><span class="pln"> urllib2</span><span class="pun">.</span><span class="pln">urlopen</span><span class="pun">(</span><span class="str">"https://graph.facebook.com/"</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> path </span><span class="pun">+</span><span class="pln"> </span><span class="str">"?"</span><span class="pln"> </span><span class="pun">+</span><span class="pln">
                    urllib</span><span class="pun">.</span><span class="pln">urlencode</span><span class="pun">(</span><span class="pln">args</span><span class="pun">),</span><span class="pln"> post_data</span><span class="pun">,</span><span class="pln"> timeout</span><span class="pun">=</span><span class="kwd">self</span><span class="pun">.</span><span class="pln">timeout</span><span class="pun">)</span><span class="pln">
        </span><span class="kwd">except</span><span class="pln"> urllib2</span><span class="pun">.</span><span class="typ">HTTPError</span><span class="pun">,</span><span class="pln"> e</span><span class="pun">:</span><span class="pln">
            response </span><span class="pun">=</span><span class="pln"> _parse_json</span><span class="pun">(</span><span class="pln">e</span><span class="pun">.</span><span class="pln">read</span><span class="pun">())</span><span class="pln">
            </span><span class="kwd">raise</span><span class="pln"> </span><span class="typ">GraphAPIError</span><span class="pun">(</span><span class="pln">response</span><span class="pun">)</span><span class="pln">
        </span><span class="kwd">except</span><span class="pln"> </span><span class="typ">TypeError</span><span class="pun">:</span><span class="pln">
            </span><span class="com"># Timeout support for Python &lt;2.6</span><span class="pln">
            </span><span class="kwd">if</span><span class="pln"> </span><span class="kwd">self</span><span class="pun">.</span><span class="pln">timeout</span><span class="pun">:</span><span class="pln">
                socket</span><span class="pun">.</span><span class="pln">setdefaulttimeout</span><span class="pun">(</span><span class="kwd">self</span><span class="pun">.</span><span class="pln">timeout</span><span class="pun">)</span><span class="pln">
            file </span><span class="pun">=</span><span class="pln"> urllib2</span><span class="pun">.</span><span class="pln">urlopen</span><span class="pun">(</span><span class="str">"https://graph.facebook.com/"</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> path </span><span class="pun">+</span><span class="pln"> </span><span class="str">"?"</span><span class="pln"> </span><span class="pun">+</span><span class="pln">
                                    urllib</span><span class="pun">.</span><span class="pln">urlencode</span><span class="pun">(</span><span class="pln">args</span><span class="pun">),</span><span class="pln"> post_data</span><span class="pun">)</span><span class="pln">
        </span><span class="kwd">try</span><span class="pun">:</span><span class="pln">
            fileInfo </span><span class="pun">=</span><span class="pln"> file</span><span class="pun">.</span><span class="pln">info</span><span class="pun">()</span><span class="pln">
            </span><span class="kwd">if</span><span class="pln"> fileInfo</span><span class="pun">.</span><span class="pln">maintype </span><span class="pun">==</span><span class="pln"> </span><span class="str">'text'</span><span class="pun">:</span><span class="pln">
                response </span><span class="pun">=</span><span class="pln"> _parse_json</span><span class="pun">(</span><span class="pln">file</span><span class="pun">.</span><span class="pln">read</span><span class="pun">())</span><span class="pln">
            </span><span class="kwd">elif</span><span class="pln"> fileInfo</span><span class="pun">.</span><span class="pln">maintype </span><span class="pun">==</span><span class="pln"> </span><span class="str">'image'</span><span class="pun">:</span><span class="pln">
                mimetype </span><span class="pun">=</span><span class="pln"> fileInfo</span><span class="pun">[</span><span class="str">'content-type'</span><span class="pun">]</span><span class="pln">
                response </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{</span><span class="pln">
                    </span><span class="str">"data"</span><span class="pun">:</span><span class="pln"> file</span><span class="pun">.</span><span class="pln">read</span><span class="pun">(),</span><span class="pln">
                    </span><span class="str">"mime-type"</span><span class="pun">:</span><span class="pln"> mimetype</span><span class="pun">,</span><span class="pln">
                    </span><span class="str">"url"</span><span class="pun">:</span><span class="pln"> file</span><span class="pun">.</span><span class="pln">url</span><span class="pun">,</span><span class="pln">
                </span><span class="pun">}</span><span class="pln">
            </span><span class="kwd">else</span><span class="pun">:</span><span class="pln">
                </span><span class="kwd">raise</span><span class="pln"> </span><span class="typ">GraphAPIError</span><span class="pun">(</span><span class="str">'Maintype was not text or image'</span><span class="pun">)</span><span class="pln">
        </span><span class="kwd">finally</span><span class="pun">:</span><span class="pln">
            file</span><span class="pun">.</span><span class="pln">close</span><span class="pun">()</span><span class="pln">
        </span><span class="kwd">if</span><span class="pln"> response </span><span class="kwd">and</span><span class="pln"> isinstance</span><span class="pun">(</span><span class="pln">response</span><span class="pun">,</span><span class="pln"> dict</span><span class="pun">)</span><span class="pln"> </span><span class="kwd">and</span><span class="pln"> response</span><span class="pun">.</span><span class="kwd">get</span><span class="pun">(</span><span class="str">"error"</span><span class="pun">):</span><span class="pln">
            </span><span class="kwd">raise</span><span class="pln"> </span><span class="typ">GraphAPIError</span><span class="pun">(</span><span class="pln">response</span><span class="pun">[</span><span class="str">"error"</span><span class="pun">][</span><span class="str">"type"</span><span class="pun">],</span><span class="pln">
                                response</span><span class="pun">[</span><span class="str">"error"</span><span class="pun">][</span><span class="str">"message"</span><span class="pun">])</span><span class="pln">
        </span><span class="kwd">return</span><span class="pln"> response

    </span><span class="kwd">def</span><span class="pln"> api_request</span><span class="pun">(</span><span class="kwd">self</span><span class="pun">,</span><span class="pln"> path</span><span class="pun">,</span><span class="pln"> args</span><span class="pun">=</span><span class="kwd">None</span><span class="pun">,</span><span class="pln"> post_args</span><span class="pun">=</span><span class="kwd">None</span><span class="pun">):</span><span class="pln">
        </span><span class="str">"""Fetches the given path in the Graph API.

        We translate args to a valid query string. If post_args is
        given, we send a POST request to the given path with the given
        arguments.

        """</span><span class="pln">
        args </span><span class="pun">=</span><span class="pln"> args </span><span class="kwd">or</span><span class="pln"> </span><span class="pun">{}</span><span class="pln">
        </span><span class="kwd">if</span><span class="pln"> </span><span class="kwd">self</span><span class="pun">.</span><span class="pln">access_token</span><span class="pun">:</span><span class="pln">
            </span><span class="kwd">if</span><span class="pln"> post_args </span><span class="kwd">is</span><span class="pln"> </span><span class="kwd">not</span><span class="pln"> </span><span class="kwd">None</span><span class="pun">:</span><span class="pln">
                post_args</span><span class="pun">[</span><span class="str">"access_token"</span><span class="pun">]</span><span class="pln"> </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">self</span><span class="pun">.</span><span class="pln">access_token
            </span><span class="kwd">else</span><span class="pun">:</span><span class="pln">
                args</span><span class="pun">[</span><span class="str">"access_token"</span><span class="pun">]</span><span class="pln"> </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">self</span><span class="pun">.</span><span class="pln">access_token
        </span><span class="kwd">if</span><span class="pln"> </span><span class="kwd">self</span><span class="pun">.</span><span class="pln">api_key</span><span class="pun">:</span><span class="pln">
            </span><span class="kwd">if</span><span class="pln"> post_args </span><span class="kwd">is</span><span class="pln"> </span><span class="kwd">not</span><span class="pln"> </span><span class="kwd">None</span><span class="pun">:</span><span class="pln">
                post_args</span><span class="pun">[</span><span class="str">"api_key"</span><span class="pun">]</span><span class="pln"> </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">self</span><span class="pun">.</span><span class="pln">api_key
            </span><span class="kwd">else</span><span class="pun">:</span><span class="pln">
                args</span><span class="pun">[</span><span class="str">"api_key"</span><span class="pun">]</span><span class="pln"> </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">self</span><span class="pun">.</span><span class="pln">api_key
        </span><span class="kwd">if</span><span class="pln"> post_args </span><span class="kwd">is</span><span class="pln"> </span><span class="kwd">not</span><span class="pln"> </span><span class="kwd">None</span><span class="pun">:</span><span class="pln">
            post_args</span><span class="pun">[</span><span class="str">"format"</span><span class="pun">]</span><span class="pln"> </span><span class="pun">=</span><span class="pln"> </span><span class="str">"json-strings"</span><span class="pln">
        </span><span class="kwd">else</span><span class="pun">:</span><span class="pln">
            args</span><span class="pun">[</span><span class="str">"format"</span><span class="pun">]</span><span class="pln"> </span><span class="pun">=</span><span class="pln"> </span><span class="str">"json-strings"</span><span class="pln">
        post_data </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">None</span><span class="pln"> </span><span class="kwd">if</span><span class="pln"> post_args </span><span class="kwd">is</span><span class="pln"> </span><span class="kwd">None</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> urllib</span><span class="pun">.</span><span class="pln">urlencode</span><span class="pun">(</span><span class="pln">post_args</span><span class="pun">)</span><span class="pln">
        </span><span class="kwd">try</span><span class="pun">:</span><span class="pln">
            file </span><span class="pun">=</span><span class="pln"> urllib</span><span class="pun">.</span><span class="pln">urlopen</span><span class="pun">(</span><span class="str">"https://api.facebook.com/method/"</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> path </span><span class="pun">+</span><span class="pln">
                    </span><span class="str">"?"</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> urllib</span><span class="pun">.</span><span class="pln">urlencode</span><span class="pun">(</span><span class="pln">args</span><span class="pun">),</span><span class="pln">
                    post_data</span><span class="pun">,</span><span class="pln"> timeout</span><span class="pun">=</span><span class="kwd">self</span><span class="pun">.</span><span class="pln">timeout</span><span class="pun">)</span><span class="pln">
        </span><span class="kwd">except</span><span class="pln"> </span><span class="typ">TypeError</span><span class="pun">:</span><span class="pln">
            </span><span class="com"># Timeout support for Python &lt;2.6</span><span class="pln">
            </span><span class="kwd">if</span><span class="pln"> </span><span class="kwd">self</span><span class="pun">.</span><span class="pln">timeout</span><span class="pun">:</span><span class="pln">
                socket</span><span class="pun">.</span><span class="pln">setdefaulttimeout</span><span class="pun">(</span><span class="kwd">self</span><span class="pun">.</span><span class="pln">timeout</span><span class="pun">)</span><span class="pln">
            file </span><span class="pun">=</span><span class="pln"> urllib</span><span class="pun">.</span><span class="pln">urlopen</span><span class="pun">(</span><span class="str">"https://api.facebook.com/method/"</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> path </span><span class="pun">+</span><span class="pln">
                    </span><span class="str">"?"</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> urllib</span><span class="pun">.</span><span class="pln">urlencode</span><span class="pun">(</span><span class="pln">args</span><span class="pun">),</span><span class="pln"> post_data</span><span class="pun">)</span><span class="pln">

        </span><span class="kwd">try</span><span class="pun">:</span><span class="pln">
            response </span><span class="pun">=</span><span class="pln"> _parse_json</span><span class="pun">(</span><span class="pln">file</span><span class="pun">.</span><span class="pln">read</span><span class="pun">())</span><span class="pln">
        </span><span class="kwd">finally</span><span class="pun">:</span><span class="pln">
            file</span><span class="pun">.</span><span class="pln">close</span><span class="pun">()</span><span class="pln">
        </span><span class="kwd">if</span><span class="pln"> response </span><span class="kwd">and</span><span class="pln"> response</span><span class="pun">.</span><span class="kwd">get</span><span class="pun">(</span><span class="str">"error"</span><span class="pun">):</span><span class="pln">
            </span><span class="kwd">raise</span><span class="pln"> </span><span class="typ">GraphAPIError</span><span class="pun">(</span><span class="pln">response</span><span class="pun">)</span><span class="pln">
        </span><span class="kwd">return</span><span class="pln"> response

    </span><span class="kwd">def</span><span class="pln"> fql</span><span class="pun">(</span><span class="kwd">self</span><span class="pun">,</span><span class="pln"> query</span><span class="pun">,</span><span class="pln"> args</span><span class="pun">=</span><span class="kwd">None</span><span class="pun">,</span><span class="pln"> post_args</span><span class="pun">=</span><span class="kwd">None</span><span class="pun">):</span><span class="pln">
        </span><span class="str">"""FQL query.

        Example query: "</span><span class="pln">SELECT affiliations FROM user WHERE uid </span><span class="pun">=</span><span class="pln"> me</span><span class="pun">()</span><span class="str">"

        """</span><span class="pln">
        args </span><span class="pun">=</span><span class="pln"> args </span><span class="kwd">or</span><span class="pln"> </span><span class="pun">{}</span><span class="pln">
        </span><span class="kwd">if</span><span class="pln"> </span><span class="kwd">self</span><span class="pun">.</span><span class="pln">access_token</span><span class="pun">:</span><span class="pln">
            </span><span class="kwd">if</span><span class="pln"> post_args </span><span class="kwd">is</span><span class="pln"> </span><span class="kwd">not</span><span class="pln"> </span><span class="kwd">None</span><span class="pun">:</span><span class="pln">
                post_args</span><span class="pun">[</span><span class="str">"access_token"</span><span class="pun">]</span><span class="pln"> </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">self</span><span class="pun">.</span><span class="pln">access_token
            </span><span class="kwd">else</span><span class="pun">:</span><span class="pln">
                args</span><span class="pun">[</span><span class="str">"access_token"</span><span class="pun">]</span><span class="pln"> </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">self</span><span class="pun">.</span><span class="pln">access_token
        post_data </span><span class="pun">=</span><span class="pln"> </span><span class="kwd">None</span><span class="pln"> </span><span class="kwd">if</span><span class="pln"> post_args </span><span class="kwd">is</span><span class="pln"> </span><span class="kwd">None</span><span class="pln"> </span><span class="kwd">else</span><span class="pln"> urllib</span><span class="pun">.</span><span class="pln">urlencode</span><span class="pun">(</span><span class="pln">post_args</span><span class="pun">)</span><span class="pln">

        </span><span class="str">"""Check if query is a dict and
           use the multiquery method
           else use single query
        """</span><span class="pln">
        </span><span class="kwd">if</span><span class="pln"> </span><span class="kwd">not</span><span class="pln"> isinstance</span><span class="pun">(</span><span class="pln">query</span><span class="pun">,</span><span class="pln"> basestring</span><span class="pun">):</span><span class="pln">
            args</span><span class="pun">[</span><span class="str">"queries"</span><span class="pun">]</span><span class="pln"> </span><span class="pun">=</span><span class="pln"> query
            fql_method </span><span class="pun">=</span><span class="pln"> </span><span class="str">'fql.multiquery'</span><span class="pln">
        </span><span class="kwd">else</span><span class="pun">:</span><span class="pln">
            args</span><span class="pun">[</span><span class="str">"query"</span><span class="pun">]</span><span class="pln"> </span><span class="pun">=</span><span class="pln"> query
            fql_method </span><span class="pun">=</span><span class="pln"> </span><span class="str">'fql.query'</span><span class="pln">

        args</span><span class="pun">[</span><span class="str">"format"</span><span class="pun">]</span><span class="pln"> </span><span class="pun">=</span><span class="pln"> </span><span class="str">"json"</span><span class="pln">

        </span><span class="kwd">try</span><span class="pun">:</span><span class="pln">
            file </span><span class="pun">=</span><span class="pln"> urllib2</span><span class="pun">.</span><span class="pln">urlopen</span><span class="pun">(</span><span class="str">"https://api.facebook.com/method/"</span><span class="pln"> </span><span class="pun">+</span><span class="pln">
                               fql_method </span><span class="pun">+</span><span class="pln"> </span><span class="str">"?"</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> urllib</span><span class="pun">.</span><span class="pln">urlencode</span><span class="pun">(</span><span class="pln">args</span><span class="pun">),</span><span class="pln">
                               post_data</span><span class="pun">,</span><span class="pln"> timeout</span><span class="pun">=</span><span class="kwd">self</span><span class="pun">.</span><span class="pln">timeout</span><span class="pun">)</span><span class="pln">
        </span><span class="kwd">except</span><span class="pln"> </span><span class="typ">TypeError</span><span class="pun">:</span><span class="pln">
            </span><span class="com"># Timeout support for Python &lt;2.6</span><span class="pln">
            </span><span class="kwd">if</span><span class="pln"> </span><span class="kwd">self</span><span class="pun">.</span><span class="pln">timeout</span><span class="pun">:</span><span class="pln">
                socket</span><span class="pun">.</span><span class="pln">setdefaulttimeout</span><span class="pun">(</span><span class="kwd">self</span><span class="pun">.</span><span class="pln">timeout</span><span class="pun">)</span><span class="pln">
            file </span><span class="pun">=</span><span class="pln"> urllib2</span><span class="pun">.</span><span class="pln">urlopen</span><span class="pun">(</span><span class="str">"https://api.facebook.com/method/"</span><span class="pln"> </span><span class="pun">+</span><span class="pln">
                           fql_method </span><span class="pun">+</span><span class="pln"> </span><span class="str">"?"</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> urllib</span><span class="pun">.</span><span class="pln">urlencode</span><span class="pun">(</span><span class="pln">args</span><span class="pun">),</span><span class="pln">
                           post_data</span><span class="pun">)</span><span class="pln">

        </span><span class="kwd">try</span><span class="pun">:</span><span class="pln">
            content </span><span class="pun">=</span><span class="pln"> file</span><span class="pun">.</span><span class="pln">read</span><span class="pun">()</span><span class="pln">
            response </span><span class="pun">=</span><span class="pln"> _parse_json</span><span class="pun">(</span><span class="pln">content</span><span class="pun">)</span><span class="pln">
            </span><span class="com">#Return a list if success, return a dictionary if failed</span><span class="pln">
            </span><span class="kwd">if</span><span class="pln"> type</span><span class="pun">(</span><span class="pln">response</span><span class="pun">)</span><span class="pln"> </span><span class="kwd">is</span><span class="pln"> dict </span><span class="kwd">and</span><span class="pln"> </span><span class="str">"error_code"</span><span class="pln"> </span><span class="kwd">in</span><span class="pln"> response</span><span class="pun">:</span><span class="pln">
                </span><span class="kwd">raise</span><span class="pln"> </span><span class="typ">GraphAPIError</span><span class="pun">(</span><span class="pln">response</span><span class="pun">)</span><span class="pln">
        </span><span class="kwd">except</span><span class="pln"> </span><span class="typ">Exception</span><span class="pun">,</span><span class="pln"> e</span><span class="pun">:</span><span class="pln">
            </span><span class="kwd">raise</span><span class="pln"> e
        </span><span class="kwd">finally</span><span class="pun">:</span><span class="pln">
            file</span><span class="pun">.</span><span class="pln">close</span><span class="pun">()</span><span class="pln">

        </span><span class="kwd">return</span><span class="pln"> response

    </span><span class="kwd">def</span><span class="pln"> extend_access_token</span><span class="pun">(</span><span class="kwd">self</span><span class="pun">,</span><span class="pln"> app_id</span><span class="pun">,</span><span class="pln"> app_secret</span><span class="pun">):</span><span class="pln">
        </span><span class="str">"""
        Extends the expiration time of a valid OAuth access token. See
        &lt;https://developers.facebook.com/roadmap/offline-access-removal/
        #extend_token&gt;

        """</span><span class="pln">
        args </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{</span><span class="pln">
            </span><span class="str">"client_id"</span><span class="pun">:</span><span class="pln"> app_id</span><span class="pun">,</span><span class="pln">
            </span><span class="str">"client_secret"</span><span class="pun">:</span><span class="pln"> app_secret</span><span class="pun">,</span><span class="pln">
            </span><span class="str">"grant_type"</span><span class="pun">:</span><span class="pln"> </span><span class="str">"fb_exchange_token"</span><span class="pun">,</span><span class="pln">
            </span><span class="str">"fb_exchange_token"</span><span class="pun">:</span><span class="pln"> </span><span class="kwd">self</span><span class="pun">.</span><span class="pln">access_token</span><span class="pun">,</span><span class="pln">
        </span><span class="pun">}</span><span class="pln">
        response </span><span class="pun">=</span><span class="pln"> urllib</span><span class="pun">.</span><span class="pln">urlopen</span><span class="pun">(</span><span class="str">"https://graph.facebook.com/oauth/"</span><span class="pln">
                            </span><span class="str">"access_token?"</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> urllib</span><span class="pun">.</span><span class="pln">urlencode</span><span class="pun">(</span><span class="pln">args</span><span class="pun">)).</span><span class="pln">read</span><span class="pun">()</span><span class="pln">
        query_str </span><span class="pun">=</span><span class="pln"> parse_qs</span><span class="pun">(</span><span class="pln">response</span><span class="pun">)</span><span class="pln">
        </span><span class="kwd">if</span><span class="pln"> </span><span class="str">"access_token"</span><span class="pln"> </span><span class="kwd">in</span><span class="pln"> query_str</span><span class="pun">:</span><span class="pln">
            result </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{</span><span class="str">"access_token"</span><span class="pun">:</span><span class="pln"> query_str</span><span class="pun">[</span><span class="str">"access_token"</span><span class="pun">][</span><span class="lit">0</span><span class="pun">]}</span><span class="pln">
            </span><span class="kwd">if</span><span class="pln"> </span><span class="str">"expires"</span><span class="pln"> </span><span class="kwd">in</span><span class="pln"> query_str</span><span class="pun">:</span><span class="pln">
                result</span><span class="pun">[</span><span class="str">"expires"</span><span class="pun">]</span><span class="pln"> </span><span class="pun">=</span><span class="pln"> query_str</span><span class="pun">[</span><span class="str">"expires"</span><span class="pun">][</span><span class="lit">0</span><span class="pun">]</span><span class="pln">
            </span><span class="kwd">return</span><span class="pln"> result
        </span><span class="kwd">else</span><span class="pun">:</span><span class="pln">
            response </span><span class="pun">=</span><span class="pln"> json</span><span class="pun">.</span><span class="pln">loads</span><span class="pun">(</span><span class="pln">response</span><span class="pun">)</span><span class="pln">
            </span><span class="kwd">raise</span><span class="pln"> </span><span class="typ">GraphAPIError</span><span class="pun">(</span><span class="pln">response</span><span class="pun">)</span><span class="pln">


</span><span class="kwd">class</span><span class="pln"> </span><span class="typ">GraphAPIError</span><span class="pun">(</span><span class="typ">Exception</span><span class="pun">):</span><span class="pln">
    </span><span class="kwd">def</span><span class="pln"> __init__</span><span class="pun">(</span><span class="kwd">self</span><span class="pun">,</span><span class="pln"> result</span><span class="pun">):</span><span class="pln">
        </span><span class="com">#Exception.__init__(self, message)</span><span class="pln">
        </span><span class="com">#self.type = type</span><span class="pln">
        </span><span class="kwd">self</span><span class="pun">.</span><span class="pln">result </span><span class="pun">=</span><span class="pln"> result
        </span><span class="kwd">try</span><span class="pun">:</span><span class="pln">
            </span><span class="kwd">self</span><span class="pun">.</span><span class="pln">type </span><span class="pun">=</span><span class="pln"> result</span><span class="pun">[</span><span class="str">"error_code"</span><span class="pun">]</span><span class="pln">
        </span><span class="kwd">except</span><span class="pun">:</span><span class="pln">
            </span><span class="kwd">self</span><span class="pun">.</span><span class="pln">type </span><span class="pun">=</span><span class="pln"> </span><span class="str">""</span><span class="pln">

        </span><span class="com"># OAuth 2.0 Draft 10</span><span class="pln">
        </span><span class="kwd">try</span><span class="pun">:</span><span class="pln">
            </span><span class="kwd">self</span><span class="pun">.</span><span class="pln">message </span><span class="pun">=</span><span class="pln"> result</span><span class="pun">[</span><span class="str">"error_description"</span><span class="pun">]</span><span class="pln">
        </span><span class="kwd">except</span><span class="pun">:</span><span class="pln">
            </span><span class="com"># OAuth 2.0 Draft 00</span><span class="pln">
            </span><span class="kwd">try</span><span class="pun">:</span><span class="pln">
                </span><span class="kwd">self</span><span class="pun">.</span><span class="pln">message </span><span class="pun">=</span><span class="pln"> result</span><span class="pun">[</span><span class="str">"error"</span><span class="pun">][</span><span class="str">"message"</span><span class="pun">]</span><span class="pln">
            </span><span class="kwd">except</span><span class="pun">:</span><span class="pln">
                </span><span class="com"># REST server style</span><span class="pln">
                </span><span class="kwd">try</span><span class="pun">:</span><span class="pln">
                    </span><span class="kwd">self</span><span class="pun">.</span><span class="pln">message </span><span class="pun">=</span><span class="pln"> result</span><span class="pun">[</span><span class="str">"error_msg"</span><span class="pun">]</span><span class="pln">
                </span><span class="kwd">except</span><span class="pun">:</span><span class="pln">
                    </span><span class="kwd">self</span><span class="pun">.</span><span class="pln">message </span><span class="pun">=</span><span class="pln"> result

        </span><span class="typ">Exception</span><span class="pun">.</span><span class="pln">__init__</span><span class="pun">(</span><span class="kwd">self</span><span class="pun">,</span><span class="pln"> </span><span class="kwd">self</span><span class="pun">.</span><span class="pln">message</span><span class="pun">)</span><span class="pln">


</span><span class="kwd">def</span><span class="pln"> get_user_from_cookie</span><span class="pun">(</span><span class="pln">cookies</span><span class="pun">,</span><span class="pln"> app_id</span><span class="pun">,</span><span class="pln"> app_secret</span><span class="pun">):</span><span class="pln">
    </span><span class="str">"""Parses the cookie set by the official Facebook JavaScript SDK.

    cookies should be a dictionary-like object mapping cookie names to
    cookie values.

    If the user is logged in via Facebook, we return a dictionary with
    the keys "</span><span class="pln">uid</span><span class="str">" and "</span><span class="pln">access_token</span><span class="str">". The former is the user's
    Facebook ID, and the latter can be used to make authenticated
    requests to the Graph API. If the user is not logged in, we
    return None.

    Download the official Facebook JavaScript SDK at
    http://github.com/facebook/connect-js/. Read more about Facebook
    authentication at
    http://developers.facebook.com/docs/authentication/.

    """</span><span class="pln">
    cookie </span><span class="pun">=</span><span class="pln"> cookies</span><span class="pun">.</span><span class="kwd">get</span><span class="pun">(</span><span class="str">"fbsr_"</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> app_id</span><span class="pun">,</span><span class="pln"> </span><span class="str">""</span><span class="pun">)</span><span class="pln">
    </span><span class="kwd">if</span><span class="pln"> </span><span class="kwd">not</span><span class="pln"> cookie</span><span class="pun">:</span><span class="pln">
        </span><span class="kwd">return</span><span class="pln"> </span><span class="kwd">None</span><span class="pln">
    parsed_request </span><span class="pun">=</span><span class="pln"> parse_signed_request</span><span class="pun">(</span><span class="pln">cookie</span><span class="pun">,</span><span class="pln"> app_secret</span><span class="pun">)</span><span class="pln">
    </span><span class="kwd">try</span><span class="pun">:</span><span class="pln">
        result </span><span class="pun">=</span><span class="pln"> get_access_token_from_code</span><span class="pun">(</span><span class="pln">parsed_request</span><span class="pun">[</span><span class="str">"code"</span><span class="pun">],</span><span class="pln"> </span><span class="str">""</span><span class="pun">,</span><span class="pln">
                                          app_id</span><span class="pun">,</span><span class="pln"> app_secret</span><span class="pun">)</span><span class="pln">
    </span><span class="kwd">except</span><span class="pln"> </span><span class="typ">GraphAPIError</span><span class="pun">:</span><span class="pln">
        </span><span class="kwd">return</span><span class="pln"> </span><span class="kwd">None</span><span class="pln">
    result</span><span class="pun">[</span><span class="str">"uid"</span><span class="pun">]</span><span class="pln"> </span><span class="pun">=</span><span class="pln"> parsed_request</span><span class="pun">[</span><span class="str">"user_id"</span><span class="pun">]</span><span class="pln">
    </span><span class="kwd">return</span><span class="pln"> result


</span><span class="kwd">def</span><span class="pln"> parse_signed_request</span><span class="pun">(</span><span class="pln">signed_request</span><span class="pun">,</span><span class="pln"> app_secret</span><span class="pun">):</span><span class="pln">
    </span><span class="str">""" Return dictionary with signed request data.

    We return a dictionary containing the information in the
    signed_request. This includes a user_id if the user has authorised
    your application, as well as any information requested.

    If the signed_request is malformed or corrupted, False is returned.

    """</span><span class="pln">
    </span><span class="kwd">try</span><span class="pun">:</span><span class="pln">
        l </span><span class="pun">=</span><span class="pln"> signed_request</span><span class="pun">.</span><span class="pln">split</span><span class="pun">(</span><span class="str">'.'</span><span class="pun">,</span><span class="pln"> </span><span class="lit">2</span><span class="pun">)</span><span class="pln">
        encoded_sig </span><span class="pun">=</span><span class="pln"> str</span><span class="pun">(</span><span class="pln">l</span><span class="pun">[</span><span class="lit">0</span><span class="pun">])</span><span class="pln">
        payload </span><span class="pun">=</span><span class="pln"> str</span><span class="pun">(</span><span class="pln">l</span><span class="pun">[</span><span class="lit">1</span><span class="pun">])</span><span class="pln">
        sig </span><span class="pun">=</span><span class="pln"> base64</span><span class="pun">.</span><span class="pln">urlsafe_b64decode</span><span class="pun">(</span><span class="pln">encoded_sig </span><span class="pun">+</span><span class="pln"> </span><span class="str">"="</span><span class="pln"> </span><span class="pun">*</span><span class="pln">
                                       </span><span class="pun">((</span><span class="lit">4</span><span class="pln"> </span><span class="pun">-</span><span class="pln"> len</span><span class="pun">(</span><span class="pln">encoded_sig</span><span class="pun">)</span><span class="pln"> </span><span class="pun">%</span><span class="pln"> </span><span class="lit">4</span><span class="pun">)</span><span class="pln"> </span><span class="pun">%</span><span class="pln"> </span><span class="lit">4</span><span class="pun">))</span><span class="pln">
        data </span><span class="pun">=</span><span class="pln"> base64</span><span class="pun">.</span><span class="pln">urlsafe_b64decode</span><span class="pun">(</span><span class="pln">payload </span><span class="pun">+</span><span class="pln"> </span><span class="str">"="</span><span class="pln"> </span><span class="pun">*</span><span class="pln">
                                        </span><span class="pun">((</span><span class="lit">4</span><span class="pln"> </span><span class="pun">-</span><span class="pln"> len</span><span class="pun">(</span><span class="pln">payload</span><span class="pun">)</span><span class="pln"> </span><span class="pun">%</span><span class="pln"> </span><span class="lit">4</span><span class="pun">)</span><span class="pln"> </span><span class="pun">%</span><span class="pln"> </span><span class="lit">4</span><span class="pun">))</span><span class="pln">
    </span><span class="kwd">except</span><span class="pln"> </span><span class="typ">IndexError</span><span class="pun">:</span><span class="pln">
        </span><span class="com"># Signed request was malformed.</span><span class="pln">
        </span><span class="kwd">return</span><span class="pln"> </span><span class="kwd">False</span><span class="pln">
    </span><span class="kwd">except</span><span class="pln"> </span><span class="typ">TypeError</span><span class="pun">:</span><span class="pln">
        </span><span class="com"># Signed request had a corrupted payload.</span><span class="pln">
        </span><span class="kwd">return</span><span class="pln"> </span><span class="kwd">False</span><span class="pln">

    data </span><span class="pun">=</span><span class="pln"> _parse_json</span><span class="pun">(</span><span class="pln">data</span><span class="pun">)</span><span class="pln">
    </span><span class="kwd">if</span><span class="pln"> data</span><span class="pun">.</span><span class="kwd">get</span><span class="pun">(</span><span class="str">'algorithm'</span><span class="pun">,</span><span class="pln"> </span><span class="str">''</span><span class="pun">).</span><span class="pln">upper</span><span class="pun">()</span><span class="pln"> </span><span class="pun">!=</span><span class="pln"> </span><span class="str">'HMAC-SHA256'</span><span class="pun">:</span><span class="pln">
        </span><span class="kwd">return</span><span class="pln"> </span><span class="kwd">False</span><span class="pln">

    </span><span class="com"># HMAC can only handle ascii (byte) strings</span><span class="pln">
    </span><span class="com"># http://bugs.python.org/issue5285</span><span class="pln">
    app_secret </span><span class="pun">=</span><span class="pln"> app_secret</span><span class="pun">.</span><span class="pln">encode</span><span class="pun">(</span><span class="str">'ascii'</span><span class="pun">)</span><span class="pln">
    payload </span><span class="pun">=</span><span class="pln"> payload</span><span class="pun">.</span><span class="pln">encode</span><span class="pun">(</span><span class="str">'ascii'</span><span class="pun">)</span><span class="pln">

    expected_sig </span><span class="pun">=</span><span class="pln"> hmac</span><span class="pun">.</span><span class="kwd">new</span><span class="pun">(</span><span class="pln">app_secret</span><span class="pun">,</span><span class="pln">
                            msg</span><span class="pun">=</span><span class="pln">payload</span><span class="pun">,</span><span class="pln">
                            digestmod</span><span class="pun">=</span><span class="pln">hashlib</span><span class="pun">.</span><span class="pln">sha256</span><span class="pun">).</span><span class="pln">digest</span><span class="pun">()</span><span class="pln">
    </span><span class="kwd">if</span><span class="pln"> sig </span><span class="pun">!=</span><span class="pln"> expected_sig</span><span class="pun">:</span><span class="pln">
        </span><span class="kwd">return</span><span class="pln"> </span><span class="kwd">False</span><span class="pln">

    </span><span class="kwd">return</span><span class="pln"> data


</span><span class="kwd">def</span><span class="pln"> auth_url</span><span class="pun">(</span><span class="pln">app_id</span><span class="pun">,</span><span class="pln"> canvas_url</span><span class="pun">,</span><span class="pln"> perms</span><span class="pun">=</span><span class="kwd">None</span><span class="pun">,</span><span class="pln"> state</span><span class="pun">=</span><span class="kwd">None</span><span class="pun">):</span><span class="pln">
    url </span><span class="pun">=</span><span class="pln"> </span><span class="str">"https://www.facebook.com/dialog/oauth?"</span><span class="pln">
    kvps </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{</span><span class="str">'client_id'</span><span class="pun">:</span><span class="pln"> app_id</span><span class="pun">,</span><span class="pln"> </span><span class="str">'redirect_uri'</span><span class="pun">:</span><span class="pln"> canvas_url</span><span class="pun">}</span><span class="pln">
    </span><span class="kwd">if</span><span class="pln"> perms</span><span class="pun">:</span><span class="pln">
        kvps</span><span class="pun">[</span><span class="str">'scope'</span><span class="pun">]</span><span class="pln"> </span><span class="pun">=</span><span class="pln"> </span><span class="str">","</span><span class="pun">.</span><span class="pln">join</span><span class="pun">(</span><span class="pln">perms</span><span class="pun">)</span><span class="pln">
    </span><span class="kwd">if</span><span class="pln"> state</span><span class="pun">:</span><span class="pln">
        kvps</span><span class="pun">[</span><span class="str">'state'</span><span class="pun">]</span><span class="pln"> </span><span class="pun">=</span><span class="pln"> state
    </span><span class="kwd">return</span><span class="pln"> url </span><span class="pun">+</span><span class="pln"> urllib</span><span class="pun">.</span><span class="pln">urlencode</span><span class="pun">(</span><span class="pln">kvps</span><span class="pun">)</span><span class="pln">


</span><span class="kwd">def</span><span class="pln"> get_access_token_from_code</span><span class="pun">(</span><span class="pln">code</span><span class="pun">,</span><span class="pln"> redirect_uri</span><span class="pun">,</span><span class="pln"> app_id</span><span class="pun">,</span><span class="pln"> app_secret</span><span class="pun">):</span><span class="pln">
    </span><span class="str">"""Get an access token from the "</span><span class="pln">code</span><span class="str">" returned from an OAuth dialog.

    Returns a dict containing the user-specific access token and its
    expiration date (if applicable).

    """</span><span class="pln">
    args </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{</span><span class="pln">
        </span><span class="str">"code"</span><span class="pun">:</span><span class="pln"> code</span><span class="pun">,</span><span class="pln">
        </span><span class="str">"redirect_uri"</span><span class="pun">:</span><span class="pln"> redirect_uri</span><span class="pun">,</span><span class="pln">
        </span><span class="str">"client_id"</span><span class="pun">:</span><span class="pln"> app_id</span><span class="pun">,</span><span class="pln">
        </span><span class="str">"client_secret"</span><span class="pun">:</span><span class="pln"> app_secret</span><span class="pun">,</span><span class="pln">
    </span><span class="pun">}</span><span class="pln">
    </span><span class="com"># We would use GraphAPI.request() here, except for that the fact</span><span class="pln">
    </span><span class="com"># that the response is a key-value pair, and not JSON.</span><span class="pln">
    response </span><span class="pun">=</span><span class="pln"> urllib</span><span class="pun">.</span><span class="pln">urlopen</span><span class="pun">(</span><span class="str">"https://graph.facebook.com/oauth/access_token"</span><span class="pln"> </span><span class="pun">+</span><span class="pln">
                              </span><span class="str">"?"</span><span class="pln"> </span><span class="pun">+</span><span class="pln"> urllib</span><span class="pun">.</span><span class="pln">urlencode</span><span class="pun">(</span><span class="pln">args</span><span class="pun">)).</span><span class="pln">read</span><span class="pun">()</span><span class="pln">
    query_str </span><span class="pun">=</span><span class="pln"> parse_qs</span><span class="pun">(</span><span class="pln">response</span><span class="pun">)</span><span class="pln">
    </span><span class="kwd">if</span><span class="pln"> </span><span class="str">"access_token"</span><span class="pln"> </span><span class="kwd">in</span><span class="pln"> query_str</span><span class="pun">:</span><span class="pln">
        result </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{</span><span class="str">"access_token"</span><span class="pun">:</span><span class="pln"> query_str</span><span class="pun">[</span><span class="str">"access_token"</span><span class="pun">][</span><span class="lit">0</span><span class="pun">]}</span><span class="pln">
        </span><span class="kwd">if</span><span class="pln"> </span><span class="str">"expires"</span><span class="pln"> </span><span class="kwd">in</span><span class="pln"> query_str</span><span class="pun">:</span><span class="pln">
            result</span><span class="pun">[</span><span class="str">"expires"</span><span class="pun">]</span><span class="pln"> </span><span class="pun">=</span><span class="pln"> query_str</span><span class="pun">[</span><span class="str">"expires"</span><span class="pun">][</span><span class="lit">0</span><span class="pun">]</span><span class="pln">
        </span><span class="kwd">return</span><span class="pln"> result
    </span><span class="kwd">else</span><span class="pun">:</span><span class="pln">
        response </span><span class="pun">=</span><span class="pln"> json</span><span class="pun">.</span><span class="pln">loads</span><span class="pun">(</span><span class="pln">response</span><span class="pun">)</span><span class="pln">
        </span><span class="kwd">raise</span><span class="pln"> </span><span class="typ">GraphAPIError</span><span class="pun">(</span><span class="pln">response</span><span class="pun">)</span><span class="pln">


</span><span class="kwd">def</span><span class="pln"> get_app_access_token</span><span class="pun">(</span><span class="pln">app_id</span><span class="pun">,</span><span class="pln"> app_secret</span><span class="pun">):</span><span class="pln">
    </span><span class="str">"""Get the access_token for the app.

    This token can be used for insights and creating test users.

    app_id = retrieved from the developer page
    app_secret = retrieved from the developer page

    Returns the application access_token.

    """</span><span class="pln">
    </span><span class="com"># Get an app access token</span><span class="pln">
    args </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{</span><span class="str">'grant_type'</span><span class="pun">:</span><span class="pln"> </span><span class="str">'client_credentials'</span><span class="pun">,</span><span class="pln">
            </span><span class="str">'client_id'</span><span class="pun">:</span><span class="pln"> app_id</span><span class="pun">,</span><span class="pln">
            </span><span class="str">'client_secret'</span><span class="pun">:</span><span class="pln"> app_secret</span><span class="pun">}</span><span class="pln">

    file </span><span class="pun">=</span><span class="pln"> urllib2</span><span class="pun">.</span><span class="pln">urlopen</span><span class="pun">(</span><span class="str">"https://graph.facebook.com/oauth/access_token?"</span><span class="pln"> </span><span class="pun">+</span><span class="pln">
                              urllib</span><span class="pun">.</span><span class="pln">urlencode</span><span class="pun">(</span><span class="pln">args</span><span class="pun">))</span><span class="pln">

    </span><span class="kwd">try</span><span class="pun">:</span><span class="pln">
        result </span><span class="pun">=</span><span class="pln"> file</span><span class="pun">.</span><span class="pln">read</span><span class="pun">().</span><span class="pln">split</span><span class="pun">(</span><span class="str">"="</span><span class="pun">)[</span><span class="lit">1</span><span class="pun">]</span><span class="pln">
    </span><span class="kwd">finally</span><span class="pun">:</span><span class="pln">
        file</span><span class="pun">.</span><span class="pln">close</span><span class="pun">()</span><span class="pln">

    </span><span class="kwd">return</span><span class="pln"> result </span></code></pre>  <script async="" src="http://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script> <ins class="adsbygoogle" style="display:inline-block;width:728px;height:90px" data-ad-client="ca-pub-7704156438452645" data-ad-slot="4642642597"></ins> <script> (adsbygoogle = window.adsbygoogle || []).push({}); </script> </div> </div> <hr> <footer> <p class="pull-right"><small> Developed by <a href="http://leprofdinfo.fr/">Le Prof d'Info</a> using <a href="http://twitter.github.io/bootstrap/">Twitter Bootstrap</a>, <a href="http://qtip2.com/">qTip2</a> and <a href="https://github.com/themattharris/tmhOAuth">tmhOAuth</a></small></p> <p class="pull-left"><small>© 2013 pythoninside.com</small></p> <p style="text-align:center;"> <a href="http://megasnippets.com/en/">megasnippets.com</a> | <a href="http://dotnetinside.com/en/">dotnetinside.com</a> </p> </footer> <script> jQuery(document).ready(function() {
        jQuery(window.location.hash).collapse('show');
            
        jQuery('[bind=global-search-text]').keypress(function(e){
            if(e.which == 13) {
                var distrib = jQuery('input[bind=global-search-distrib]').val();
                if (!distrib)
                    distrib = 'all';
                location.href = 'search/' + distrib + '/' + jQuery(this).val();
                e.preventDefault();
            }
        })
            
        jQuery('[bind=search-range-selector] a').click(function(e){
            jQuery('[bind=search-range]').text(jQuery(this).text());
            jQuery('[bind=search-range-selector] li').removeClass('active');
            jQuery(this).parent().addClass('active');
                
            jQuery('input[bind=global-search-distrib]').val(jQuery(this).data('d'));
                
            e.preventDefault();
        });

    }); </script> </article> <script src="./facebook_files/bootstrap.min.js"></script><script> (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
            (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
        m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
    })(window,document,'script','//www.google-analytics.com/analytics.js','ga');
    
    ga('create', 'UA-16757229-12', 'pythoninside.com');
    ga('send', 'pageview'); </script>   </body></html>