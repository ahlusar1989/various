from xml.dom.minidom import parse, parseString
from xml.sax.saxutils import unescape

def getText(nodelist):
    rc = ""
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc = rc + node.data
    return rc

dom = parse('C:\\Program Files\\Compuware\\Uniface 9.3.01\\project\\bin\\COPS_GOODS_IN.cmx')
tags = dom.getElementsByTagName('DAT')
for t in tags:
    if t.attributes["name"].value == "FORMPIC":
        print t.childNodes
        print unescape(getText(t.childNodes))

