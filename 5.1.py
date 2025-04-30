import RPi.GPIO as GPIO
import time

def dec2bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def adc():
    for i in range(256):
        out = dec2bin(i)
        GPIO.output(dac, out)

        time.sleep(0.05)
        compare = GPIO.input(comp)

        if compare == 1:
            return i

    return 0

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

try:
    while True:
        val = adc()
        if val != 0:
            print(f"number = {val}")
            print(f"voltage = {val*3.3/256}")

finally:
    GPIO.setup(dac, 0)
    GPIO.cleanup()


