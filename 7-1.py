import RPi.GPIO as GPIO
import matplotlib.pyplot as plt
import time

def dec2bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def adc(sleeep):

    num = 128
    binNum = [int(bit) for bit in bin(num)[2:].zfill(8)]

    GPIO.output(dac, binNum)

    time.sleep(sleeep)
    compare = GPIO.input(comp)

    if compare == 1:
        num -= 64
    else:
        num += 64
    

    binNum = [int(bit) for bit in bin(num)[2:].zfill(8)]

    GPIO.output(dac, binNum)

    time.sleep(sleeep)
    compare = GPIO.input(comp)

    if compare == 1:
        num -= 32
    else:
        num += 32
    

    binNum = [int(bit) for bit in bin(num)[2:].zfill(8)]

    GPIO.output(dac, binNum)

    time.sleep(sleeep)
    compare = GPIO.input(comp)

    if compare == 1:
        num -= 16
    else:
        num += 16
    

    binNum = [int(bit) for bit in bin(num)[2:].zfill(8)]

    GPIO.output(dac, binNum)

    time.sleep(sleeep)
    compare = GPIO.input(comp)

    if compare == 1:
        num -= 8
    else:
        num += 8
    
    
    binNum = [int(bit) for bit in bin(num)[2:].zfill(8)]

    GPIO.output(dac, binNum)

    time.sleep(sleeep)
    compare = GPIO.input(comp)

    if compare == 1:
        num -= 4
    else:
        num += 4
    
    
    binNum = [int(bit) for bit in bin(num)[2:].zfill(8)]

    GPIO.output(dac, binNum)

    time.sleep(sleeep)
    compare = GPIO.input(comp)

    if compare == 1:
        num -= 2
    else:
        num += 2
    
        binNum = [int(bit) for bit in bin(num)[2:].zfill(8)]


    GPIO.output(dac, binNum)

    time.sleep(sleeep)
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

def printLED(sleeep):
    val = adc(sleeep)
    #GPIO.output(leds, doLED(val))

    #if val != 0 and 0:
    #    print(f"number = {val}")
    #    print(f"voltage = {val*3.3/256}")

    return val

dac     = [8, 11, 7, 1, 0, 5, 12, 6]
leds    = [2, 3, 4, 17, 27, 22, 10, 9]
comp    = 14
troyka  = 13

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

mesList = []

flag = 0

try:
    interval = 0.0025
    GPIO.output(troyka, 1)

    startTime = time.time()

    while True:
        val = printLED(interval)
        mesList.append(val)

        if val > 205:
            GPIO.output(troyka, 0)
            flag = 1
        
        if val < 195 and flag:
            endTime = time.time()
            totalTime = endTime - startTime

            file = open("mes.txt", "w")
            fileText = ""

            for data in mesList:
                fileText += str(data/256*3.3) + "\n"
            
            file.write(fileText)
            file.close()

            settings = open("settings.txt", "w")
            settings.write(f"discr: {len(mesList)/totalTime} hz\nstep:{3.3/256} V")
            settings.close()

            print(f"\n\nresults:\n")

            print(f"totalTime = {totalTime}")
            print(f"mesTime = {interval * 7}s")
            print(f"discr: {len(mesList)/totalTime} Hz")
            print(f"step:{3.3/256} V")

            plt.plot(mesList)
            plt.grid(True)
            plt.savefig("picture.png")
            plt.show()

            exit()


finally:
    GPIO.output(dac, 0)
    GPIO.output(leds, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()