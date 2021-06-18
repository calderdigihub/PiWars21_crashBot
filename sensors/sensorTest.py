import sensormodule
from time import sleep

while True:
    if sensormodule.isSensorLeft()== True:
      print("Sensed Left")
    elif sensormodule.isSensorRight()== True:
      print("Sensed right")
    else: 
      print("Nothing sensed")

    sleep(1)

