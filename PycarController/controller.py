from pynput.keyboard import Key, Controller
from picar import front_wheels
from picar import back_wheels
import time


class PiCarController:
    force_turning = 0  # 0 = random direction, 1 = force left, 2 = force right, 3 = orderdly

    fw = front_wheels.Front_Wheels(db='config')
    bw = back_wheels.Back_Wheels(db='config')
    fw.turning_max = 45

    forward_speed = 100
    backward_speed = 100

    back_distance = 10
    turn_distance = 20

    timeout = 10
    last_angle = 90
    last_dir = 0

    turning_angle = 8

    current_angle = 100
    moving = False
    turning = False

    def debug(self, func):
        print(func)
        print("is moving - {}".format(self.moving))
        print("is turning - {}".format(self.turning))

    def on_press(self, key):
        self.debug("on_press")
        if key in [Key.up, Key.down, Key.left, Key.right]:
            if key == Key.down and self.moving is False:
                self.moving = True
                print("down")
                self.bw.backward()
                self.bw.speed = self.backward_speed
            elif key == Key.up and self.moving is False:
                print("up")
                self.moving = True
                self.bw.forward()
                self.bw.speed = self.forward_speed
            elif key == Key.left and self.turning is False:
                self.turning = True
                print("left")
                if self.current_angle - self.turning_angle > 50:
                    self.current_angle -= self.turning_angle
                    self.fw.turn(self.current_angle)

            elif key == Key.right and self.turning is False:
                self.turning = True
                print("right")
                if self.current_angle + self.turning_angle < 150:
                    self.current_angle += self.turning_angle
                    self.fw.turn(self.current_angle)

    def on_release(self, key):
        self.debug("on_release")
        if key in [Key.up, Key.down, Key.left, Key.right]:
            if key == Key.down and self.moving is True:
                self.moving = False
                print("down - stop")
                self.bw.stop()
            elif key == Key.up and self.moving is True:
                self.moving = False
                print("up - stop")
                self.bw.stop()
            elif key == Key.left and self.turning is True:
                self.turning = False
                print("left - stop")

            elif key == Key.right and self.turning is True:
                self.turning = False
                print("right - stop")

        if key == Key.esc:
            # Stop listener
            return False
