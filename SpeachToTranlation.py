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
from word2number import w2n
import random
import re



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
  LANGUAGES = {
  'af': 'afrikaans',
  'sq': 'albanian',
  'am': 'amharic',
  'ar': 'arabic',
  'hy': 'armenian',
  'az': 'azerbaijani',
  'eu': 'basque',
  'be': 'belarusian',
  'bn': 'bengali',
  'bs': 'bosnian',
  'bg': 'bulgarian',
  'ca': 'catalan',
  'ceb': 'cebuano',
  'ny': 'chichewa',
  'zh-cn': 'chinese (simplified)',
  'zh-tw': 'chinese (traditional)',
  'co': 'corsican',
  'hr': 'croatian',
  'cs': 'czech',
  'da': 'danish',
  'nl': 'dutch',
  'en': 'english',
  'eo': 'esperanto',
  'et': 'estonian',
  'tl': 'filipino',
  'fi': 'finnish',
  'fr': 'french',
  'fy': 'frisian',
  'gl': 'galician',
  'ka': 'georgian',
  'de': 'german',
  'el': 'greek',
  'gu': 'gujarati',
  'ht': 'haitian creole',
  'ha': 'hausa',
  'haw': 'hawaiian',
  'iw': 'hebrew',
  'he': 'hebrew',
  'hi': 'hindi',
  'hmn': 'hmong',
  'hu': 'hungarian',
  'is': 'icelandic',
  'ig': 'igbo',
  'id': 'indonesian',
  'ga': 'irish',
  'it': 'italian',
  'ja': 'japanese',
  'jw': 'javanese',
  'kn': 'kannada',
  'kk': 'kazakh',
  'km': 'khmer',
  'ko': 'korean',
  'ku': 'kurdish (kurmanji)',
  'ky': 'kyrgyz',
  'lo': 'lao',
  'la': 'latin',
  'lv': 'latvian',
  'lt': 'lithuanian',
  'lb': 'luxembourgish',
  'mk': 'macedonian',
  'mg': 'malagasy',
  'ms': 'malay',
  'ml': 'malayalam',
  'mt': 'maltese',
  'mi': 'maori',
  'mr': 'marathi',
  'mn': 'mongolian',
  'my': 'myanmar (burmese)',
  'ne': 'nepali',
  'no': 'norwegian',
  'or': 'odia',
  'ps': 'pashto',
  'fa': 'persian',
  'pl': 'polish',
  'pt': 'portuguese',
  'pa': 'punjabi',
  'ro': 'romanian',
  'ru': 'russian',
  'sm': 'samoan',
  'gd': 'scots gaelic',
  'sr': 'serbian',
  'st': 'sesotho',
  'sn': 'shona',
  'sd': 'sindhi',
  'si': 'sinhala',
  'sk': 'slovak',
  'sl': 'slovenian',
  'so': 'somali',
  'es': 'spanish',
  'su': 'sundanese',
  'sw': 'swahili',
  'sv': 'swedish',
  'tg': 'tajik',
  'ta': 'tamil',
  'te': 'telugu',
  'th': 'thai',
  'tr': 'turkish',
  'uk': 'ukrainian',
  'ur': 'urdu',
  'ug': 'uyghur',
  'uz': 'uzbek',
  'vi': 'vietnamese',
  'cy': 'welsh',
  'xh': 'xhosa',
  'yi': 'yiddish',
  'yo': 'yoruba',
  'zu': 'zulu'}

  textWords = text.split()
  if textWords < 3:
      return "".join(textWords)
  translatedWords = int(len(textWords) / 3)
  newSentence = ""
  for i in range(translatedWords - 1):
      random_number = random.randint(0, len(textWords)  - 1)
      textWords[random_number] = (translator.translate(textWords[random_number], dest = random.choice(list(LANGUAGES.keys())))).text
 
  newSentence = "".join(textWords)
  return newSentence


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
cantHearResponce = False
firstIteration = True
def getDirections():
   # print("function called")
   output_path = "./SoundOutput/"
   global iteration
   global cantHearResponce
   global firstIteration
   firstIteration = True


   while True:
       try:
           if(cantHearResponce == False):
               playsound(output_path +  "question.mp3")
               directions = speechToText(5)


           playsound(output_path +  "didYouSay.mp3")
           gc.collect()
           if (firstIteration):
               directions = textTranslated(directions)
           firstIteration = False
           textToSpeech(directions, "confirm" + str(iteration) + ".mp3")


           iteration = iteration + 1
           cantHearResponce = True
           response = speechToText(2)
           cantHearResponce = False


           #if you say no, it will cause an infinite loop!!!!!!
           if(("yeah" in response or "yes" in response or "sure" in response)):
               gc.collect()
               return directions.lower()
          
           playsound(output_path + "apology.mp3")
           gc.collect()


       except Exception as e:
           print(e)
           if(cantHearResponce == False):
               playsound(output_path + "extraOne.mp3")
           gc.collect()

def main():
    output_path = "./SoundOutput/"
    location = "Serenity Circle"

    textToSpeech("Help! Help! I don’t know who's on the line but my car broke down and I’m lost. I'm on Serenity Circle next to Kettle Academy."
     + "I don’t know what to do. I need to find a way out of here to get home. What’s your name?", "one.mp3")

    while True:
        try:
            name = speechToText(3)
            if name:  # If name is not empty, break the loop
                break
        except:
            # give them a chance to try again
            playsound(output_path + "extraOne.mp3")


    textToSpeech("Is this a human? Please verify. What is your shoe size?", "VerifyQuestion.mp3")

    while True:
        try:
            answers = speechToText(3)
            if answers:  # If name is not empty, break the loop
                textToSpeech("Verified!", "Verified.mp3")
                break
        except:
            # textToSpeech("Sorry, I couldn\'t hear you can you repeat that","extraOne.mp3");
            playsound(output_path + "extraOne.mp3")
    
    textToSpeech("Thank you for helping me " + name + "! There’s no one around, and it’s starting to get dark. I live on Evergreen Grove."
                 + "How do I get there? Again, I'm on Serenity Circle, with Kettle Academy on my right.", "two.mp3")
    
    
    for i in range(2):
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
            elif any(i in directions for i in ["clovered", "clover"]):
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
        if i == 1:
            textToSpeech("Im running out of energy! I'm still at " + location + ", which I think is still very far from home. I’m gonna need to use taxi to get back. Do you happen to have a phonebook? Can you tell me the number to call a cab?", "directions" + str(i + 1) + ".mp3")
            break
    textToSpeech("Im running out of energy! I'm still at " + location + ", which I think is still very far from home. I’m gonna need to use taxi to get back. Do you happen to have a phonebook? Can you telll me the number to call a cab?", file_name)


    # TAXI THING
    global taxi
    while True:
        try:
            taxi = speechToText(6) #reduce the time
            taxiWords = taxi.split()
            taxiWords = np.random.shuffle(taxiWords)
            taxi = ""
            for i in range(len(taxiWords)):
                try:
                    w2n.word_to_num(taxiWords[i])
                    taxi = taxi + taxiWords[i] + " "
                except:
                    print("not a number: " + taxiWords[i])
            if(len(taxiWords) > 0):
                break
        except:
            playsound(output_path + "findNumberQuestion.mp3")
            print("no number")

    # while True:
    #     try:
    #         response = speechToText(3)
    #         if(response and ("No" in response or "no" in response)):
    #             print("debugger2")
    #             textToSpeech("okay let me know when you find it.", "six.mp3")
    #         if(response and ("yes" in response or "Yes" in response or "yeah" in response)):
    #             textToSpeech("okay let me know.", "six.mp3")
    #             try:
    #                 taxi = speechToText(6) #reduce the time
    #                 taxiWords = taxi.split()
    #                 if("four" == taxiWords[0] or "five"  == taxiWords[1] or  "three"  == taxiWords[2] or "seven" == taxiWords[3]):
    #                     break
    #             except:
    #                 textToSpeech("Can you say it again? ", "CanYouSayItAgain.mp3")
    #                 break
    #         else:
    #             try:
    #                 taxi = speechToText(6) #reduce the time
    #                 taxiWords = taxi.split()
    #                 if("four" == taxiWords[0] or "five"  == taxiWords[1] or  "three"  == taxiWords[2] or "seven" == taxiWords[3]):
    #                     break
    #             except:
    #                 textToSpeech("Can you say it again? ", "CanYouSayItAgain.mp3")
                            
    #             break
    #         gc.collect()
    #     except Exception as e:
    #         print("Error:", e)
    #         playsound(output_path + "extraOne.mp3")
    #         gc.collect()
    #         print("debugger3")

       
    textToSpeech("Can you please repeat the number? I think I heard " +
                taxi + ", but then you cut out. I can’t understand you!", "six.mp3")
    
    while True:
        try:
            taxi = speechToText(6) #reduce the time
            taxiWords = taxi.split()
            taxi = ""
            for i in range(len(taxiWords)):
                try:
                    w2n.word_to_num(taxiWords[i])
                    taxi = taxi + taxiWords[i] + " "
                except:
                    print("not a number: " + taxiWords[i])
            if (len(taxiWords) > 0):
                break
        except:
            playsound(output_path + "findNumberQuestion.mp3")
            print("no number")



    textToSpeech("Got it! Thanks " + name + ", I’ll call now. ", "calling.mp3")
    textToSpeech("         They're on the way! will you wait on the line with me?", "seven.mp3")
    try:
        confirmation = speechToText(2)
    except:
        confirmation = "default"

    if "yes" in confirmation:
        textToSpeech("Thank you. Knowing someone is listening is helpful. When I was little, my parents would tell me memories in the rain to comfort me.", "eight.mp3")
    else: 
        textToSpeech("Please, I would really appreciate it! Knowing someone is listening is helpful. When I was little, my parents would tell me memories in the rain to comfort me", "eight.mp3")
    # uses past participant's memory
    
    oldMem = ""
    with open(output_path + "output.txt", "r") as text_file:
        oldMem = text_file.read()
        text_file.close()
    textToSpeech(oldMem, "memory.mp3")

    # textToSpeech("   Share one of your own memories in the rain! I'd be happy to learn, it'll remind me of home.", "nine.mp3")
    playsound(output_path + "nine.mp3")
    try:
        memory = speechToText(5)
        
        with open(output_path + "output.txt", "w") as text_file:
            text_file.write(memory)
            text_file.close()

    except:
        pass


    # textToSpeech("Thank you for sharing " + name + ", that was very comforting. Okay, I’m starting to see headlights! I’m not sure if it’s for me… Should I get in?", "ten.mp3")

    # try:
    #     savior = speechToText(5)
    # except:
    #     savior = "yes"
    # if "yes" in savior:
    #     textToSpeech("Okay, I'm getting in. Whatever happens, please preserve my memory by writing it on the wall of the phonebooth. Thanks for your help.", "eleven.mp3")
    # else:
    #     textToSpeech("Okay, I'll wait. If the connection disconnects, please preserve my memory by writing it on the wall of the phonebooth. Thanks for your help.", "eleven.mp3")

    # # play dial tone idk

    print("done!")
main()
