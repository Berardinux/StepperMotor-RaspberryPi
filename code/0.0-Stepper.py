# Voltage supplyed was 10V and the VREF was .45V

from time import sleep
import RPi.GPIO as GPIO

CW = 1  # Clockwise rotation
CCW = 0  # Counterclockwise rotation
SPR = 200 # (360/2) = 200 steps per revolution

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT) # 20 Direction pin
GPIO.setup(21, GPIO.OUT)# 21 Step pin

# Set direction
GPIO.output(20, 1)

# Step the motor
for _ in range(200):
    GPIO.output(21, GPIO.HIGH)
    sleep(.005)
    GPIO.output(21, GPIO.LOW)
    sleep(.005)
