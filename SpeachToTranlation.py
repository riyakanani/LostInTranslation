# https://thepythoncode.com/article/using-speech-recognition-to-convert-speech-to-text-python
# https://www.makeuseof.com/python-translator-build/#:~:text=Using%20the%20Googletrans%20Python%20module,a%20few%20lines%20of%20code.
# https://www.educative.io/answers/how-do-you-translate-text-using-python 
# https://www.geeksforgeeks.org/convert-text-speech-python/

#add more interaction that is visible to the user.
#changes
import pyaudio
import librosa
import soundfile as sf
import time as tm # Import the time module




#changes

#add more interaction that is visible to the user. 
import speech_recognition as sr

from googletrans import Translator
from gtts import gTTS 
import os
from playsound import playsound
import gc
import numpy as np


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

#changes
# Distortion function
# def slow_down(data, factor=1):
#     return np.repeat(data, factor)


# def callback(in_data, frame_count, time_info, status):
#     data = np.frombuffer(in_data, dtype=np.float32)
    
#     processed_data = data.copy()
#     processed_data = slow_down(processed_data, factor=2)  
    
#     return processed_data.tobytes(), pyaudio.paContinue


# def speechToText(time):
#     r = sr.Recognizer()
#     #changes
#     p = pyaudio.PyAudio()


#     CHUNK = 1024
#     FORMAT = pyaudio.paFloat32
#     CHANNELS = 1
#     RATE = 44100

#     stream = p.open(format=FORMAT,
#                     channels=CHANNELS,
#                     rate=RATE,
#                     input=True,
#                     output=True,
#                     frames_per_buffer=CHUNK,
#                     stream_callback=callback)
    
#     stream.start_stream()
#     start_time = tm.time()
#     while stream.is_active() and tm.time() - start_time < time:
#         pass


#     stream.stop_stream()
#     stream.close()
#     p.terminate()

    
#     # processed_audio = slow_down(audio_data, factor=2)


#     with sr.Microphone() as source:
#         # read the audio data from the default microphone
#         audio_data = r.record(source, duration=time)
#         # print("Recognizing...")
#         # convert speech to text
#         text = r.recognize_google(audio_data)
#         print(text)
#         return text



def textTranslated(text):
    translator = Translator()

    # translated_text = translator.translate(text)
    translated_text = translator.translate(text, dest='ja')
    print(translated_text.text)
    translated_text = translator.translate(translated_text.text, src='la')
    print(translated_text.text)
    translated_text = translator.translate(translated_text.text)
    print(translated_text.text)
    return translated_text.text

def textToSpeech(text, filename, play=True):
    language = 'en'
    myobj = gTTS(text=text, lang=language, slow=False) 
    # Define the output file path
    output_path = "./SoundOutput/"
    output_file = os.path.join(output_path, filename)

    # Saving the converted audio in an MP3 file named "welcome.mp3" at the specified path
    myobj.save(output_file)

    # Playing audio
    if play:
        playsound(output_file)
    gc.collect()


# OTHER IDEAS FOR OPTIMIZATION
# ~ add distortion!!! connect to fiza script somehow idk
# ~ update try catch to catch specific error
# ~ put script lines into array?
# ~ change hard coded time values?? idk how that'd work w phonebook tho
# ~ add more interactivity! tbh not hard at all

def main():
    output_path = "./SoundOutput/"
    #add placeholder text
    textToSpeech("Help! Help! I don’t know who's on the line right now but my car broke down and I’m lost in _. I don’t know what to do. I think I need to find a way out of here to get home. Who is this? What’s your name?", "one.mp3")
    # name = speechToText(3)
    while True:
        try:
            name = speechToText(3)
            if name:  # If name is not empty, break the loop
                break
        except:
            # give them a chance to try again
            # textToSpeech("Sorry, I couldn\'t hear you can you repeat that","extraOne.mp3");
            playsound(output_path + "extraOne.mp3")

    textToSpeech("Thanks so much for your help " + name + "! There’s no one around, and it’s starting to get dark. How do I get to _? Can you please tell me the directions?", "two.mp3")
    
    responce = "No"
    while True:
        try:
            directions = speechToText(5)
            directions = textTranslated(directions)

            playsound(output_path +  "didYouSay.mp3")
            gc.collect()
            textToSpeech(directions, "directions.mp3")

            responce = speechToText(2)
            print("debugger1")
            #if you say no, it will cause an infinite loop
            if(("yeah" in responce or "yes" in responce)):
                print("debugger2")
                break
            playsound(output_path + "repeat2.mp3")
            gc.collect()

        except Exception as e:
            print("Error:", e)
            playsound(output_path + "extraOne.mp3")
            gc.collect()
            print("debugger3")



    if "left" in directions:
        textToSpeech("Okay, I’m taking a left towards _. This doesn’t seem right… I’m heading the other direction instead. I'm walking past a large tree. Which colored path should I take?", "three.mp3")
    elif "right" in directions: 
        textToSpeech("So I’m taking a right near _, but it is all blocked off by police cars and cones. There is no way for me to get around! Is there another path that I could take?", "three.mp3")
    else:
        textToSpeech("I couldn’t quite hear you! So I’m taking a right near _, but it is all blocked off by police cars and cones. There is no way for me to get around! Is there another path that I could take?", "three.mp3")
    try:
        directionsAgain = speechToText(5)
    except:
        directionsAgain = "change default directions here later" # update

    textToSpeech("I’m still lost " + name + ", and I’m starting to lose connection. Did you say " + 
                 textTranslated(directionsAgain) +
                 "? Please help me!", "four.mp3")
    
    # add the text to respond
    responce = "No"
    while True:
        try:
            responce = speechToText(3)
            if(("yeah" in responce or "yes" in responce) and responce):
                print("debugger2")
                break
            playsound(output_path + "repeat2.mp3")
            gc.collect()
        except Exception as e:
            print("Error:", e)
            playsound(output_path + "extraOne.mp3")
            gc.collect()
            print("debugger3")

    textToSpeech("Okay, I think I got it now. I am now at _, but I think I’m gonna need a taxi to get all the way back home. Do you happen to have a phonebook? Do you know what the number to call a cab is? Hurry " +
                name + ", it’s already dark out here.", "five.mp3")
    

    #taxi number
    try:
        taxi = speechToText(6) #reduce the time
        taxiWords = taxi.split()
        np.random.shuffle(taxiWords)
        taxi = ""
        for i in range(5):
            taxi = taxi + taxiWords[i] + " "
    except:
        textToSpeech("Were you able to find the number?: ")


    while True:
        try:
            responce = speechToText(3)
            if(responce and ("No" in responce or "no" in responce)):
                print("debugger2")
                textToSpeech("okay let me know when you find it.", "six.mp3")
            if(responce and ("yes" in responce or "Yes" in responce or "yeah" in responce)):
                textToSpeech("okay let me know.", "six.mp3")
                try:
                    taxi = speechToText(6) #reduce the time
                    taxiWords = taxi.split()
                    if("four" == taxiWords[0] or "five"  == taxiWords[1] or  "three"  == taxiWords[2] or "seven" == taxiWords[3]):
                        break
                except:
                    textToSpeech("Can you say it again?: ")
                    break
            else:
                try:
                    taxi = speechToText(6) #reduce the time
                    taxiWords = taxi.split()
                    if("four" == taxiWords[0] or "five"  == taxiWords[1] or  "three"  == taxiWords[2] or "seven" == taxiWords[3]):
                        break
                except:
                    textToSpeech("Can you say it again?: ")
                            
                break
            gc.collect()
        except Exception as e:
            print("Error:", e)
            playsound(output_path + "extraOne.mp3")
            gc.collect()
            print("debugger3")

       
    textToSpeech("Can you please repeat the number? I think I heard " +
                taxi + ", but then you cut out. I can’t understand you!", "six.mp3")
    
    try:
        taxi = speechToText(6) #reduce the time
        taxiWords = taxi.split()
        np.random.shuffle(taxiWords)
        taxi = ""
        for i in range(5):
            taxi = taxi + taxiWords[i] + " "
    except:
        print("no number")



    textToSpeech("Got it! Thanks " + name + ", I’ll call now, be right back… Awesome, someone’s on their way to pick me up now! Is it okay if I stay on the line with you while I wait?", "seven.mp3")
    try:
        confirmation = speechToText(2)
    except:
        confirmation = "default"

    if "yes" in confirmation:
        textToSpeech("Thank you, I really appreciate it! Just knowing someone is listening is comforting to me. When I was a little kid and scared, my mom would always tell me to try to relive a happy memory.", "eight.mp3")
    else: 
        textToSpeech("Please, I would really appreciate it! Just knowing someone is listening is comforting to me. When I was a little kid and scared, my mom would always tell me to try to relive a happy memory.", "eight.mp3")
    # uses past participant's memory
    playsound("./SoundOutput/memory.mp3")
    # comment below out once generated once!!!!!!
    # textToSpeech("insert default memory here", "memory.mp3") # update

    #this is one of many memories that I have:
    textToSpeech("Share one of your own! I'd be happy to hear about anything, it'll remind me of home.", "nine.mp3")
    # playsound(output_path + "nine.mp3")
    try:
        memory = speechToText(30)
        memory = textTranslated(memory)
        memoryWords = taxi.split(".")
        np.random.shuffle(memoryWords)
        memory = ""
        for i in range(5):
            memory = memory + memoryWords[i] + " "
        textToSpeech(memory, "memory.mp3", False)
    except:
        pass

    # probably split below up to add pause + sound effect
    textToSpeech("Thank you for sharing " + name + ", that was very comforting. Okay, I’m starting to see a car pull up! I’m not sure if it’s the one for me or not… Do you think I should get in? This might be my only chance to get home.", "ten.mp3")
    # play dial tone idk
    try:
        savior = speechToText(5)
    except:
        savior = "yes"
    if "yes" in savior:
        textToSpeech("Okay, I'll just get in. I really want to just go home. Whatever happens to me, please preserve my memory by writing it on the wall of the phonebooth. Thanks for your help.", "eleven.mp3")
    else:
        textToSpeech("Okay, I'll wait for another car until I'm sure. If the connection disconnects, please preserve my memory by writing it on the wall of the phonebooth. Thanks for your help.", "eleven.mp3")


    print("done!")
main()
