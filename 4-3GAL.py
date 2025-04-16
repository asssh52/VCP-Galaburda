import RPi.GPIO as GPIO

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)

channel = GPIO.PWM(24, 1000)
channel.start(0)

try:
    while True:
        koef = int(input("Input coefficient."))
        channel.ChangeDutyCycle(koef)

        print(3.3*koef/100)


except ValueError:
    print("Wrong input value.")

finally:
    channel.stop()
    GPIO.cleanup()
