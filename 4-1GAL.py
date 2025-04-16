import RPi.GPIO as GPIO

def dec2bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

GPIO.setwarnings(False)
dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    while True:
        num = input("Input an integer from 0 to 255.\n")

        try:
            num = int(num)

            if 0 <= num <= 255:
                GPIO.output(dac, dec2bin(num))
                vol = float(num) / 256.0 * 3.3

                print(f"voltage: {vol}")
            else:
                if num < 0:
                    print("Too small.")
                if num > 255:
                    print("Too large.")

        except ValueError:
            try:
                float(num)
                print("Not a float.")

            except ValueError:
                if num == "q": break
                else: 
                    print("Not a string. Integer.")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()

