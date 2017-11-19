# -*- coding: utf-8 -*-
# Run with python 3 or else get error 
import pyaudio
import speech_recognition as sr
import wave
#import errorhaddle as eh

from ctypes import *
from contextlib import contextmanager
from os import path
from subprocess import call



def speech():
	open_string  = "เปิดไฟ"
	close_string = "ปิดไฟ"

	FORMAT = pyaudio.paInt16
	CHANNELS = 2
	RATE = 44100
	CHUNK = 1024
	RECORD_SECONDS = 5
	WAVE_OUTPUT_FILENAME = "output.wav"
	#with eh.noalsaerr():
	audio = pyaudio.PyAudio()

	# start Recording
	stream = audio.open(format=FORMAT, channels=CHANNELS,
		        rate=RATE, input=True,
		        frames_per_buffer=CHUNK)
	print("recording...")
	frames = []

	for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
		data = stream.read(CHUNK)
		frames.append(data)
	print ("finished recording")


	# stop Recording
	stream.stop_stream()
	stream.close()
	audio.terminate()

	waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
	waveFile.setnchannels(CHANNELS)
	waveFile.setsampwidth(audio.get_sample_size(FORMAT))
	waveFile.setframerate(RATE)
	waveFile.writeframes(b''.join(frames))
	waveFile.close()

	AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "output.wav")
	r = sr.Recognizer()
	with sr.AudioFile(AUDIO_FILE) as source:
		audio = r.record(source)  # read the entire audio file

	# recognize speech using Google Speech Recognition
	try:
		# for testing purposes, we're just using the default API key
		# to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH$
		# instead of `r.recognize_google(audio)`

		speech_out = r.recognize_google(audio,language = "th-TH")
		print("Word  : " + speech_out)
		if open_string in speech_out:
		    print("Open Plug")
		    call(["node","plug_api-open.js"])
		elif close_string in speech_out:
		    print("Close Plug")
		    call(["node","plug_api-close.js"])
	except sr.UnknownValueError:
		print("Google Speech Recognition could not understand audio")

if __name__ == "__main__":
	speech()

