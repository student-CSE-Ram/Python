import speech_recognition as sr  # For recognizing spoken words
import webbrowser  # For opening web pages
import pyttsx3  # For converting text to speech
import musicLib

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to execute commands based on the recognized text
def runCommand(command):
    if "open google" in command.lower():
        speak("Opening Google")
        webbrowser.open("https://google.com")

    elif "open youtube" in command.lower():
        speak("Opening Youtube")
        webbrowser.open("https://youtube.com")

    elif command.lower().startswith("play"):
        song = command.lower().split(" ")[1]
        link = musicLib.songs[song]
        webbrowser.open(link)

    else:
        speak("Sorry, I don't recognize that command.")

# Main program execution starts here
if __name__ == "__main__":
    speak("Yes boss, I'm listening...")  # Speak an initial greeting

    while True:  # Infinite loop to continuously listen
        with sr.Microphone() as source:  # Use the microphone as the audio source
            print("Listening...")
            try:
                # Capture the audio
                audio = recognizer.listen(source)
                print("Recognizing...")
                # Recognize speech using Google's Web Speech API
                command = recognizer.recognize_google(audio)
                print(f"You said: {command}")

                # Check for the "Friday" wake word
                if command.lower() == "friday":
                    speak("Yes boss")
                    print("Friday is here. Listening for your command...")

                    # Listen for the next command after "Friday"
                    audio = recognizer.listen(source)
                    follow_up_command = recognizer.recognize_google(audio)
                    print(f"You said: {follow_up_command}")
                    runCommand(follow_up_command)

                # Stop the program when "stop" is heard
                elif command.lower() == "stop":
                    speak("Okay boss! Stopping the program.")
                    print("Program stopped")
                    break

                # Handle unrecognized commands
                else:
                    speak("I didn't catch that. Please try again.")

            except sr.UnknownValueError:
                print("Sorry, I could not understand the audio.")  # If speech is unclear
            except sr.RequestError as e:
                print(f"Error with the speech recognition service: {e}")  # If there's an issue with the API request
