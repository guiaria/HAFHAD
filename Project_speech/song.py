from __future__ import unicode_literals
import youtube_dl
import vlc
import urllib
import urllib.request as urllib2
import urllib.parse
from bs4 import BeautifulSoup
from pythainlp.tokenize import word_tokenize 
from tts import tts
from stt import stt




inte = False





def getLink(search): 
    query = urllib.parse.quote(search)
    url = "https://www.youtube.com/results?search_query=" + query
    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html,"html5lib")
    find = soup.findAll(attrs={'class':'yt-uix-tile-link'})
    detail = find[0]
    link = 'https://www.youtube.com'+detail['href']
    return link

def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')



def getSong(link):
    
    ydl_opts = {
            'format': 'worstaudio/worst',    
            'extractaudio': True,
            'outtmpl': 'song/%(title)s',        
            'noplaylist' : True,        
            'progress_hooks': [my_hook],
            'prefer_ffmpeg': True
            }

    r = None
    try:
        tts("กําลังหาเพลงค่ะ")
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
            r = ydl.extract_info(link,download=False)
            
            
        return r['title']
    except Exception as e:
        tts("มีปัญหาโหลดเพลงค่ะ")
        
        return 0
            
    



def playSong(song):
    try:
        p = vlc.MediaPlayer("song/"+song)
        p.play()
        return 1
    except Exception as e:
        tts("มีปัญหาเล่นเพลงค่ะ")
        return 0
        
        
        
    
    
    
def song(text):   
    e=word_tokenize(text,engine='newmm')
    if(e[0] == 'เล่น' or e[0] == 'เปิด'):
        if(e[1] == 'เพลง' and e[1] != e[-1]):
            print(e)
            e.pop(0)
            e.pop(0)
            search = ''.join(e)
            print("Song to Search: %s"%search)
            link = getLink(search)
            
            song = getSong(link)
            if(song == 0):
                return 0
            
            player = playSong(song)
            if(player == 0):
                return 0
            else:
                return player
            
        elif(e[1] == 'เพลง' and e[1] == e[-1]):
            tts("กรุณาระบุชื่อเพลงด้วยค่ะ")
            search = stt()
            print("Song to Search: %s"%search)
            link = getLink(search)
            
            song = getSong(link)
            if(song == 0):
                return 0
            
            player = playSong(song)
            if(player == 0):
                return 0
            else:
                return player
            
            return 0
        else:
            tts("ไม่เข้าใจคำสั่งของคุณค่ะ")
            return 0
            
    else:
        return 0
            
    
    

