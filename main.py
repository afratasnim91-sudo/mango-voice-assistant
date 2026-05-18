import speech_recognition as sr
import webbrowser
import pyttsx3
import time
import musicLibrary
import requests
import brain

newsapi="f95da0b1e5a741d3877bfd87244d1f4e"


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()


def processCommand(c):
    if "open google" in c.lower() or "go to google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower() or "go to facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open instagram" in c.lower() or "go to instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open linkedin"  in c.lower() or " open linkdin" in c.lower() or "go to linkedin" in c.lower() or "go to linkdin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open youtube" in c.lower() or "go to youtube" in c.lower():
        webbrowser.open("https://youtube.com")


    elif c.lower().startswith("play "):
        song = c.lower().split("play ", 1)[1].strip()
        try:
            link = musicLibrary.music[song]
            webbrowser.open(link)
        except KeyError:
            speak(f"I couldn't find {song} in your music library.")


    elif "news" in c.lower():
        response = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if response.status_code == 200:
            data = response.json()
            articles = data.get('articles', [])
            for article in articles[:5]:
                print(article['title'])
                speak(article['title'])
        else:
            speak("I'm having trouble fetching the news right now.")


    else:      
        # This handles everything else by asking the AI
        reply = brain.get_ai_response(c)
        print(f"Mango: {reply}")
        speak(reply)

if __name__=="__main__":
    speak('Initializing Mango...')
    r = sr.Recognizer()
    r.pause_threshold = 0.8 
    r.dynamic_energy_threshold = True

    with sr.Microphone() as source:
        print("Calibrating microphone for background noise...")
        r.adjust_for_ambient_noise(source, duration=1)

    print("Mango is ready!")


    while True:  
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=None, phrase_time_limit=None)
            word = r.recognize_google(audio)
            print(f"Heard: '{word}'")

            if "mango" in word.lower():
                command = word.lower().split("mango", 1)[1].strip()
                if command:
                    print(f"Processing command: '{command}'")
                    processCommand(command)

                else:
                    # If you ONLY said "mango", ask what you need
                    speak("Yes, I am listening")

                    with sr.Microphone() as source:
                        print("Mango Active (Listening for command)...")
                        audio = r.listen(source, timeout=5, phrase_time_limit=12)
                        command = r.recognize_google(audio)
                        print(f"Mango heard: '{command}'")
                        processCommand(command)

        except sr.UnknownValueError:
            # Silently pass if it just hears random room noise to avoid terminal spam
            continue
        except sr.WaitTimeoutError:
            print("Listening timed out waiting for speech.")
        except Exception as e:
            print(f"Error: {e}")
