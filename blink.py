import RPi.GPIO as GPIO
import time
ledPin = 12
blinkDelay = .5
ledOn = True
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledPin, GPIO.OUT)
try:
    while True:
        print("led=" + str(ledOn))
        GPIO.output(ledPin, ledOn)
        ledOn = not ledOn
        time.sleep(blinkDelay)

except:
    GPIO.cleanup()
    print("Thanks for using blink.py\n")