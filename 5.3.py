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


def doLED(num):
    out = 0

    if num >= 128:
        out += 128

    if num >= 64:
        out += 64
    
    if num >= 32:
        out += 32
    
    if num >= 16:
        out += 16
    
    if num >= 8:
        out += 8
    
    if num >= 4:
        out += 4
    
    if num >= 2:
        out += 2
    
    if num >= 1:
        out += 1
    
    return dec2bin(out)


GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
leds = [2, 3, 5, 17, 27, 22, 10, 9]
comp = 14
troyka = 13

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

try:
    while True:
        val = adc()
        GPIO.output(leds, doLED(val))

        if val != 0:
            print(f"number = {val}")
            print(f"voltage = {val*3.3/256}")

finally:
    GPIO.setup(dac, 0)
    GPIO.cleanup()


