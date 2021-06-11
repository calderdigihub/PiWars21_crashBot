import RPi.GPIO as GPIO
from evdev import InputDevice, categorize, ecodes
import sys
from time import sleep

mode=GPIO.getmode()

GPIO.cleanup()

rightForward=37
rightBackward=35
leftForward=38
leftBackward=36

GPIO.setmode(GPIO.BOARD)
GPIO.setup(leftForward, GPIO.OUT)
GPIO.setup(leftBackward, GPIO.OUT)
GPIO.setup(rightForward, GPIO.OUT)
GPIO.setup(rightBackward, GPIO.OUT)

def left_forward():
	GPIO.output(leftForward, GPIO.HIGH)
	GPIO.output(leftBackward, GPIO.LOW)
	print("Moving forward L")
def left_reverse():
	GPIO.output(leftForward, GPIO.LOW)
	GPIO.output(leftBackward, GPIO.HIGH)
	print("Moving back L")
def right_forward():
	GPIO.output(rightForward, GPIO.HIGH)
	GPIO.output(rightBackward, GPIO.LOW)
	print("Moving forward R")
def right_reverse():
	GPIO.output(rightForward, GPIO.LOW)
	GPIO.output(rightBackward, GPIO.HIGH)
	print("Moving back R")

	GPIO.output(leftForward, GPIO.LOW)

def stop():
	print("Stoping")
	GPIO.output(leftForward, GPIO.LOW)
	GPIO.output(leftBackward, GPIO.LOW)
	GPIO.output(rightForward, GPIO.LOW)
	GPIO.output(rightBackward, GPIO.LOW)



def back():
	right_reverse()
	left_forward()
	print("F")
def forward():
	right_forward()
	left_reverse()
	print("B")

def left():
	right_forward()
	left_forward()
	print("L")
def right():
	right_reverse()
	left_reverse()
	print("R")

controller = InputDevice('/dev/input/event2')


for event in controller.read_loop():

	print(str(event.code)+" "+str(event.value))

       # if event.code == 17:
       #    if event.value == -1:
       #         do this
       #     elif event.value == 1:
       #         do that

       # if event.code == 16:




	if event.code == 17 and event.value == -1:
		forward()
	if event.code == 17 and event.value == 1:
		back()
	if event.code == 16 and event.value == 1:
		right()
	if event.code == 16 and event.value == -1:
		left()
	if event.code == 314 or event.code == 315:
		stop()
	if event.code == 316:
		break
	if event.code == 17 and event.value == 0 or event.code == 16 and event.value == 0:
		stop()
	if event.code == 304 and event.value == 1:
		left_reverse()
		sleep(2)
		stop()
		left_forward()
		sleep(2)
		stop()
		right_forward()
		sleep(2)
		stop()
		right_reverse()
		sleep(2)
		stop()


stop()
GPIO.cleanup()
