from sensormodule import isSensorLeft, isSensorRight
from directions import forward, left_forward,right_forward

while True:
    if isSensorLeft() == True:
        right_forward()
    elif isSensorRight() == True:
        left_forward()
    else:
        forward()
