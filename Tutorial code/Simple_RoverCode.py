import time
import board
import pwmio
from adafruit_motor import servo
#init our servo
pwm = pwmio.PWMOut(board.D0, duty_cycle = 2**15, frequency=50)
pwm_2 = pwmio.PWMOut(board.D1, duty_cycle = 2**15, frequency=50)


servo_1 = servo.ContinuousServo(pwm)
servo_2 = servo.ContinuousServo(pwm_2)


def straight():
    .throttle = 0.5
    m2.throttle = -0.45


def straight():
    servo_1.throttle = 0.365
    servo_2.throttle = -0.5

def stop():
    servo_1.throttle = 0.0
    servo_2.throttle = 0.0



while true
    print("right")
    servo_1.throttle = 0
    servo_2.throttle = 0.5
    print("left")
    servo_1.throttle = 0.5
    servo_2.throttle = 0


'''while True:
    print("forward")
    servo_1.throttle = 1.0
    servo_2.throttle = 1.0
    time.sleep(5.0)
    print("stop")
    servo_1.throttle = 0.0
    servo_2.throttle = 0.0
    time.sleep(1.0)
    print("reverse")
    servo_1.throttle = -1.0
    servo_2.throttle = -1.0
    time.sleep(5.0)
    print("stop")
    servo_1.throttle = -0.0
    servo_2.throttle = 0.0
    time.sleep(1.0)# Write your code here :-)



