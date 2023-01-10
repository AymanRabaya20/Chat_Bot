from datetime import datetime
import playsound
import speech_recognition as sr
from chatterbot import ChatBot
from gtts import gTTS


recognizer = sr.Recognizer()
print(sr.Microphone.list_microphone_names())
bot = ChatBot('Omar')
count = 0


def speck(text):
    date_string = datetime.now().strftime("%d%m%Y%H%M%S")
    converted_audio = gTTS(text=text, lang="ar")
    filename = "voice" + date_string + ".mp3"
    converted_audio.save(filename)
    playsound.playsound(filename)


while True:
    with sr.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic, duration=0.2)
        audio = recognizer.listen(mic)
        try:
            text = recognizer.recognize_google(audio, language="ar", show_all=True)
        except Exception as e:
            speck("انا لم افهم. اعد ما قلت")
        if text:
            print(text['alternative'][0]['transcript'])
            # Get a response to the input text 'I would like to book a flight.'
            response = bot.get_response(text['alternative'][0]['transcript'])
            print("Bot: ", response)
            speck(str(response))


