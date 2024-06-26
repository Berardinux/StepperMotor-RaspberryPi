from time import sleep
import pigpio

DIR = 20
STEP = 21
SWITCH = 16

pi = pigpio.pi()

pi.set_mode(SWITCH, pigpio.INPUT)
pi.set_pull_up_down(SWITCH, pigpio.PUD_UP)

pi.set_PWM_dutycycle(STEP, 128) # 50% On 50% Off 
pi.set_PWM_frequency(STEP, 500) # 500 pulses per second 

# For more info check out "rdagger68" on Youtube!

try:
  while True:
    pi.write(DIR, pi.read(SWITCH))
    sleep(.1)

except KeyboardInterrupt:
  print ("\nCtrl -C pressed.")
finally:
  pi.set_PWM_dutycycle(STEP, 0)
  pi.stop()