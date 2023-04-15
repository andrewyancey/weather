import urllib.request as web
import xml.etree.ElementTree as et

class infocaller:
    url = "https://forecast.weather.gov/MapClick.php?lat=35.3092&lon=-99.1859&unit=0&lg=english&FcstType=dwml"
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
