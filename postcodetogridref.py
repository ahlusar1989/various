import urllib, re

postcode = urllib.quote('NW2 5JU')
print "http://www.streetmap.co.uk/streetmap.dll?GridConvert?name=%s&type=PostCode" % (postcode)
streetmap = urllib.urlopen("http://www.streetmap.co.uk/streetmap.dll?GridConvert?name=%s&type=PostCode" % (postcode))
html = streetmap.read()

def scrape(attr, html):
  match = re.search('<strong>'+attr+'</strong> </td> <td width="50%" align="center" valign="middle">(.*?)</td>', html)
  return match.group(1)

print scrape('LR', html)
