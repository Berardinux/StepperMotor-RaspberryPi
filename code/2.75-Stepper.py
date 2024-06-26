from time import sleep
import pigpio
import RPi.GPIO as GPIO

# Define constants
M0 = 14
M1 = 15  # Microstepping pins
M2 = 18

DIR = 20
STEP = 21
SWITCH = 16
PPS = 1000
SUB = -4
ADD = 4

# Initialize pigpio and GPIO
pi = pigpio.pi()

pi.set_mode(SWITCH, pigpio.INPUT)
pi.set_pull_up_down(SWITCH, pigpio.PUD_UP)

pi.set_PWM_dutycycle(STEP, 128)  # 50% On 50% Off
pi.set_PWM_frequency(STEP, PPS)  # 1000 pulses per second

pi.set_mode(M0, pigpio.OUTPUT)
pi.set_mode(M1, pigpio.OUTPUT) # Microstepping pins
pi.set_mode(M2, pigpio.OUTPUT)

# Set microstepping mode
# Full Step          (000)
# Half Step          (100)
# Quarter Step       (010)
# Eigth Step         (110)
# Sixteenth Step     (001)
# Thirty-Second Step (101)

pi.write(M0, 1)
pi.write(M1, 0) # Microstepping output
pi.write(M2, 0)

def Ramp(prev_switch_state):
  start = int(PPS / 1.5)  # Calculate starting point and convert to integer
  end = 100

  # Decrement loop
  for i in range(start, end, SUB):
    pi.set_PWM_frequency(STEP, i)
    pi.write(DIR, prev_switch_state)
    sleep(0.0000005)

  # Increment loop
  for i in range(end, start, ADD):
    pi.set_PWM_frequency(STEP, i)
    pi.write(DIR, current_switch_state)
    sleep(0.0000005)

  print("Previous: ", prev_switch_state)
  print("Current: ", current_switch_state)
  print("Ramp")

try:
  prev_switch_state = pi.read(SWITCH)
  while True:
    current_switch_state = pi.read(SWITCH)
    if prev_switch_state != current_switch_state:
      Ramp(prev_switch_state)
      pi.write(DIR, pi.read(SWITCH))
      prev_switch_state = current_switch_state
      sleep(0.1)

      print("In While Loop Current: ", pi.read(SWITCH))

except KeyboardInterrupt:
  print("\nCtrl -C pressed.")
finally:
  pi.set_PWM_dutycycle(STEP, 0)
  pi.stop()
