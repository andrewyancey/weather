import pyttsx3
import weather
import time

def displaywarnings(warnings):
    for warning in warnings:
        engine.say(warning)
        print(warning)

def getwarnings():
    mycaller = weather.infocaller()
    mycaller.call()
    myparser = weather.parser(mycaller.textdata)
    warnings = myparser.getwarnings()
    return warnings



#if warning is different from previous warning
#then sound alert

engine = pyttsx3.init()
engine.setProperty('rate', 0.1)
previouswarning = []


cont = False
while cont == False:
    print(previouswarning)
    timestart = time.time()
    currenttime = 0
    currentwarnings = getwarnings()
    if(currentwarnings != previouswarning):
        displaywarnings(currentwarnings)
        previouswarning = currentwarnings
    engine.runAndWait()
    while currenttime < 5:
        currenttime = time.time() - timestart

