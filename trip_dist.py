import urllib, re

page1 = { 'url' : "http://www.postcode.org.uk/country/uk/_postcode-distance-calculator.asp?SPC=%s&FPC=%s&Submit=Calculate+Distance", 'mask':'<strong>&nbsp;(.*?)&nbsp;&nbsp;</strong></font></td>\r\n  </tr>' }
page2 = { 'url' : "http://www.driving-distances.com/distances-between-calculator.php?from=%s&to=%s", 'mask': 'align=\'center\'>(.*?)</td></tr></table>' }
        
def trip(web, pointa='BS7 9LE', pointb='NW2 5JU'):
    pointa = urllib.quote(pointa)
    pointb = urllib.quote(pointb)
    url = web['url'] % (pointa, pointb)
    data = urllib.urlopen(url)
    html = data.read()
    match = re.search(web['mask'], html)
    return match.group(1)

print trip(page1)
print trip(page2)
