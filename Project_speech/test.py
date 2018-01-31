from gtts import gTTS
import os


text_say = "shoppingกับเมียตอน 21:30"
tts = gTTS(text_say, lang = 'th')
tts.save("speak.mp3")
os.system("mpg321 speak.mp3")
