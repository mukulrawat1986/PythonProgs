# nextbus.py

from xml.etree.ElementTree import XML
import urllib.request

u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?route=22&stop=14787')
data = u.read()


doc = XML(data)

for pt in doc.findall('.//pt'):
    print(pt.text)
