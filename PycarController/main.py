from controller import PiCarController
from pynput.keyboard import Key, Listener, Controller
import picar
from picar import front_wheels, back_wheels

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


def debug(func):
    print(func)
    print("is moving - {}".format(moving))
    print("is turning - {}".format(turning))


def on_press(key):
    global moving, turning
    global current_angle
    debug("on_press")
    if key in [Key.up, Key.down, Key.left, Key.right]:
        if key == Key.down:
            moving = True
            print("down")
            bw.backward()
            bw.speed = backward_speed
        elif key == Key.up:
            print("up")
            moving = True
            bw.forward()
            bw.speed = forward_speed
        elif key == Key.left:
            turning = True
            print("left")
            if current_angle - turning_angle > 60:
                current_angle -= turning_angle
                fw.turn(current_angle)
        elif key == Key.right:
            turning = True
            print("right")
            if current_angle + turning_angle < 140:
                current_angle += turning_angle
                fw.turn(current_angle)


def on_release(key):
    global moving, turning
    if key in [Key.up, Key.down, Key.left, Key.right]:
        if key == Key.down:
            moving = False
            print("down - stop")
            bw.stop()
        elif key == Key.up:
            moving = False
            print("up - stop")
            bw.stop()
        elif key == Key.left:
            turning = False
            print("left - stop")
        elif key == Key.right:
            turning = False
            print("right - stop")

    if key == Key.esc:
            # Stop listener
            return False


def main():
    picar.setup()
    controller = PiCarController()

    # Collect events until released
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()


if __name__ == '__main__':
    main()
    # picar.front_wheels.Front_Wheels().turn_straight()
