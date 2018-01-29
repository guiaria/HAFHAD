from pythainlp.tag import pos_tag
from pythainlp.corpus import stopwords
from pythainlp.tokenize import word_tokenize
import speech_recognition as sr
import json
import csv
from Open_Close import open_close



def conversation():
    
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # recognize speech using Google Speech Recognition
    try:
         print("Google Speech Recognition thinks you said " + r.recognize_google(audio, language ="th-TH"))
         text = r.recognize_google(audio, language ="th-TH")
         if any(['ปิดไฟ' in text, 'ปิดปลั๊ก' in text, 'เปิดไฟ' in text, 'เปิดปลั๊ก' in text]):
             open_close(text)

	 		 

	
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


	
    

if __name__ == "__main__":
    conversation()
    print("Analyzing Conversation")
