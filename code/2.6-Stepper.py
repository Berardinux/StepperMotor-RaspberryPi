from time import sleep
import pigpio

DIR = 20
STEP = 21
SWITCH = 16
PPS = 500

pi = pigpio.pi()

pi.set_mode(SWITCH, pigpio.INPUT)
pi.set_pull_up_down(SWITCH, pigpio.PUD_UP)

pi.set_PWM_dutycycle(STEP, 128) # 50% On 50% Off 
pi.set_PWM_frequency(STEP, 500) # 500 pulses per second 

# For more info check out "rdagger68" on Youtube!

def Ramp():
  for i in range(PPS, 0, -1):
    pi.set_PWM_frequency(STEP, i)
    pi.write(DIR, pi.read(SWITCH))
    sleep(.05)
  for i in range(0, 500, +1):
    pi.set_PWM_frequency(STEP, i)
    pi.write(DIR, pi.read(SWITCH))
    sleep(.05)

try:
  prev_switch_state = pi.read(SWITCH)
  while True:
    current_switch_state = pi.read(SWITCH)
    if current_switch_state != current_switch_state:
      Ramp()
    prev_switch_state = current_switch_state

    pi.write(DIR, pi.read(SWITCH))
    sleep(.1)


except KeyboardInterrupt:
  print ("\nCtrl -C pressed.")
finally:
  pi.set_PWM_dutycycle(STEP, 0)
  pi.stop()