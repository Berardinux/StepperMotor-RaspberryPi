# Voltage supplyed was 10V and the VREF was .45V

from time import sleep
import RPi.GPIO as GPIO

DIR = 20  # Direction pin
STEP = 21  # Step pin
CW = 1  # Clockwise rotation
CCW = 0  # Counterclockwise rotation
SPR = 200 # (360/2) = 200 steps per revolution

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)

def step_motor(direction, steps, delay):
    # Set direction
    GPIO.output(DIR, direction)

    # Step the motor
    for _ in range(steps):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)

try:
    step_motor(CW, SPR *4, 0.0005)

    sleep(1)

    step_motor(CCW, SPR, 0.005)

except KeyboardInterrupt:
    print("Program interrupted by user")
finally:
    GPIO.cleanup()
