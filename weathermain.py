import pyttsx3
import weather
#import urllib.request as web
#import xml.etree.ElementTree as et
import time

def displaywarnings():
    mycaller = weather.infocaller()
    mycaller.call()
    myparser = weather.parser(mycaller.textdata)
    warnings = myparser.getwarnings()
    for warning in warnings:
        engine.say(warning)
        print(warning)


engine = pyttsx3.init()
engine.setProperty('rate', 0.1)

b = False
while b == False:
    ts = time.time()
    t = 0
    displaywarnings() 
    engine.runAndWait()
    while t < 30:
        t = time.time() - ts

