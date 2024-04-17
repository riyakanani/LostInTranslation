# https://thepythoncode.com/article/using-speech-recognition-to-convert-speech-to-text-python
# https://www.makeuseof.com/python-translator-build/#:~:text=Using%20the%20Googletrans%20Python%20module,a%20few%20lines%20of%20code.
# https://www.educative.io/answers/how-do-you-translate-text-using-python 
# https://www.geeksforgeeks.org/convert-text-speech-python/
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS 
import os
from playsound import playsound
# def speechToText(audioName):
#     r = sr.Recognizer()   #Speech recognition
#     audio = sr.AudioFile(audioName)
#     with audio as source:
#         print("Wait. Program Starting")
#         audio = r.record(source)
#         message = r.recognize_google(audio)
#         # message = r.recognize_google(audio, language="es-ES")
#     return message

# microphone
def speechToText(time) :
    r = sr.Recognizer()

    with sr.Microphone() as source:
        # read the audio data from the default microphone
        audio_data = r.record(source, duration=time)
        # print("Recognizing...")
        # convert speech to text
        text = r.recognize_google(audio_data)
        print(text)
        return text

def textTranslated(text): # can mess around w this!
    translator = Translator()

    text = translator.translate(text, dest='es')
    text = translator.translate(text, dest='en')

    return text

def textToSpeech(text, filename):
    language = 'en'
    myobj = gTTS(text=text, lang=language, slow=False) 
    # Define the output file path
    output_path = "/Users/malay/Desktop/litgit/LostInTranslation/SoundOutput/"
    output_file = os.path.join(output_path, filename)

    # Saving the converted audio in an MP3 file named "welcome.mp3" at the specified path
    myobj.save(output_file)

    # Playing audio
    playsound(output_file)

# put script in array for conciseness ?
def main():
    textToSpeech("Help! Help! Is this 911? I don’t know who's on the line right now but my car broke down and I’m lost in _. I don’t know what to do. I think I need to find a way out of here to get home. Who is this? What’s your name?", "one.mp3")
    name = speechToText(2)

    textToSpeech("Thanks so much for your help " + name + "! There’s no one around, and it’s starting to get dark. How do I get to _? Can you please tell me the directions?", "two.mp3")
    directions = speechToText(5)

    if "left" in directions:
        textToSpeech("Okay, I’m taking a left towards _. This doesn’t seem right… I’m heading the other direction instead.", "three.mp3")
    elif "right" in directions: 
        textToSpeech("So I’m taking a right near _, but it is all blocked off by police cars and cones. There is no way for me to get around! Is there another path that I could take?", "three.mp3")
    else:
        textToSpeech("I couldn’t quite hear you! So I’m taking a right near _, but it is all blocked off by police cars and cones. There is no way for me to get around! Is there another path that I could take?", "three.mp3")
    directionsAgain = speechToText(5)

    textToSpeech("I’m still lost " + name + ", and I’m starting to lose connection. Did you say " + 
                 textTranslated(directionsAgain) +
                 "? Please help me!", "four.mp3")

    print("done!")

main()
