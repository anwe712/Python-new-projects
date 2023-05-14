import pygame as sr
import pyttsx3
import datetime
import webbrowser
import os

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Define a function to speak the given text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Define a function to listen to the user's voice command
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(f"You said: {query}\n")
    except Exception as e:
        print("Sorry, please say that again...")
        return "None"
    return query.lower()

# Define the main function to run the voice assistant
def run_voice_assistant():
    speak("Hello, how can I help you today?")

    while True:
        command = listen()

        # Tell the time
        if 'time' in command:
            now = datetime.datetime.now()
            time = now.strftime("%H:%M:%S")
            speak(f"The time is {time}")

        # Tell the weather
        elif 'weather' in command:
            # You can replace this with an API call to get the actual weather data
            speak("The weather is sunny today")

        # Open a website
        elif 'open' in command:
            website = command.replace('open ', '')
            speak(f"Opening {website}")
            webbrowser.open_new_tab(f"https://www.{website}.com")

        # Play music
        elif 'play music' in command:
            music_dir = 'C:/Users/Public/Music/Sample Music' # Replace with your music directory
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        # Exit the program
        elif 'exit' in command:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    run_voice_assistant()

