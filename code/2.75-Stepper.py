from time import sleep
import pigpio
import RPi.GPIO as GPIO

M0 = 14
M1 = 15 # Microstepping pins
M2 = 18

DIR = 20
STEP = 21
SWITCH = 16
PPS = 500

pi = pigpio.pi()

pi.set_mode(SWITCH, pigpio.INPUT)
pi.set_pull_up_down(SWITCH, pigpio.PUD_UP)

pi.set_PWM_dutycycle(STEP, 128) # 50% On 50% Off 
pi.set_PWM_frequency(STEP, 500) # 500 pulses per second 

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

# For more info check out "rdagger68" on Youtube!

def Ramp():
  for i in range(PPS, 0, -1):
    pi.set_PWM_frequency(STEP, i)
    pi.write(DIR, pi.read(SWITCH))
    sleep(.00005)
  for i in range(0, 500, +1):
    pi.set_PWM_frequency(STEP, i)
    pi.write(DIR, pi.read(SWITCH))
    sleep(.00005)
  print("Ramp")

try:
  prev_switch_state = pi.read(SWITCH)
  while True:
    
    current_switch_state = pi.read(SWITCH)
    if prev_switch_state != current_switch_state:
      Ramp()
    print(prev_switch_state + current_switch_state)
    pi.write(DIR, pi.read(SWITCH))
    sleep(.1)
    prev_switch_state = current_switch_state


except KeyboardInterrupt:
  print ("\nCtrl -C pressed.")
finally:
  pi.set_PWM_dutycycle(STEP, 0)
  pi.stop()