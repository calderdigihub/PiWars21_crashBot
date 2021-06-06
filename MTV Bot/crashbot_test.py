# Simple demo code for tracked robot controlled by Raspberry Pi
#
# Mainly uses RPi.GPIO to manually hit the various pins. 
#
# Motorcontroller: L298N
#
# Good resource: https://www.learnrobotics.org/blog/motor-controller-raspberry-pi-arduino-configurations/

import sys
from time import sleep
import RPi.GPIO as GPIO
#GPIO.setmode(GPIO.BOARD)
mode=GPIO.getmode()

GPIO.cleanup()


#Pins used for motor controller
rightForward=35
rightBackward=37
leftForward=36
leftBackward=38

sleeptime=1

GPIO.setmode(GPIO.BOARD)
GPIO.setup(leftForward, GPIO.OUT)
GPIO.setup(leftBackward, GPIO.OUT)
GPIO.setup(rightForward, GPIO.OUT)
GPIO.setup(rightBackward, GPIO.OUT)

def left_forward(x):
   GPIO.output(leftForward, GPIO.HIGH)
   print("Moving Forward")
   sleep(x)
   GPIO.output(leftBackward, GPIO.LOW)

def left_reverse(x):
   GPIO.output(leftForward, GPIO.HIGH)
   print("Moving Backward")
   sleep(x)
   GPIO.output(leftBackward, GPIO.LOW)

def right_forward(x):
   GPIO.output(rightForward, GPIO.HIGH)
   GPIO.output(rightBackward, GPIO.LOW)
   print("Moving Forward")
   sleep(x)
#  GPIO.output(rightForward, GPIO.LOW)

def right_reverse(x):
   GPIO.output(rightForward, GPIO.LOW)
   GPIO.output(rightBackward, GPIO.HIGH)
   print("Moving Forward")
   sleep(x)
   GPIO.output(leftForward, GPIO.LOW)


def stop():
   print("Stoppppppping")
   GPIO.output(leftForward, GPIO.LOW)
   GPIO.output(leftBackward, GPIO.LOW)
   GPIO.output(rightForward, GPIO.LOW)
   GPIO.output(rightBackward, GPIO.LOW)


right_forward(2)
stop()
sleep(2)
right_reverse(2)
stop()
sleep(2)
left_forward(2)
sleep(2)


stop()
GPIO.cleanup()
