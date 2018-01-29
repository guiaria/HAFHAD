import speech_recognition as sr
from Open_Close import open_close
from checkemail import checkemail
from stt import stt
from tts import tts

def conversation():


	tts("ว่าไงคะ")
	text = stt()
	count = 0
	if any(['ปิดไฟ' in text, 'ปิดปลั๊ก' in text, 'เปิดไฟ' in text, 'เปิดปลั๊ก' in text]):
		open_close(text)
		count = 1
		
	if any(['เช็คเมล์' in text,'เช็คอีเมล' in text,'เช็ค inbox' in text,'ตรวจอีเมล' in text, 'ตรวจเมล์' in text]):
		checkemail()
		count = 1
		
	
	if count != 1:
		tts("ไม่เข้าใจคำสั่งของคุณค่ะ")


	
    


