# https://thepythoncode.com/article/using-speech-recognition-to-convert-speech-to-text-python
# https://www.makeuseof.com/python-translator-build/#:~:text=Using%20the%20Googletrans%20Python%20module,a%20few%20lines%20of%20code.
# https://www.educative.io/answers/how-do-you-translate-text-using-python 
# https://www.geeksforgeeks.org/convert-text-speech-python/
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS 
import os 


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

    translated_text = translator.translate(translated_text.text, dest='ja')
    # print(translated_text.text)

    translated_text = translator.translate(translated_text.text, src='en')
    # print(translated_text.text)
    return translated_text.text

def textToSpeech(text):
    language = 'en'
    myobj = gTTS(text=text, lang=language, slow=False) 
    # Define the output file path
    output_path = "/Users/riyakanani/Desktop/IMDM/IMDM390/LostInTranslation/SoundOutput/"
    output_file = os.path.join(output_path, "welcome.mp3")

    # Saving the converted audio in an MP3 file named "welcome.mp3" at the specified path
    myobj.save(output_file)

    # Playing the converted file
    os.system(f"mpg321 {output_file}")


def main():
    text = speechToText("sound.wav")
    translated = textTranslated(text)
    textToSpeech(translated)
    print(translated)

main()
