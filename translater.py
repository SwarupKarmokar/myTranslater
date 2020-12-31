import pyttsx3
import speech_recognition as sr
from googletrans import Translator

engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

listener = sr.Recognizer()

with sr.Microphone() as source:
    print('listening....')
    try:
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
    except:
        print("don't recognize your voice......")

translator = Translator()
output = translator.translate(str(command), dest="en")
print(output.text)
talk(output.text)