#!/usr/bin/env python


"""
Used for dumping the states of all the pins on an RPI 3 B(+)
board.
"""


import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)
#GPIO.setmode(GPIO.BCM)

# 40 pins
all_pins = range(1, 41)

for pin_num in all_pins:
    try:
        GPIO.setup(pin_num, GPIO.IN, GPIO.PUD_DOWN)
        val = GPIO.input(pin_num)
        
        if val:
            print("Pin {} is HIGH".format(pin_num))
        else:
            print("Pin {} is LOW".format(pin_num))
    except:
        print("error with pin {}".format(pin_num))
        continue

GPIO.cleanup()
print("done")

