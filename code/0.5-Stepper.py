from time import sleep
import RPi.GPIO as GPIO

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT) # 20 Direction pin
GPIO.setup(21, GPIO.OUT)# 21 Step pin

# Set direction
GPIO.output(20, 1) # 1 or a 0 to change the direction

# Step the motor
for _ in range(200):
    GPIO.output(21, GPIO.HIGH)
    sleep(.0025)
    GPIO.output(21, GPIO.LOW)
    sleep(.0025)

GPIO.cleanup()