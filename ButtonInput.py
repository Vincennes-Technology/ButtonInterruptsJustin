#!/usr/bin/python
# Script written by Alex Eames. Http://RasPi.tv. Original comments retained.
# Slight variations made by Justin Limbach (noted in comments)

import RPi.GPIO as GPIO
import time
# Displaying to LCD deviation from original code
import Adafruit_CharLCD as LCD
lcd = LCD.Adafruit_CharLCDPlate()
GPIO.setmode(GPIO.BCM)

# GPIO 23 & 24 set up as inputs. I (Justin Limbach) modified the original
# Script so both are pulled up and waiting for a falling edge.
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
time_stamp = time.time()

# now we'll define the threaded callback function
# This will run in another thread when our event is detected
def my_callback(channel):
    lcd.clear()
    lcd.message('Falling edge\non port 24!')    # Omitted extra print lines

raw_input(lcd.message('Press Enter \nwhen ready\n>'))
# Setting up so that when port 24 has falling edge, my_callback happens

GPIO.add_event_detect(24, GPIO.FALLING, callback=my_callback, bouncetime = 200)

# Changed the text that displays because why not
try:
    lcd.clear()
    lcd.message('Watching \n Port 23')
    GPIO.wait_for_edge(23, GPIO.FALLING)
    lcd.clear()
    lcd.message('All Your Base R \n Belong To Us!')

except KeyboardInterrupt:
    GPIO.cleanup()
GPIO.cleanup()