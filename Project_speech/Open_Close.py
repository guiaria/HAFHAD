from pythainlp.tag import pos_tag
from pythainlp.corpus import stopwords
from pythainlp.tokenize import word_tokenize
import speech_recognition as sr
import json
import csv



def open_close(text):
    
    print(text)
    e=word_tokenize(text,engine='newmm')
    print(e)
    
    open_light = []
    close_light = []
    stopwords1 = stopwords.words('thai')
    stopwords2 = ['สิ','ดิ','หน่อย','ให้','ใน']

    filter_word1 = e
    for word in e:

        if any(['เปิด' in word, 'ปิด' in word]):
            continue
        if word in stopwords2:
            filter_word1.remove(word)

    filter_word = [word1 for word1 in filter_word1 if word1 not in stopwords2]
    pos_list = pos_tag(filter_word,engine='artagger')
    print(filter_word)


    if(filter_word[0] == "เปิดไฟ"):
        open_light.append(filter_word[1])
        if len(filter_word) > 2:
            if(filter_word[2] == "เเละ" and filter_word[-1] != "เเละ"):
                open_light.append(filter_word[3])
  

    if(filter_word[0] == "เปิด" and filter_word[1] == "ปลั๊ก"):
        open_light.append(filter_word[2])
        if len(filter_word) > 3:
            if(filter_word[3] == "เเละ" and filter_word[-1] != "เเละ"):
                open_light.append(filter_word[4])


    if(filter_word[0] == "ปิดไฟ"):
        close_light.append(filter_word[1])
        if len(filter_word) > 2:
            if(filter_word[2] == "เเละ" and filter_word[-1] != "เเละ"):
                 close_light.append(filter_word[3])
 

    if(filter_word[0] == "ปิด" and filter_word[1] == "ปลั๊ก"):
        close_light.append(filter_word[2])
        if len(filter_word) > 3:
            if(filter_word[3] == "เเละ" and filter_word[-1] != "เเละ"):
                close_light.append(filter_word[4])

if __name__ == "__main__":
    open_close()
    print("Finished open close light function")
