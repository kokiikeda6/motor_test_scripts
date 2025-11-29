#!/usr/bin/python

import Adafruit_PCA9685
import time

def move(pwm, channel):
  time.sleep(1)
  pwm.set_pwm(channel, 0, 350)
  time.sleep(1)
  pwm.set_pwm(channel, 0, 600)
  time.sleep(1)
  pwm.set_pwm(channel, 0, 0)

pwm = Adafruit_PCA9685.PCA9685(address=0x40, busnum=1)

pwm.set_pwm_freq(60)

move(pwm, 0)
move(pwm, 4)
move(pwm, 8)
