import RPi.GPIO as GPIO

M0 = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(M0, GPIO.OUT)

while True:
  GPIO.output(M0, GPIO.HIGH)