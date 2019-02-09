#!/Users/manu/.ve/PythonProgs/bin/python3.7

from xml.etree.ElementTree import XML
import sys
import urllib.request


if len(sys.argv) != 3:
    raise SystemExit('Usage: nextbus.py route stopid')

route = sys.argv[1]
stopid = sys.argv[2]

u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?route={}&stop={}'.format(route, stopid))
data = u.read()

doc = XML(data)

for pt in doc.findall('.//pt'):
    print(pt.text)
