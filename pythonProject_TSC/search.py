import speech_recognition as sr # recognise speech
import playsound # to play an audio file
from gtts import gTTS # google text to speech
import random
from time import ctime # get time details
import webbrowser # open browser

import time
import os # to remove created audio files

class person:
    name = ''
    def setName(self, name):
        self.name = name

def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

r = sr.Recognizer() # initialise a recogniser
# listen for audio and convert it to text:
def record_audio(ask=False):
    with sr.Microphone() as source: # microphone as source
        if ask:
            speak(ask)
        audio = r.listen(source)  # listen for the audio via source
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError: # error: recognizer does not understand
            speak('I did not get that')
        except sr.RequestError:
            speak('Sorry, the service is down') # error: recognizer is not connected
        print(f">> {voice_data.lower()}") # print what user said
        return voice_data.lower()

# get string and make a audio file to be played
def speak(audio_string):
    tts = gTTS(text=audio_string, lang='en') # text to speech(voice)
    r = random.randint(1,20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file) # save as mp3
    playsound.playsound(audio_file) # play the audio file
    print(f"TSC: {audio_string}") # print what app said
    os.remove(audio_file) # remove audio file

def respond(voice_data):
    # 1: greeting
    if there_exists(['hey','hi','hello']):
        greetings = [f"hey, how can I help you {person_obj.name}", f"hey, what's up? {person_obj.name}", f"I'm listening {person_obj.name}", f"how can I help you? {person_obj.name}", f"hello {person_obj.name}"]
        greet = greetings[random.randint(0,len(greetings)-1)]
        speak(greet)

    # 2: name
    if there_exists(["what is your name","what's your name","tell me your name"]):
        if person_obj.name:
            speak("my name is TSC")
        else:
            speak("my name is TSC. what's your name?")

    if there_exists(["my name is"]):
        person_name = voice_data.split("is")[-1].strip()
        speak(f"okay, i will remember that {person_name}")
        person_obj.setName(person_name) # remember name in person object

    # 3: greeting
    if there_exists(["how are you","how are you doing"]):
        speak(f"I'm very well, thanks for asking {person_obj.name}")

    # 4: time
    if there_exists(["what's the time","tell me the time","what time is it"]):
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = f'{hours} {minutes}'
        speak(time)

    # 5: search google
    if there_exists(["search for"]) and 'youtube' not in voice_data:
        search_term = voice_data.split("for")[-1]
        url = f"https://google.com/search?q={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found {search_term}')

    # 6: search facebook
    if there_exists(["facebook"]):
        search_term = voice_data.split("for")[-1]
        url = f"https://www.facebook.com/search?q={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found {search_term}')

    # 7: search instagram
    if there_exists(["instagram"]):
        search_term = voice_data.split("for")[-1]
        url = f"https://www.instagram.com/search?q={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found {search_term}')

    # 8: search twitter
    if there_exists(["twitter"]):
        search_term = voice_data.split("for")[-1]
        url = f"https://twitter.com/search?q={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found {search_term}')

    # 9: search google scholar
    if there_exists(["google scholar"]):
        search_term = voice_data.split("for")[-1]
        url = f"https://scholar.google.com/search?q={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found {search_term}')

    # 10: search javatpoint
    if there_exists(["javatpoint"]):
        search_term = voice_data.split("for")[-1]
        url = f"https://www.javatpoint.com/search?q={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found {search_term}')

    # 11: search geeks for geeks
    if there_exists(["geeks for geeks"]):
        search_term = voice_data.split("for")[-1]
        url = f"https://www.geeksforgeeks.org/search?q={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found {search_term}')

    # 12: search tutorialspoint
    if there_exists(["tutorialspoint"]):
        search_term = voice_data.split("for")[-1]
        url = f"https://www.tutorialspoint.com/search?q={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found {search_term}')

    # 13: search alibaba
    if there_exists(["alibaba"]):
        search_term = voice_data.split("for")[-1]
        url = f"https://www.alibaba.com/search?q={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found {search_term}')
    # 14: search amazon
    if there_exists(["amazon"]):
        search_term = voice_data.split("for")[-1]
        url = f"https://www.amazon.com/search?q={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found {search_term}')

    # 15: search daraz
    if there_exists(["daraz"]):
        search_term = voice_data.split("for")[-1]
        url = f"https://www.daraz.com.bd/search?q={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found {search_term}')

    # 16: search github
    if there_exists(["github"]):
        search_term = voice_data.split("for")[-1]
        url = f"https://github.com/search?q={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found {search_term}')

    # 17: search crazy programmer
    if there_exists(["crazy programmer"]):
        search_term = voice_data.split("for")[-1]
        url = f"https://www.thecrazyprogrammer.com/search?q={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found {search_term}')

    # 18: search w3 schools
    if there_exists(["w3 schools"]):
        search_term = voice_data.split("for")[-1]
        url = f"https://www.w3schools.com/search?q={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found {search_term}')

    # 19: search wikipedia
    if there_exists(["wikipedia"]):
        search_term = voice_data.split("for")[-1]
        url = f"https://www.wikipedia.org/search?q={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found {search_term}')


    # 20: search youtube
    if there_exists(["youtube"]):
        search_term = voice_data.split("for")[-1]
        url = f"https://www.youtube.com/results?search_query={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found for {search_term} on youtube')

    # 21: find location
    if 'find location' in voice_data:
        location = record_audio('what is the location?')
        url = 'https://www.google.com/maps/@23.6131425,90.4926857,14z' + location + '/&amp;'
        webbrowser.get().open(url)
        print('here is the location' + location)

    # 22: get stock price
    if there_exists(["price of"]):
        search_term = voice_data.lower().split(" of ")[-1].strip() #strip removes whitespace after/before a term in string
        stocks = {
            "apple":"AAPL",
            "microsoft":"MSFT",
            "facebook":"FB",
            "tesla":"TSLA",
            "bitcoin":"BTC-USD"
        }
        try:
            stock = stocks[search_term]
            stock = yf.Ticker(stock)
            price = stock.info["regularMarketPrice"]

            speak(f'price of {search_term} is {price} {stock.info["currency"]} {person_obj.name}')
        except:
            speak('oops, something went wrong')
    if there_exists(["exit", "quit", "goodbye"]):
        speak("going offline")
        exit()


time.sleep(1)
speak('How can I help you?')

person_obj = person()
while(1):
    voice_data = record_audio() # get the voice input
    respond(voice_data) # respond


