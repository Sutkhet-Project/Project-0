import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD) # choose the pin numbering
GPIO.setup(18, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

while True:
        GPIO.output(18, 1)
        time.sleep(2)
        GPIO.output(19, 1)
        time.sleep(2)
        GPIO.output(22, 1)
        time.sleep(2)
        GPIO.output(23, 1)
        time.sleep(2)
        
        GPIO.output(18, 0)
        time.sleep(2)
        GPIO.output(19, 0)
        time.sleep(2)
        GPIO.output(22, 0)
        time.sleep(2)
        GPIO.output(23, 0)
        time.sleep(2)
        
	
