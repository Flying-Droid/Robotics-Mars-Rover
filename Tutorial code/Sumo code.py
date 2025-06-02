import time
import board
from analogio import AnalogIn
from adafruit_simplemath import map_range
from adafruit_motor import servo
import pwmio
import displayio
import terminalio
import adafruit_displayio_ssd1306
from digitalio import DigitalInOut, Direction, Pull
from i2cdisplaybus import I2CDisplayBus
from sonarbit import Sonarbit
#------ OLED screen ------
displayio.release_displays()

oled_reset = board.D9

#releases current displays if any were initialized before setup
displayio.release_displays()

# Use for I2C
i2c = board.I2C()
display_bus = I2CDisplayBus(i2c, device_address=0x3d) # or 0x3d
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

button= DigitalInOut(board.D2)
button.direction=Direction.INPUT
button.pull= Pull.UP

Touchsensor= DigitalInOut(board.D7)
Touchsensor.direction= Direction.INPUT
Touchsensor.pull= Pull.UP
distance_sensor_front = Sonarbit(board.D3)
#distance_sensor_right = Sonarbit(board.D3)
analog_in = AnalogIn(board.A0)
new_min = 0
new_max = 100
pwm = pwmio.PWMOut(board.D0, duty_cycle=2 ** 15, frequency=50)
pwm2 = pwmio.PWMOut(board.D1, duty_cycle=2 ** 15, frequency=50)
my_servo_right = servo.ContinuousServo(pwm)
my_servo_left = servo.ContinuousServo(pwm2)

def mapped_voltage(pin):
    # Maps our current 0-65535 range to 0-100
    mapped_value = map_range(pin.value, 0, 65535, 0, 100)
    return round(mapped_value)



# ----------- INIT VARIABLES --------------
black_min = 70  # change to minimum observed reading for black
white_max = 50  # change to maximum observed reading for white
air_min = 51  # change to minimum observed reading for in the air
air_max = 79  # change to minimum observed reading for in the air
robot_active=False
prev_distance = 570
print("start loop")

'''
#right

my_servo_left.throttle=-0.5
my_servo_right.throttle=-0.5
time.sleep(0.5)

'''

my_servo_left.throttle=-0.15
my_servo_right.throttle=-0.15
time.sleep(0.3)

my_servo_left.throttle=0.0
my_servo_right.throttle=0.0
time.sleep(0.4)

my_servo_left.throttle=0.5
my_servo_right.throttle=-0.5

def search():
    print("we're on white!")
    print("Colour",line_sensor)
    my_servo_left.throttle=-0.15
    my_servo_right.throttle=-0.15




def black_line():
    print("on black line!")
    print("Colour",line_sensor)
    #stop
    my_servo_left.throttle=0.0
    my_servo_right.throttle=0.0
    time.sleep(0.2)
    #Backup
    my_servo_left.throttle=--0.7
    my_servo_right.throttle=-0.6
    time.sleep(3)
    #Turn around
    my_servo_left.throttle=-0.2
    my_servo_right.throttle=-0.2
    time.sleep(1.3)



def enemy_found():
    print("I see you!")
    my_servo_left.throttle=0.5
    my_servo_right.throttle=-0.5





while True:
    if button.value == False:
        robot_active = True
        contact=False
    if robot_active:
        line_sensor = mapped_voltage(analog_in)
        distance = distance_sensor_front.get_distance(prev_distance)# Replace with your init sensor

        if line_sensor > black_min:
            black_line()


        else:

            if distance < 60:
                enemy_found()


            else:
                search()



    time.sleep(0.02)

#turn 45 degrees
