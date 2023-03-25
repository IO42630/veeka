import subprocess
import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    while True:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            text = text.lower()
            print("> ", text)
            subprocess.run(["bash", "-c", text])
        except sr.UnknownValueError:
            print("...")
        except sr.RequestError as e:
            print(".......", e)
