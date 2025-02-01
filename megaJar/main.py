import speech_recognition as sr
import webbrowser  # For opening web pages
import pyttsx3  # For converting text to speech

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

def runCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")

# Main program execution starts here
if __name__ == "__main__":
    speak("Yes boss, I'm listening...")  # Speak an initial greeting

    while True:  # Infinite loop to continuously listen
        r = sr.Recognizer()  # Create a new recognizer instance
        with sr.Microphone() as source:  # Use the microphone as the audio source
            print("Listening...")
            try:
                audio = r.listen(source)  # Capture the audio
                print("Recognizing...")
                # Recognize speech using Google's Web Speech API
                command = r.recognize_google(audio)
                print(f"You said: {command}")
                    # to stop hte program when i said stop

                if (command == "Friday"):
                    
                    audio = r.listen(source)  # Capture the audio
                    speak("Yes boss")
                    print("Friday is here")
                    
                    word = r.recognize_google(audio)
                    print("Recognizing...")
                    print(f"You said: {word}")
                    runCommand(word)

                if (command == "stop"):
                    
                    speak("Okk boss! Stoping the program")
                    print("Program stoped")
                    break

            except sr.UnknownValueError:
                print("Sorry, I could not understand the audio.")  # If speech is unclear
            except sr.RequestError as e:
                print(f"Error with the speech recognition service: {e}")  # If there's an issue with the API request
