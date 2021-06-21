import RPi.GPIO as GPIO
from evdev import InputDevice, categorize, ecodes
import gpiozero
from directions_pulse import left_forward, right_forward, forward, back, left, right, stop
from time import sleep

controller = InputDevice('/dev/input/event0')

#angle2 = float(0)
#servoPin.value = angle2

speed=30

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
                    forward(speed)
            elif event.value == 1:
                    back(speed)
            else:
                    stop()
    if event.code == 16:
            if event.value == 1:
                    right()
            elif event.value == -1:
                    left()
            else:
                    stop()

    if event.code == 311:
            if event.value == 1 and speed <= 90:
                    speed = speed + 10
                    print("speed at: "+str(speed))
    if event.code == 310:
            if event.value == 1 and speed >= 40:
                    speed = speed - 10
                    print("speed at: "+str(speed))
    if event.code == 314 or event.code == 315:
            stop()
    if event.code == 316:
            break
directions_pulse.stop()
GPIO.cleanup()
