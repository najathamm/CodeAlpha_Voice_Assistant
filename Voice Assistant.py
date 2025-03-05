import speech_recognition as sr
import pyttsx3
import webbrowser
import os

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand that.")
        return ""
    except sr.RequestError:
        speak("Sorry, there was an issue with the speech recognition service.")
        return ""

def open_youtube():
    speak("Opening YouTube")
    webbrowser.open("https://www.youtube.com")

def open_spotify():
    speak("Opening Spotify")
    webbrowser.open("https://open.spotify.com")

def google_search(query):
    speak(f"Searching Google for {query}")
    webbrowser.open(f"https://www.google.com/search?q={query}")

def main():
    speak("Hello! How can I assist you today?")
    while True:
        command = recognize_speech()
        if "youtube" in command:
            open_youtube()
        elif "spotify" in command:
            open_spotify()
        elif "search" in command:
            query = command.replace("search", "").strip()
            google_search(query)
        elif "exit" in command or "quit" in command:
            speak("Goodbye!")
            break
        else:
            speak("I'm not sure how to do that.")

if __name__ == "__main__":
    main()
