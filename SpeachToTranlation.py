# https://thepythoncode.com/article/using-speech-recognition-to-convert-speech-to-text-python
# https://www.makeuseof.com/python-translator-build/#:~:text=Using%20the%20Googletrans%20Python%20module,a%20few%20lines%20of%20code.
import speech_recognition as sr
from googletrans import Translator


def speechToText(audioName):
    r = sr.Recognizer()   #Speech recognition
    audio = sr.AudioFile(audioName)
    with audio as source:
        print("Wait. Program Starting")
        audio = r.record(source)
        message = r.recognize_google(audio)
        # message = r.recognize_google(audio, language="es-ES")
    return message

# microphone
# def speechToText() :
#     r = sr.Recognizer()

#     with sr.Microphone() as source:
#         # read the audio data from the default microphone
#         audio_data = r.record(source, duration=5)
#         print("Recognizing...")
#         # convert speech to text
#         text = r.recognize_google(audio_data)
#         print(text)

def textTranslated(text):
    translator = Translator()

    translated_text = translator.translate(text)
    # print(translated_text.text)

    translated_text = translator.translate(translated_text, dest='ja')
    # print(translated_text.text)

    translated_text = translator.translate(translated_text, src='la')
    # print(translated_text.text)
    return translated_text

def main():
    text = speechToText("sound.wav")
    translated = textTranslated(text)
    print(translated)

main()
