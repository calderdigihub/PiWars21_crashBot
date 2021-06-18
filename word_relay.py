#pip3 install SpeechRecognition
#pip3 install pyaudio
#https://realpython.com/python-speech-recognition/#picking-a-python-speech-recognition-package
import speech_recognition as sr
r=sr.Recognizer()
mic = sr.Microphone() 
while r.recognize_google(audio_text) != "end":
	with mic as source:
		r.adjust_for_ambient_noise(source)
		print("listening")
		audio = r.listen(source)
		print("Text: "+r.recognize_google(audio_text))
		print("not listening")

	try:
    	# using google speech recognition
    	print("Text: "+r.recognize_google(audio_text))
	except:
    	print("Sorry, I did not get that")
