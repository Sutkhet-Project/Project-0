import RPi.GPIO as GPIO
import time

# GPIO.setmode(GPIO.BCM)
GPIO.setmode(GPIO.BOARD) # choose the pin numbering
GPIO.setup(15, GPIO.IN)
GPIO.setup(16, GPIO.IN)

start = GPIO.input(15)
stop = GPIO.input(16)


while True:

        if(start == 1):
                print("A")
	if(stop == 1)
                print("D")
		
