import urllib.request as web
import xml.etree.ElementTree as et
import time


class infocaller:
    url = "https://forecast.weather.gov/MapClick.php?lat=47.0542&lon=-111.2936&unit=0&lg=english&FcstType=dwml"
    data = None
    textdata = None
    
    def __init__(self):
        return

    def call(self):
        self.data = web.urlopen(self.url)
        self.textdata = self.data.read()

class parser:

    data = None

    def __init__(self, xmldata):
        self.data = xmldata

    def getwarnings(self):
        warnings = []
        xmlroot = et.fromstring(self.data)
        for warning in xmlroot.iter('hazard'):
            warnings.append(warning.get('headline'))
        return warnings

def displaywarnings():
    mycaller = infocaller()
    mycaller.call()
    myparser = parser(mycaller.textdata)
    warnings = myparser.getwarnings()
    for warning in warnings:
        print(warning)

b = False
while b == False:
    ts = time.time()
    t = 0
    displaywarnings() 
    while t < 30:
        t = time.time() - ts

