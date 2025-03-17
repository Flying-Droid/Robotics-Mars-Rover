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

def move_forward(sleep_time):
    # Code to move the rover forward
    servo_1.throttle = -1
    servo_2.throttle = 1
    time.sleep(sleep_time)
    print("forward")

def stop_rover(sleep_time):
    # Code to stop the rover's motors
    print("stop")
    servo_1.throttle = 0
    servo_2.throttle = 0
    time.sleep(time_sleep)

def right(sleep_time):
    print("right")
    # code to turn our servos right
    servo_1.throttle = -1
    servo_2.throttle = 0
    time.sleep(sleep_time)

def left(sleep_time):
    print("left")
    #code to turn our servos left
    servo_1.throttle = 1
    servo_2.throttle = 1
    time.sleep(sleep_time)

def u_turn(sleep_time):
    print("u turn")
    # code to make our robot do a 180
    servo_1.throttle = 1
    servo_2.throttle = 1
    time.sleep(sleep_time)

while True:
    right(0.5)
    move_forward(0.1)

'''

# draw a circle

right(7.6)

'''
'''

#Make a triangle

move_forward(1.5)

right(1.4)

move_forward(1.5)

right(1.4)

move_forward(1.5)
'''
'''
#Make a sqaure

move_forward(1)

right(1)

move_forward(1)

right(1)

move_forward(1)


right(1)

move_forward(1)


'''






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
