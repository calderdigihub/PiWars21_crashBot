import RPi.GPIO as GPIO
from evdev import InputDevice, categorize, ecodes
import gpiozero

import sys
from time import sleep


GPIO.cleanup()

rightForward=26
rightBackward=19
leftForward=20
leftBackward=16
up=13
down=6
servoPin=gpiozero.Servo(17)



GPIO.setmode(GPIO.BCM)
GPIO.setup(leftForward, GPIO.OUT)
GPIO.setup(leftBackward, GPIO.OUT)
GPIO.setup(rightForward, GPIO.OUT)
GPIO.setup(rightBackward, GPIO.OUT)
GPIO.setup(up, GPIO.OUT)
GPIO.setup(down, GPIO.OUT)


def left_reverse():
	GPIO.output(leftForward, GPIO.HIGH)
	GPIO.output(leftBackward, GPIO.LOW)
	print("Moving back L")
def left_forward():
	GPIO.output(leftForward, GPIO.LOW)
	GPIO.output(leftBackward, GPIO.HIGH)
	print("Moving forward L")
def right_forward():
	GPIO.output(rightForward, GPIO.HIGH)
	GPIO.output(rightBackward, GPIO.LOW)
	print("Moving forward R")
def right_reverse():
	GPIO.output(rightForward, GPIO.LOW)
	GPIO.output(rightBackward, GPIO.HIGH)
	print("Moving back R")

def stop():
	print("Stoping")
	GPIO.output(leftForward, GPIO.LOW)
	GPIO.output(leftBackward, GPIO.LOW)
	GPIO.output(rightForward, GPIO.LOW)
	GPIO.output(rightBackward, GPIO.LOW)
	GPIO.output(down, GPIO.LOW)
	GPIO.output(up, GPIO.LOW)



def back():
	right_reverse()
	left_reverse()
	print("B")
def forward():
	right_forward()
	left_forward()
	print("F")

def left():
	right_forward()
	left_reverse()
	print("L")
def right():
	right_reverse()
	left_forward()
	print("R")


def f_up():
	GPIO.output(up, GPIO.HIGH)
	GPIO.output(down, GPIO.LOW)
	print ("Rasing")
def f_down():
	GPIO.output(down, GPIO.HIGH)
	GPIO.output(up, GPIO.LOW)
	print ("Lowering")
#def f_angle(angle):
	#claw.ChangeDutyCycle(angle)
	#print("Angle at: "+str((angle-2)*18))
def f_angle_zero(angle2):
	servoPin.value = angle2
	print ("Angle at: "+str(angle2*90))



controller = InputDevice('/dev/input/event0')
#angle = float(12)
angle2 = float(0)
#claw.ChangeDutyCycle
servoPin.value = angle2


for event in controller.read_loop():

	print(str(event.code)+" "+str(event.value))

       # if event.code == 17:
       #    if event.value == -1:
       #         do this
       #     elif event.value == 1:
       #         do that

       # if event.code == 16:

	if event.code == 17: 
		if event.value == -1:
			forward()
		elif event.value == 1:
			back()
		else:
			stop()
	if event.code == 16:
		if event.value == 1:
			right()
		elif event.value == -1:
			left()
		else:
			stop()

	if event.code == 304:
		if event.value == 1:
			f_down()
		else:
			stop()

	if event.code == 308:
		if event.value == 1:
			f_up()
		else:
			stop()

	if event.code == 305:
		if event.value == 1:
			if angle2 + (2/18) <=1:
				angle2 = angle2 + (2/18)
				f_angle_zero(angle2)
			#if angle + (10/18) <=12:
				#angle = angle + (10/18)
				#f_angle(angle)
		else:
			stop()

	if event.code == 307:
		if event.value == 1:
			if angle2 - (2/18) >= -1:
				angle2 = angle2 - (2/18)
				f_angle_zero(angle2) 
			#if angle - (10/18) >=2:
				#angle = angle - (10/18)
				#f_angle(angle)
		else:
			stop()
			
	if event.code == 314 or event.code == 315:
		stop()
	if event.code == 316:
		break
stop()
GPIO.cleanup()

