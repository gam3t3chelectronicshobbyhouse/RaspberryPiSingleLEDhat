#!/usr/bin/env python3
import RPi.GPIO as GPIO
import psutil

LED = 18

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED, GPIO.OUT)

try:
    while (1):
        cpu_pc = psutil.cpu_percent(interval=1)
        print("CPU = " + str(cpu_pc) + "%")
        if cpu_pc <= 50:
            GPIO.output(LED, False)
        if 50 < cpu_pc < 100:
            GPIO.output(LED, True)
except KeyboardInterrupt:
    GPIO.cleanup()
    print ("Thank you for using CPU Monitor")
