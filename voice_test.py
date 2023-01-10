import speech_recognition as sr
recognizer = sr.Recognizer()
print(sr.Microphone.list_microphone_names())

while True:
    with sr.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic, duration=0.3)
        audio = recognizer.listen(mic)

        text = recognizer.recognize_google(audio, language="ar", show_all=True)
        if text:
            print(text['alternative'][0]['transcript'])
