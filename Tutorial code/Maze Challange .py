import time
import board
import pwmio
from digitalio import DigitalInOut, Direction, Pull
from sonarbit import Sonarbit
from adafruit_motor import servo

#init our servo
pwm = pwmio.PWMOut(board.D0,frequency=50)
pwm_2 = pwmio.PWMOut(board.D1, frequency=50)

led_right = DigitalInOut(board.D9)
led_forward = DigitalInOut(board.D12)

led_right.direction = Direction.OUTPUT
led_forward.direction = Direction.OUTPUT

servo_1 = servo.ContinuousServo(pwm)
servo_2 = servo.ContinuousServo(pwm_2)

distance_sensor_front = Sonarbit(board.D2)
distance_sensor_right = Sonarbit(board.D3)
distance_sensor_left = Sonarbit(board.D5)


#D0 left servo
#D1 right servo
#D2 Distance sensor front
#D3 Distance sensor right

def stop_rover():
    # Code to stop the rover's motors
    print("stop")
    servo_1.throttle = 0
    servo_2.throttle = 0
    time.sleep(2.0)


def reverse():
    print("reverse")
    servo_1.throttle = -0.5
    servo_2.throttle = -0.5

def right():
    print("right")
    servo_1.throttle = -0.5
    servo_2.throttle = -0.6
    time.sleep(0.75)

def left():
    print("left")
    servo_1.throttle = 0.4
    servo_2.throttle = 0.6
    time.sleep(0.7)

def u_turn():
    print("u turn")
    servo_1.throttle = 1
    servo_2.throttle = 1
    time.sleep(1.35)



def move_forward():
    # Code to move the rover forward
    servo_1.throttle = -0.25
    servo_2.throttle = 0.2
    time.sleep(2.0)
    print("forward")

prev_distance = 570  # Initial value
prev_distance_right = 570



while True:
    #read distance sensor
    distance = distance_sensor_front.get_distance(prev_distance)
    distance_right = distance_sensor_right.get_distance(prev_distance)
    distance_left = distance_sensor_left.get_distance(prev_distance)
    if distance_right > 20 :
        time.sleep(1.0)
        #If no wall on right turn right
        led_right.value=False


        right()
        move_forward()

        stop_rover()


    else:
        time.sleep(1.0)
        led_right.value=True
        if distance > 20:
            led_forward.value=False

            move_forward()


            stop_rover()

        else:
            if distance_left > 20:
                left()
                move_forward()
                stop_rover()






            else:
                u_turn()
                led_forward.value=True
                stop_rover()







    prev_distance = distance
    prev_distance_right = distance_right
    prev_distance_left = distance_left
    time.sleep(0.1)
    print(distance)



