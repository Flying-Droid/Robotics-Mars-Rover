import time
import board
import pwmio
import digitalio
from sonarbit import Sonarbit
from adafruit_motor import servo

#init our servo
pwm = pwmio.PWMOut(board.D0,frequency=50)
pwm_2 = pwmio.PWMOut(board.D1, frequency=50)

led_right = digitalio.DigitalInOut(board.D9)
led_u_turn = digitalio.DigitalInOut(board.D12)
led_forward = digitalio.Direction.OUTPUT
led_right.direction = digitalio.Direction.OUTPUT

servo_1 = servo.ContinuousServo(pwm)
servo_2 = servo.ContinuousServo(pwm_2)

distance_sensor_front = Sonarbit(board.D2)
distance_sensor_right = Sonarbit(board.D3)


#D0 left servo
#D1 right servo
#D2 Distance sensor front
#D3 Distance sensor right

def stop_rover():
    # Code to stop the rover's motors
    servo_1.throttle = 0
    servo_2.throttle = 0
    time.sleep(2.0)

def reverse():
    print("reverse")
    servo_1.throttle = -0.5
    servo_2.throttle = -0.5

def right():
    print("right")
    servo_1.throttle = -0.365
    servo_2.throttle = -0.2
    time.sleep(0.7)

def u_turn():
    print("u turn")
    servo_1.throttle = 1
    servo_2.throttle = 1
    time.sleep(1.35)



def move_forward():
    # Code to move the rover forward
    servo_1.throttle = -0.18
    servo_2.throttle = 0.5

prev_distance = 570  # Initial value
prev_distance_right = 570


while True:
    #read distance sensor
    distance = distance_sensor_front.get_distance(prev_distance)
    distance_right = distance_sensor_right.get_distance(prev_distance)

    if distance_right > 30 :  # Wall in front and wall on the right

        right()
        move_forward()

        time.sleep(2.5)

        print("right")
        stop_rover()
        print("stop")
    else:
        if distance > 30:
            move_forward()
            print("forward")
            stop_rover()

            print("stop")

        else:
            u_turn()

            print("u turn")

            stop_rover()

            print("stop")





    prev_distance = distance
    prev_distance_right = distance_right
    time.sleep(0.1)
    print(distance)




