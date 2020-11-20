import pyttsx3
import json
import datetime
import requests
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os

speaker = pyttsx3.init()



def speak(audio):

    '''
    enables Harvey to speak
    pip install pyttsx3
    '''
    speaker.say(audio)
    speaker.runAndWait()

def wishme():
    '''
    wishes you depending upon the time
    '''
    hour = int(datetime.datetime.now().hour)
    
    if(hour>=0 and hour<12):
        speak("Good Morning!")

    elif(hour>12 and hour<18):
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("hello i am Jarvis")  
    speak("How may I help You")


def weather(lat,lng):
    '''
    finds weather at you current location 
    code reference from gfg
    '''

    api_key = "aa9bd4341bb147f4265f73c509b69226"
  
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
  
   
    complete_url = base_url + "lat="+f"{lat}"+"&lon="+f"{lng}"+"&appid="+ api_key +"&units=metric"
    response = requests.get(complete_url)
    x = response.json()     
    if x["cod"] != "404":     
        y = x["main"]     
        current_temperature = y["temp"]     
        current_pressure = y["pressure"]     
        current_humidiy = y["humidity"]        
        z = x["weather"]     
        weather_description = z[0]["description"]     
        data = (" Temperature (in celcius unit) is " +
                        str(current_temperature) + 
            "\n atmospheric pressure (in hPa unit) is " +
                        str(current_pressure) +
            "\n humidity (in percentage) is " +
                        str(current_humidiy) +
            "\n description = " +
                        str(weather_description)) 
        speak(data)
        
    
    else:
        
        speak(" City Not Found ")
        
def location():
    '''
    finds latitude and longitude of your current location
    pip install geocoder
    '''
    import geocoder 

    x = geocoder.ip("me")
    weather(x.lat,x.lng)
    
def takeCommand():
    '''
    takes voice input from the person through microphone and returns string output
    pip install speechRecognition
    pip install pywin32
    pipwin install pyaudio
    '''
    res = sr.Recognizer()
    with sr.Microphone() as source:
        print("speak Now...")
        res.pause_threshold = 1
        audio = res.listen(source)

    try:
        print("Recognizing....")
        query = res.recognize_google(audio,language="en-in" )
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        speak("Say that again please.....")
        return "None"
    return query

def helloHarvey():
    res = sr.Recognizer()
    with sr.Microphone() as source:
        print("speak Now...")
        res.pause_threshold = 1
        audio = res.listen(source)

    try:
        print("Recognizing....")
        query = res.recognize_google(audio,language="en-in" )
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        return "None"
    return query

def activateAssistant():
    query=""
    query = helloHarvey().lower()
    if query == "hey jarvis":  
        flag = 1
    else:
        flag = 0
    return flag 


def startAssistant():
    
    activate = activateAssistant()
    print(activate)
    if activate==1:      
        wishme()         
        while True:
            query = takeCommand().lower() #Converting user query into lower case

            # Logic for executing tasks based on query
            if 'wikipedia' in query: 
                '''pip install wikipedia'''
                #if wikipedia found in the query then this block will be executed
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2) 
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif "open youtube " in query:
                webbrowser.open("youtube.com")

            elif "open spotify" in query:
                CodePath = "C:\\Users\\hello\\AppData\\Roaming\\Spotify\\Spotify.exe"
                os.startfile(CodePath)

            elif 'open google' in query:
                webbrowser.open("google.com")

            elif "open vs code" in query:
                CodePath = "c:\\user\\hello\\appdata\\local\\programs\\microsoft vs code\\code.exe"
                os.startfile(CodePath)

            elif "open illustrator" in query:
                CodePath = "C:\\Program Files\\Adobe\\Adobe Illustrator CC 2019\\Support Files\\Contents\\Windows\\Illustrator.exe"
                os.startfile(CodePath)

            elif "what's the weather today" in query:
                location()

            elif "open udemy" in query:
                webbrowser.open("https://www.udemy.com/course/machinelearning/learn/lecture/6760378#overview")
            elif "ok bye" in query:
                startAssistant()

    else:
       startAssistant()



if __name__ == "__main__": 
        startAssistant()
   