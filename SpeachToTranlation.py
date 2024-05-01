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

iteration = 0
def getDirections():
    output_path = "./SoundOutput/"
    global iteration
    while True:
        try:
            directions = speechToText(5)

            playsound(output_path +  "didYouSay.mp3")
            gc.collect()
            textToSpeech(directions, "confirm" + str(iteration) + ".mp3")
            iteration = iteration + 1

            response = speechToText(2)
            print("debugger1")

            #if you say no, it will cause an infinite loop!!!!!!
            if(("yeah" in response or "yes" in response)):
                print("debugger2")
                gc.collect()
                return directions.lower()
            playsound(output_path + "repeat2.mp3")
            gc.collect()

        except Exception as e:
            print("didn't understand")
            playsound(output_path + "extraOne.mp3")
            gc.collect()

def main():
    output_path = "./SoundOutput/"
    location = "Serenity Circle"
    iteration = 0

    # textToSpeech("Help! Help! I don’t know who's on the line right now but my car broke down and I’m lost. I'm on Serenity Circle next to a _."
    #  + "I don’t know what to do. I think I need to find a way out of here to get home. Who is this? What’s your name?", "one.mp3")

    # while True:
    #     try:
    #         name = speechToText(3)
    #         if name:  # If name is not empty, break the loop
    #             break
    #     except:
    #         # give them a chance to try again
    #         playsound(output_path + "extraOne.mp3")

    # textToSpeech("Thanks so much for your help " + name + "! There’s no one around, and it’s starting to get dark. I live on Evergreen Grove."
    #              + "How do I get there? Again, I'm on Serenity Circle, with Kettle Academy on my right. Can you please tell me the directions?", "two.mp3")
    
    
    for i in range(3): # repeats 3 times
        directions = getDirections();
        file_name = "directions" + str(i) + ".mp3"

        if location == "Serenity Circle": # willow, tranquility, echo
            if any(i in directions for i in ["tranquility", "lane", "right", "up"]):
                textToSpeech("Okay, I'm going up and right to Tranquility Lane.", file_name)
                location = "Tranquility Lane"
            elif any(i in directions for i in ["echo", "valley", "drive", "down"]):
                textToSpeech("Okay, I'm going down and left to Echo Valley Drive.", file_name)
                location = "Echo Valley Drive"
            elif any(i in directions for i in ["willow", "creek", "avenue", "left"]):
                textToSpeech("Okay, I'm going up and left to Willow Creek Avenue.", file_name)
                location = "Willow Creek Avenue"
            else:
                textToSpeech("I'm having trouble. I'm just going to go up and left to Willow Creek Avenue.", file_name)
                location = "Willow Creek Avenue"

        elif location == "Willow Creek Avenue": # ivy, hollow, serenity, tranquility
            if any(i in directions for i in ["hollow", "square"]) or (("left" in directions) and ("up" in directions)):
                textToSpeech("Okay, I'm going left and up to Hollow Square.", file_name)
                location = "Hollow Square"
            elif any(i in directions for i in ["ivy", "left"]):
                textToSpeech("Okay, I'm going left to Ivy Lane.", file_name)
                location = "Ivy Lane"
            elif any(i in directions for i in ["serenity", "circle"]) or (("right" in directions) and ("down" in directions)):
                textToSpeech("Okay, I'm right and down to Serenity Circle.", file_name)
                location = "Serenity Circle"
            elif any(i in directions for i in ["tranquility", "right"]):
                textToSpeech("Okay, I'm going right and up to Tranquility Lane.", file_name)
                location = "Tranquility Lane"
            else:
                textToSpeech("I'm having trouble. I'm just going to go up and left to Hollow Square.", file_name)
                location = "Hollow Square"
        elif location == "Tranquility Lane": # crystal, harmony, twisted, clovered, riverside, willow, serenity
            if any(i in directions for i in ["crystal", "falls", "drive", "up"]):
                textToSpeech("Okay, I'm going upwards towards Crystal Falls Drive.", file_name)
                location = "Crystal Falls Drive"
            elif any(i in directions for i in ["willow", "creek", "avenue"])or (("left" in directions) and ("down" in directions)):
                textToSpeech("Okay, I'm down and left to Willow Creek Avenue.", file_name)
                location = "Willow Creek Avenue"
            elif any(i in directions for i in ["harmony", "left"]):
                textToSpeech("Okay, I'm going up and left to Harmony Lane.", file_name)
                location = "Harmony Lane"
            elif any(i in directions for i in ["twisted", "way"]) or (("right" in directions) and ("up" in directions)):
                textToSpeech("Okay, I'm going up and right towards Twisted Way.", file_name)
                location = "Twisted Way"
            elif any(i in directions for i in ["clovered"]):
                textToSpeech("Okay, I'm going up and right towards Clovered Lane.", file_name)
                location = "Clovered Lane"
            elif any(i in directions for i in ["riverside", "bend", "river", "side", "right"]):
                textToSpeech("Okay, I'm going right to Riverside Bend.", file_name)
                location = "Riverside Bend"
            elif any(i in directions for i in ["serenity", "circle", "down"]):
                textToSpeech("Okay, I'm going down and right to Serenity Circle.", file_name)
                location = "Serenity Circle"
            else:
                textToSpeech("I'm having trouble. I'm just going to go upwards towards Crystal Falls Drive.", file_name)
                location = "Crystal Falls Drive"
        elif location == "Echo Valley Drive": # sunset, dead, serenity
            if any(i in directions for i in ["sunset", "boulevard", "left", "up"]):
                textToSpeech("Okay, I'm going left to Sunset Boulevard.", file_name)
                location = "Sunset Boulevard"
            elif any(i in directions for i in ["dead", "end", "down"]):
                textToSpeech("Okay, I'm going down. This seems to be a dead end! You're not very helpful. I'm going to go up and left to Sunset Boulevard.", file_name)
                location = "Sunset Boulevard"
            elif any(i in directions for i in ["serenity", "circle", "right"]):
                textToSpeech("Okay, I'm going right to Serenity Circle.", file_name)
                location = "Serenity Circle"
            else:
                textToSpeech("I'm having trouble. I'm just going to go up and left to Sunset Boulevard.", file_name)
                location = "Sunset Boulevard"
        # elif location == "ivy":
        # elif location == "hollow":
        # elif location == "crystal":
        # elif location == "harmony":
        # elif location == "twisted":
        # elif location == "clovered":
        # elif location == "riverside":
        # elif location == "sunset":
        # location == "dead":
        else:
            textToSpeech("I'm getting tired! I'm still at " + location + ", which I think is still very far from home. I'm just going to call a taxi instead.", file_name)
            break
        
        

    # if "left" in directions:
    #     textToSpeech("Okay, I’m taking a left towards _. This doesn’t seem right… I’m heading the other direction instead. I'm walking past a large tree. Which colored path should I take?", "three.mp3")
    # elif "right" in directions: 
    #     textToSpeech("So I’m taking a right near _, but it is all blocked off by police cars and cones. There is no way for me to get around! Is there another path that I could take?", "three.mp3")
    # else:
    #     textToSpeech("I couldn’t quite hear you! So I’m taking a right near _, but it is all blocked off by police cars and cones. There is no way for me to get around! Is there another path that I could take?", "three.mp3")
    
    # add more nav
    # try:
    #     directionsAgain = speechToText(5)
    # except:
    #     directionsAgain = "change default directions here later" # update

    # textToSpeech("I’m still lost " + name + ", and I’m starting to lose connection. Did you say " + 
    #              textTranslated(directionsAgain) +
    #              "? Please help me!", "four.mp3")
    
    # # add the text to respond
    # response = "No"
    # while True:
    #     try:
    #         response = speechToText(3)
    #         if(("yeah" in response or "yes" in response) and response):
    #             print("debugger2")
    #             break
    #         playsound(output_path + "repeat2.mp3")
    #         gc.collect()
    #     except Exception as e:
    #         print("Error:", e)
    #         playsound(output_path + "extraOne.mp3")
    #         gc.collect()
    #         print("debugger3")

    # textToSpeech("Okay, I think I got it now. I am now at _, but I think I’m gonna need a taxi to get all the way back home. Do you happen to have a phonebook? Do you know what the number to call a cab is? Hurry " +
    #             name + ", it’s already dark out here.", "five.mp3")
    

    # TAXI THING
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
            response = speechToText(3)
            if(response and ("No" in response or "no" in response)):
                print("debugger2")
                textToSpeech("okay let me know when you find it.", "six.mp3")
            if(response and ("yes" in response or "Yes" in response or "yeah" in response)):
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
