import speech_recognition as sr
import pyttsx3
speech = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__=="__main__":
    speak("Yes sir, i'm here.")

    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            try:
                audio = r.listen(source)
                print("recognizing....")

                command = r.recognize_google(audio)

                print(f"You said {command}")

                if (command == "stop"):
                    speak("Okk sir, i'm stoping the program")
                    print("The program has stoped")
                    break

            
            except sr.UnknownValueError:
                print("Could not understand the audio")
