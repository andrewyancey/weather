import pyttsx3, weather, time

# define global variables
engine = None
emergency = True
weather_info = None
url = "https://forecast.weather.gov/MapClick.php?lat=39.32&lon=-105.9&unit=0&lg=english&FcstType=dwml"

def init_tts():
    # Initialize pyttsx3 engine
    global engine
    engine = pyttsx3.init()
    engine.setProperty('rate', 0.1)

def init_info():
    global weather_info
    weather_info = weather.WeatherInfo(url)

def display_warnings(warnings):
    #Displays the given warnings and speaks them aloud using pyttsx3.
    for warning in warnings:
        engine.say(warning)
        print(warning)

def get_warnings():
    weather_info.update()
    return weather_info.warnings


def wait(waittime):
        # set up time variables
        timestart = time.time()
        current_time = 0
        # Wait for 5 seconds before checking again
        while current_time < waittime:
            current_time = time.time() - timestart

def run():
    global emergency
    previous_warnings = []
    # Main loop
    while True:
        current_warnings = get_warnings()
        #Check if emergency mode is on.
        if emergency == False:
            # Check if warnings have changed since last loop iteration
            if current_warnings != previous_warnings:
                display_warnings(current_warnings)
                previous_warnings = current_warnings
        else:
            display_warnings(current_warnings)
            previous_warnings = current_warnings
        # Speak any pending messages using pyttsx3
        engine.runAndWait()
        wait(5)

# begin main program
init_tts()
init_info()
run()