import RPi.GPIO as GPIO
from evdev import InputDevice, categorize, ecodes
import sys
from time import sleep
import directions


GPIO.cleanup()



controller = InputDevice('/dev/input/event2')
angle = float(12)
claw.ChangeDutyCycle


for event in controller.read_loop():

	print(str(event.code)+" "+str(event.value))
	if event.code == 17: 
		if event.value == -1:
			directions.forward()
		elif event.value == 1:
			directions.back()
		else:
			directions.stop()
	if event.code == 16:
		if event.value == 1:
			directions.right()
		elif event.value == -1:
			directions.left()
		else:
			directions.stop()
	
	if event.code == 304:
		if event.value == 1:
			directions.f_down()
		else:
			directions.stop()
			
	if event.code == 308:
		if event.value == 1:
			directions.f_up()
		else:
			directions.stop()
			
	if event.code == 305:
		if event.value == 1:
			if angle + (10/18) <=12:
				angle = angle + (10/18)
				directions.f_angle(angle)
		else:
			directions.stop()
			
	if event.code == 307:
		if event.value == 1:
			if angle - (10/18) >=2:
				angle = angle - (10/18)
				directions.f_angle(angle)
		else:
			directions.stop()
			
	if event.code == 314 or event.code == 315:
		directions.stop()
	if event.code == 316:
		break
directions.stop()
GPIO.cleanup()
