#pip3 install SpeechRecognition
#pip3 install pyaudio
#https://realpython.com/python-speech-recognition/#picking-a-python-speech-recognition-package
#https://maker.pro/raspberry-pi/tutorial/the-best-voice-recognition-software-for-raspberry-pi
import speech_recognition as sr
import directions
r=sr.Recognizer()
mic = sr.Microphone() 
with mic as source:
	r.adjust_for_ambient_noise(source)
	print("listening")
	audio_text = r.listen(source)
	print("Text: "+r.recognize_google(audio_text))
	print("not listening")
	try:
    	# using google speech recognition
		code = r.recognize_google(audio_text)
    	print("Text: "+code)
		if 
	except:
    	print("Sorry, I did not get that")
		code="blank"
	if code == "forward":
		directions.forward()
	elif code == "reverse"
		directions.back()
	elif code == "right":
		directions.right()
	elif code == "left":
		directions.left()
	elif code == "stop":
		directions.stop()

while r.recognize_google(audio_text) != "end":
	with mic as source:
		r.adjust_for_ambient_noise(source)
		print("listening")
		audio = r.listen(source)
		print("Text: "+r.recognize_google(audio_text))
		print("not listening")

	try:
    	# using google speech recognition
		code = r.recognize_google(audio_text)
    	print("Text: "+code)
		if 
	except:
    	print("Sorry, I did not get that")
		code="blank"
	if code == "forward":
		directions.forward()
	elif code == "reverse"
		directions.back()
	elif code == "right":
		directions.right()
	elif code == "left":
		directions.left()
	elif code == "stop":
		directions.stop()
