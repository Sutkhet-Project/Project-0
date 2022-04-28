import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD) # choose the pin numbering
GPIO.setup(18, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(31, GPIO.OUT)
GPIO.setup(32, GPIO.OUT)

def alra(s):
	t = str(s)
	if (t == "A"):
		GPIO.output(18, 0)
	else:
		GPIO.output(18, 1)
	if (t == "B"):
		GPIO.output(19, 0)
	else:
		GPIO.output(19, 1)
	if (t == "C"):
		GPIO.output(22, 0)
	else:
		GPIO.output(22, 1)
	if (t == "D"):
		GPIO.output(23, 0)
	else:
		GPIO.output(23, 1)
	
	if (t == "AB" or t == "BA"):
                GPIO.output(18, 0)
                GPIO.output(19, 0)
	
	if (t == "AC" or t == "CA"):
                GPIO.output(18, 0)
                GPIO.output(22, 0)

	if (t == "AD" or t == "DA"):
                GPIO.output(18, 0)
                GPIO.output(23, 0)
	
	if (t == "BC" or t == "CB"):
                GPIO.output(19, 0)
                GPIO.output(22, 0)

	if (t == "BD" or t == "DB"):
                GPIO.output(19, 0)
                GPIO.output(23, 0)
	
	if (t == "CD" or t == "DC"):
                GPIO.output(22, 0)
                GPIO.output(23, 0)

	if (t == "ABC" or t == "ACB" or t == "BAC" or t == "BCA" or t == "CBA" or t == "CAB"):
                GPIO.output(18, 0)
                GPIO.output(19, 0)
                GPIO.output(22, 0)

	if (t == "ABD" or t == "ADB" or t == "BAD" or t == "BDA" or t == "DBA" or t == "DAB"):
                GPIO.output(18, 0)
                GPIO.output(19, 0)
                GPIO.output(23, 0)

	if (t == "ADC" or t == "ACD" or t == "DAC" or t == "DCA" or t == "CDA" or t == "CAD"):
                GPIO.output(18, 0)
                GPIO.output(22, 0)
                GPIO.output(23, 0)

	if (t == "CBD" or t == "CDB" or t == "BCD" or t == "BDC" or t == "DBC" or t == "DCB"):
                GPIO.output(19, 0)
                GPIO.output(22, 0)
                GPIO.output(23, 0)

	if (t == "ABCD" or t == "ACBD" or t == "ADBC" or t == "ADCB" or t == "ACDB" or t == "ABDC"):
                GPIO.output(18, 0)
                GPIO.output(19, 0)
                GPIO.output(22, 0)
                GPIO.output(23, 0)

	if (t == "BACD" or t == "BCAD" or t == "BDAC" or t == "BDCA" or t == "BCDA" or t == "BADC"):
                GPIO.output(18, 0)
                GPIO.output(19, 0)
                GPIO.output(22, 0)
                GPIO.output(23, 0)

	if (t == "CBAD" or t == "CABD" or t == "CDBA" or t == "CDAB" or t == "CADB" or t == "CBDA"):
                GPIO.output(18, 0)
                GPIO.output(19, 0)
                GPIO.output(22, 0)
                GPIO.output(23, 0)

	if (t == "DBCA" or t == "DCBA" or t == "DABC" or t == "DACB" or t == "DCAB" or t == "DBAC"):
                GPIO.output(18, 0)
                GPIO.output(19, 0)
                GPIO.output(22, 0)
                GPIO.output(23, 0)

