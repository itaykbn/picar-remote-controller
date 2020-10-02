#!/usr/bin/env python
'''
**********************************************************************
* Filename    : ultra_sonic_avoidance.py
* Description : An example for sensor car kit to followe light
* Author      : Dream
* Brand       : SunFounder
* E-mail      : service@sunfounder.com
* Website     : www.sunfounder.com
* Update      : Dream    2016-09-27    New release
**********************************************************************
'''

from SunFounder_Ultrasonic_Avoidance import Ultrasonic_Avoidance
from picar import front_wheels
from picar import back_wheels
import time
import picar
import random

force_turning = 0    # 0 = random direction, 1 = force left, 2 = force right, 3 = orderdly

picar.setup()

ua = Ultrasonic_Avoidance.Ultrasonic_Avoidance(20)
fw = front_wheels.Front_Wheels(db='config')
bw = back_wheels.Back_Wheels(db='config')
fw.turning_max = 45

forward_speed = 70
backward_speed = 70

back_distance = 10
turn_distance = 20

timeout = 10
last_angle = 90
last_dir = 0

def move():
    angle = 100
    direction = 'f'
    duration = 1
    
    while True:
        copy = input("copy?\n")
        if(copy == "n"):
            angle = float(input("enter angle: \n"))
            fw.turn(angle)
            direction = input("enter f(forwards) or b(backwards): \n")
            duration = int(input("enter time: \n"))
        
        
        fw.turn(angle)

        if(direction == "f"):
            bw.forward()
            bw.speed = forward_speed
        
        elif(direction == "b"):
            bw.backward()
            bw.speed = backward_speed
        
#        fw.turn(angle)
        time.sleep(duration)
        bw.stop()
        
  

def stop():
    bw.stop()
    fw.turn_straight()

if __name__ == '__main__':
    try:
        move()
    except KeyboardInterrupt:
        stop()