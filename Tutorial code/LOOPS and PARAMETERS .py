import time
import board
import pwmio
from adafruit_motor import servo

#left servo - D0
#Right servo - D1

pwm = pwmio.PWMOut(board.D0, frequency=50)
pwm_2 = pwmio.PWMOut(board.D1, frequency=50)

servo_1 = servo.ContinuousServo(pwm)
servo_2 = servo.ContinuousServo(pwm_2)

user_f_input = int(input("How long do you want your robot to move forward"))

def move_forward():
    # Code to move the rover forward
    servo_1.throttle = -1
    servo_2.throttle = 1

    print("forward")


def moving_forward(robot_f):
    move_forward()
    time.sleep(robot_f)


moving_forward(user_f_input)








'''#Challange 3
def set_speed(speed):
    print("speed", speed, "set!")

for i in range (1,6,1):
    set_speed(i)
'''

'''
#Challange 2 loops
for timer in range(10,0, -1):


    print(timer)
    time.sleep(1)

print("Launch")

'''

'''
#Challange 1 for loops

for lift_object in range(4):
    time.sleep(1)
    print("Object lifted")
'''





'''
#Challange 3

def calculate_speed(distance, time):

    speed = distance / time


    print("The robots speed is", speed)


calculate_speed(20,2)

'''





'''

#Challange 2

user_name = input("What is your name")

user_greeting = input("How would you like to be greeted")

def greeting_message(user_name, user_greeting):
    print(user_greeting,user_name)


greeting_message(user_name, user_greeting)
'''
