import RPi.GPIO as GPIO
import time 

def dec2bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

GPIO.setwarnings(False)
dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)


voltage = 1
inc = 1

try:
    user_input = input("Input time interval.")
    interval = float(user_input)
    while True:
        GPIO.output(dac, dec2bin(voltage))

        if voltage == 255:
            inc = -1

        if voltage == 0:
            inc = 1

        voltage += inc     

        time.sleep(interval)

except ValueError:
    print("Wrong interval.")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()

