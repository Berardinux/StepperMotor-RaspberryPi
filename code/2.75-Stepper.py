from time import sleep
import pigpio
import RPi.GPIO as GPIO

M0 = 14
M1 = 15 # Microstepping pins
M2 = 18

DIR = 20
STEP = 21
SWITCH = 16
PPS = 2000

pi = pigpio.pi()

pi.set_mode(SWITCH, pigpio.INPUT)
pi.set_pull_up_down(SWITCH, pigpio.PUD_UP)

pi.set_PWM_dutycycle(STEP, 128) # 50% On 50% Off 
pi.set_PWM_frequency(STEP, 2000) # 2000 pulses per second 

GPIO.setmode(GPIO.BCM)
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
GPIO.output(M1, GPIO.HIGH) # Microstepping output
GPIO.output(M2, GPIO.LOW)

def Ramp(prev_switch_state):
  for i in range(PPS, 0, -1):
    pi.set_PWM_frequency(STEP, i)
    pi.write(DIR, prev_switch_state)
    sleep(.0000005)
    if i < PPS/1.5:
      -i
      if i < PPS/2:
        -i
  for i in range(0, PPS, +1):
    pi.set_PWM_frequency(STEP, i)
    pi.write(DIR, current_switch_state)
    sleep(.0000005)
    if i < PPS/2:
      +i
      if i < PPS/2:
        -i
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
    sleep(.1)
    
    print("In While Loop Current: ", pi.read(SWITCH))

except KeyboardInterrupt:
  print ("\nCtrl -C pressed.")
finally:
  pi.set_PWM_dutycycle(STEP, 0)
  pi.stop()
  GPIO.cleanup()