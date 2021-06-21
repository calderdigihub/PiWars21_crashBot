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
	except:
		print("Sorry, I did not get that")
		code="blank"
	if code == "forward long":
		directions.forward()
		sleep(10)
		directions.stop()
	elif code == "forward middle":
		directions.forward()
		sleep(5)
		directions.stop()
	elif code == "forward short":
		directions.forward()
		sleep(1)
		directions.stop()
	elif code == "reverse long":
		directions.back()
		sleep(10)
		directions.stop()
	elif code == "reverse middle":
		directions.back()
		sleep(5)
		directions.stop()
	elif code == "reverse short":
		directions.back()
		sleep(1)
		directions.stop()
	elif code == "right long":
		directions.left_forward()
		sleep(10)
		directions.stop()
	elif code == "right middle":
		directions.left_forward()
		sleep(5)
		directions.stop()
	elif code == "right short":
		directions.left_forward()
		sleep(1)
		directions.stop()
	elif code == "left long":
		directions.right_forward()
		sleep(10)
		directions.stop()
	elif code == "left middle":
		directions.right_forward()
		sleep(5)
		directions.stop()
	elif code == "left short":
		directions.right_forward()
		sleep(1)
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
		except:
			print("Sorry, I did not get that")
			code="blank"
		if code == "forward long":
			directions.forward()
			sleep(10)
			directions.stop()
		elif code == "forward middle":
			directions.forward()
			sleep(5)
		directions.stop()
		elif code == "forward short":
			directions.forward()
			sleep(1)
			directions.stop()
		elif code == "reverse long":
			directions.back()
			sleep(10)
			directions.stop()
		elif code == "reverse middle":
			directions.back()
			sleep(5)
			directions.stop()
		elif code == "reverse short":
			directions.back()
			sleep(1)
			directions.stop()
		elif code == "right long":
			directions.left_forward()
			sleep(10)
			directions.stop()
		elif code == "right middle":
			directions.left_forward()
			sleep(5)
			directions.stop()
		elif code == "right short":
			directions.left_forward()
			sleep(1)
			directions.stop()
		elif code == "left long":
			directions.right_forward()
			sleep(10)
			directions.stop()
		elif code == "left middle":
			directions.right_forward()
			sleep(5)
			directions.stop()
		elif code == "left short":
			directions.right_forward()
			sleep(1)
			directions.stop()

