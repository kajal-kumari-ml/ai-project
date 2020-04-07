import speech_recognition as sr
import pyttsx3, requests
import pyaudio
engine = pyttsx3.init()
def off():
    r = requests.get("https://api.thingspeak.com/update?api_key=YHVXZ5WQIDSIMWRF&field1=0")
def on():
    r = requests.get("https://api.thingspeak.com/update?api_key=YHVXZ5WQIDSIMWRF&field1=1")
b = ""
def update_value(b):
    if (b == "light on"):
        on()
        print('ON')
    elif (b == "light off"):
        off()
        print('OFF')
# Record Audio
r = sr.Recognizer()
r.energy_threshold = 2100
engine.say("Hello mam")
engine.say("Say something!")
engine.runAndWait()
while True:
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    # Speech recognition using Google Speech Recognition
    try:
        print("You said: " + r.recognize_google(audio))
        x = r.recognize_google(audio)
        update_value(x)
        engine.say(r.recognize_google(audio))
        engine.runAndWait()
        engine.say("Say something!")
        engine.runAndWait()
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        engine.say("Google Speech Recognition could not understand audio")
        engine.runAndWait()
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        # engine.say("Could not request results from Google Speech Recognition service; {0}".format(e))
        # engine.runAndWait()
