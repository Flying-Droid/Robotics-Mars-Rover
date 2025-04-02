
import time
import board
import pwmio
from adafruit_motor import servo
from rc import RCReceiver
from arcade_drive_servo import Drive


pwm = pwmio.PWMOut(board.D5, duty_cycle=2 ** 15, frequency=50)
my_servo = servo.Servo(pwm)

rc = RCReceiver(ch1 = board.D10, ch2 = board.D11, ch3 = None, ch4 = None,
ch5 = board.D12, ch6 = board.D13)

drive = Drive(left_pin=board.D2, right_pin=board.D3, left_stop=0.0, right_stop=0.0)

while True:
    spin = rc.read_channel(1) # spin
    throttle = rc.read_channel(2) # throttle
    arm = rc.read_channel(6)

    if spin is not None and throttle is not None: # must not be None to do something with the output
        drive.drive(spin,throttle)
        #print("spin", spin, "throttle", throttle) # move our motors arcade drive style

    else:
        if arm == 0:
            my_servo.angle = 0 # set the servo to 0 Degrees, the min point
            time.sleep(1)
            print("0 degrees")
        elif arm == 1:
            myy_servo.angle = 90 # set the servo to 0 Degrees, the min point
            time.sleep(1)
            print("90 degrees")
        elif arm == 2:
            my_servo.angle = 180 # set the servo to 0 Degrees, the min point
            time.sleep(1)
            print("180 degrees")

    time.sleep(0.02)  # Maintains sync wit






'''import board
import time
from rc import RCReceiver
from arcade_drive_servo import Drive

rc = RCReceiver(ch1=board.D10, ch2=board.D11, ch3=None, ch4=None, ch5=board.D12, ch6=board.D13)
drive = Drive(left_pin=board.D0, right_pin=board.D1, left_stop=0.0, right_stop=0.0)

channels = [1,2,5,6]

while True:
    # Read joystick channels
    spin = rc.read_channel(1)
    throttle = rc.read_channel(2)

    if spin is not None and throttle is not None:
        drive.drive(spin,throttle)
        #drive.drive(50,50) stop
        print("spin", spin, "throttle", throttle)


    time.sleep(0.02)
'''
'''
import time
import board
from rc import RCReceiver

# init rc reciver

rc = RCReceiver(ch1=board.D10, ch2=board.D11, ch3=None, ch4=None, ch5=board.D12, ch6=board.D13)

while True:
    ch1 = rc.read_channel(1)
    ch2 = rc.read_channel(2)
    ch5 = rc.read_channel(5)
    ch6 = rc.read_channel(6)
    print("ch1:", ch1, "ch2:", ch2, "ch5:", ch5, "ch6:", ch6,  )

    time.sleep(0.02) #Keeps us in sync with the 50hz duty cycle

'''



