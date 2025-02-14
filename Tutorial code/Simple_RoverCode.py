import time
import board
import pwmio
from sonarbit import Sonarbit
from adafruit_motor import servo

#init our servo
pwm = pwmio.PWMOut(board.D0,frequency=50)
pwm_2 = pwmio.PWMOut(board.D1, frequency=50)

servo_1 = servo.ContinuousServo(pwm)
servo_2 = servo.ContinuousServo(pwm_2)

distance_sensor = Sonarbit(board.D2)

prev_distance = 570  # Initial value

def straight():
    print("forward")
    servo_1.throttle = 0.365
    servo_2.throttle = -0.5
def stop():
    print("stop")
    servo_1.throttle = 0.0
    servo_2.throttle = 0.0

def reverse():
    print("reverse")
    servo_1.throttle = -0.5
    servo_2.throttle = -0.5

def right():
    print("right")
    servo_1.throttle = 0.2
    servo_2.throttle = 0.2

def left():
    print("left")
    servo_1.throttle = 0.2
    servo_2.throttle = -0.2

def distance_wall():
    global prev_distance
    distance = distance_sensor.get_distance(prev_distance)
    print("The object is: " + str(distance) +  " cm away")

    prev_distance = distance

# Function to control your rover motors
def stop_rover():
    # Code to stop the rover's motors
    servo_1.throttle = 0
    servo_2.throttle = 0

def move_forward():
    # Code to move the rover forward
    servo_1.throttle = -0.365
    servo_2.throttle = 0.5

while True:
    #read distance sensor
    distance = distance_sensor.get_distance(prev_distance)

    if distance < 10:  # Threshold in cm
        stop_rover()
    else:
        move_forward()

    prev_distance = distance
    time.sleep(0.1)
    print(distance)


