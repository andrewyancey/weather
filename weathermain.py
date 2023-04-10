import urllib.request as web
import xml.etree.ElementTree as et

class infocaller:
    url = "https://forecast.weather.gov/MapClick.php?lat=38.0993&lon=-84.4431&unit=0&lg=english&FcstType=dwml"

    def _init_(self):
        return

    def call(self):
        data = web.urlopen(self.url)
        return data

class parser:

    def warnings(data):
        warnings = []
        xmlroot = et.fromstring(data)
        for warning in xmlroot.iter('hazard'):
            warnings.append(warning.get('headline'))
        return warnings



mycaller = infocaller()
data = mycaller.call().read()
warnings = parser.warnings(data)
for warning in warnings:
    print(warning)

