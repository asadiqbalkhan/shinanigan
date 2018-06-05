from sys import argv

script , user_name = argv
prompt = '> '

print(" __        __   _"                                )
print(" \ \      / /__| | ___ ___  _ __ ___   ___ "      )
print("  \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _  )"     )
print("   \ V  V /  __/ | (_| (_) | | | | | |  __/"      )
print("    \_/\_/ \___|_|\___\___/|_| |_| |_|\___|"      )
print("\n")

print("I am Jarvis an Artificial Intelligence located in the script %s designed by Mr.%s\n" % (script,user_name))
print("I am going to ask you some questions in order to assess your profile")


# Questions asked here

print("What is your name?")
name = input(prompt)

print("Where do you live?")
lives = input(prompt)

print("What is your relationship status?")
relationship = input(prompt)

print("What is your highest education degree?")
degree = input(prompt)

print("Now I will display your current profile")
print("--------PROFILE---------")
print("Full name: %r\n" % name)
print("Location: %r\n" % lives)
print("Relationship status: %r\n" % relationship)
print("Education: %r\n" %degree)
print("-----------------------")

 
import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
 
def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")
 
def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
    audio = r.listen(source)
 
    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
 
    return data
 
def jarvis(data):
    if "how are you" in data:
        speak("I am fine")
 
    if "what time is it" in data:
        speak(ctime())
 
    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on Asad, I will show you where " + location + " is.")
        os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")
 
# initialization
time.sleep(2)
speak("Hi Asad, what can I do for you?")
while 1:
    data = recordAudio()
    jarvis(data)
