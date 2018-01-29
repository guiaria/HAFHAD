# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from pythainlp.tag import pos_tag
from pythainlp.corpus import stopwords


from pythainlp.tokenize import word_tokenize


text='เปิดไฟในห้องนอนให้หน่อย'
e=word_tokenize(text,engine='newmm') 

if any(['ปิดไฟ' in text, 'ปิดปลั๊ก' in text, 'เปิดไฟ' in text, 'เปิดปลั๊ก' in text]):
    print(1)
    

     





#e = ''.join(e)
print(e)
open_light = []
close_light = []
stopwords = stopwords.words('thai')
stopwords1 = ['สิ','ดิ','หน่อย']

filter_word1 = e
for word in e:
    if any(["เปิด" in word,"ปิด" in word]):
        continue
    if word in stopwords:
        filter_word1.remove(word)
        
filter_word = [word1 for word1 in filter_word1 if word1 not in stopwords1]
pos_list = pos_tag(filter_word,engine='artagger')
print(pos_list)

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



    

print(open_light)
print(close_light)
