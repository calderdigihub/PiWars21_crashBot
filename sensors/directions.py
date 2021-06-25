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
up=15 
down=16 
open=29 
close=32 

GPIO.setmode(GPIO.BOARD) 
GPIO.setup(leftForward, GPIO.OUT) 
GPIO.setup(leftBackward, GPIO.OUT) 
GPIO.setup(rightForward, GPIO.OUT) 
GPIO.setup(rightBackward, GPIO.OUT) 
GPIO.setup(up, GPIO.OUT) 
GPIO.setup(down, GPIO.OUT) 
GPIO.setup(open, GPIO.OUT) 
GPIO.setup(close, GPIO.OUT) 

  

  

  

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
        GPIO.output(open, GPIO.LOW) 
        GPIO.output(close, GPIO.LOW) 

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
        print("UP") 
def f_down(): 
        GPIO.output(down, GPIO.HIGH) 
        GPIO.output(up, GPIO.LOW) 
        print("DOWN") 
def f_open(): 
        GPIO.output(open, GPIO.HIGH) 
        GPIO.output(close, GPIO.LOW) 
        print("UP") 
def f_close(): 
        GPIO.output(close, GPIO.HIGH) 
        GPIO.output(open, GPIO.LOW) 
        print("DOWN") 
