import urllib.request as web
import xml.etree.ElementTree as ElementTree

class infocaller:
    data = None
    textdata = None
    
    # call the url, and store the data
    def call(self, url):
        self.data = web.urlopen(url)
        self.textdata = self.data.read()

class parser:
    data = None

    def __init__(self, xmldata):
        self.data = xmldata

    def getwarnings(self):
        warnings = []
        xmlroot = ElementTree.fromstring(self.data)
        for warning in xmlroot.iter('hazard'):
            warnings.append(warning.get('headline'))
        return warnings
    
class WeatherInfo:
    def __init__(self, url):
        self.url = url
        self.warnings = []
    
    def update(self):
        self.caller = infocaller()
        self.caller.call(self.url)
        self.parser = parser(self.caller.textdata)
        self.warnings = self.parser.getwarnings()
    
