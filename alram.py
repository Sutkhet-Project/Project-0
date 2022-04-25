import time
def alr(s):
                t = str(s)
# แจ้งเตือน
                if (t == "A"):
                        GPIO.output(18, 0)
                if (t == "B"):
                        GPIO.output(19, 0)
                if (t == "C"):
                        GPIO.output(22, 0)
                if (t == "D"):
                        GPIO.output(23, 0)
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
                if (t == "ACB" or t == "ABC" or t == "BCA" or t == "BAC" or t == "CAB" or t == "CBA"):
                        GPIO.output(18, 0)
                        GPIO.output(19, 0)
                        GPIO.output(22, 0)
                if (t == "ADB" or t == "ABD" or t == "BDA" or t == "BAD" or t == "DAB" or t == "DBA"):
                        GPIO.output(18, 0)
                        GPIO.output(19, 0)
                        GPIO.output(23, 0)
                if (t == "ACD" or t == "ADC" or t == "DCA" or t == "DAC" or t == "CAD" or t == "CDA"):
                        GPIO.output(18, 0)
                        GPIO.output(22, 0)
                        GPIO.output(23, 0)
                if (t == "DCB" or t == "DBC" or t == "BCD" or t == "BDC" or t == "CDB" or t == "CBD"):
                        GPIO.output(19, 0)
                        GPIO.output(22, 0)
                        GPIO.output(23, 0)

        # LOGGER.info(f'{s}Done. ({t3 - t2:.3f}s)')

