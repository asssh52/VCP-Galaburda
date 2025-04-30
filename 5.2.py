import RPi.GPIO as GPIO
import time

def dec2bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def adc():

    num = 128
    binNum = dec2bin(num)

    GPIO.output(dac, binNum)

    time.sleep(0.01)
    compare = GPIO.input(comp)

    if compare == 1:
        num -= 64
    else:
        num += 64
    

    binNum = dec2bin(num)

    GPIO.output(dac, binNum)

    time.sleep(0.01)
    compare = GPIO.input(comp)

    if compare == 1:
        num -= 32
    else:
        num += 32
    

    binNum = dec2bin(num)

    GPIO.output(dac, binNum)

    time.sleep(0.01)
    compare = GPIO.input(comp)

    if compare == 1:
        num -= 16
    else:
        num += 16
    

    binNum = dec2bin(num)

    GPIO.output(dac, binNum)

    time.sleep(0.01)
    compare = GPIO.input(comp)

    if compare == 1:
        num -= 8
    else:
        num += 8
    
    
    binNum = dec2bin(num)

    GPIO.output(dac, binNum)

    time.sleep(0.01)
    compare = GPIO.input(comp)

    if compare == 1:
        num -= 4
    else:
        num += 4
    
    
    binNum = dec2bin(num)

    GPIO.output(dac, binNum)

    time.sleep(0.01)
    compare = GPIO.input(comp)

    if compare == 1:
        num -= 2
    else:
        num += 2
    
        binNum = dec2bin(num)


    GPIO.output(dac, binNum)

    time.sleep(0.01)
    compare = GPIO.input(comp)

    if compare == 1:
        num -= 1
    else:
        num += 1

    return num

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


