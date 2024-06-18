from time import sleep
import RPi.GPIO as GPIO

M0 = 14
M1 = 15 # Microstepping pins
M2 = 18

DIR = 20  # Direction pin
STEP = 21  # Step pin
CW = 1  # Clockwise rotation
CCW = 0  # Counterclockwise rotation
SPR = 200 # (360/1.8) = 200 steps per revolution

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)

GPIO.setup(M0, GPIO.OUT)
GPIO.setup(M1, GPIO.OUT) # Microstepping pins
GPIO.setup(M2, GPIO.OUT) 

# Full Step          (000)
# Half Step          (100)
# Quarter Step       (010)
# Eigth Step         (110)
# Sixteenth Step     (001)
# Thirty-Second Step (101)

GPIO.output(M0, GPIO.LOW)
GPIO.output(M1, GPIO.LOW) # Microstepping output
GPIO.output(M2, GPIO.LOW)

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