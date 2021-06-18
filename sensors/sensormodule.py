# sensormodule.py
# 
# setting up right and left sensor and their functunality 
#
# Breezja

#setting up motor and controller board
from gpiozero import LineSensor

left_sensor = LineSensor(17)
right_sensor =  LineSensor(27)

#line following algoritm to test robot working :
#	left_detect = int(left_sensor.value)
#	right_detect = int(right_sensor.value)
#	print(left_detect, right_detect)

def isSensorLeft():
  left_detect = int(left_sensor.value)
  if left_detect == 1:
    return True

def isSensorRight():
  right_detect = int(right_sensor.value)
  if right_detect == 1:
    return True 
