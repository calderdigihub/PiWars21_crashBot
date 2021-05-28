

from microbit import *
from time import sleep

while True:
    pin8.write_digital(0)
    pin16.write_digital(0)
    sleep(1)
    pin8.write_digital(0)
    pin16.write_digital(1)
    sleep(1)
    pin8.write_digital(1)
    pin16.write_digital(0)
    sleep(1)
    pin8.write_digital(0)
    pin16.write_digital(0)
    
    pin8.write_digital(0)
    pin16.write_digital(0)
    sleep(1)
    pin8.write_digital(0)
    pin16.write_digital(1)
    sleep(1)
    pin8.write_digital(1)
    pin16.write_digital(0)
    sleep(1)
    pin8.write_digital(0)
    pin16.write_digital(0)