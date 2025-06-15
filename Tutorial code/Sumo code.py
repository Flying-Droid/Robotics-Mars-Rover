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

# ------ OLED screen setup ------
displayio.release_displays()  # Ensure no displays are already in use

oled_reset = board.D9  # Define reset pin for OLED (not used later)

# Initialize I2C display
i2c = board.I2C()
display_bus = I2CDisplayBus(i2c, device_address=0x3d)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

# ------ Input setup ------
button = DigitalInOut(board.D2)
button.direction = Direction.INPUT
button.pull = Pull.UP  # Internal pull-up resistor

Touchsensor = DigitalInOut(board.D7)
Touchsensor.direction = Direction.INPUT
Touchsensor.pull = Pull.UP  # Internal pull-up resistor

# ------ Sensor and actuator setup ------
distance_sensor_front = Sonarbit(board.D3)  # Ultrasonic sensor
analog_in = AnalogIn(board.A0)  # Line sensor (analog input)

# PWM outputs for continuous servos
pwm = pwmio.PWMOut(board.D0, duty_cycle=2 ** 15, frequency=50)
pwm2 = pwmio.PWMOut(board.D1, duty_cycle=2 ** 15, frequency=50)
my_servo_right = servo.ContinuousServo(pwm)
my_servo_left = servo.ContinuousServo(pwm2)

# ------ Helper function ------
def mapped_voltage(pin):
    # Convert analog value (0-65535) to 0-100 scale
    mapped_value = map_range(pin.value, 0, 65535, 0, 100)
    return round(mapped_value)

# ------ Threshold definitions ------
black_min = 70   # Minimum value for detecting black
white_max = 50   # Max value for detecting white
air_min = 51     # Air detection range lower bound
air_max = 79     # Air detection range upper bound

robot_active = False  # Flag to activate robot logic
prev_distance = 570   # Initial distance reading

print("start loop")

# ------ Initial movement ------
# Small reverse and pause, then turn in place to prepare
my_servo_left.throttle = -0.15
my_servo_right.throttle = -0.15
time.sleep(0.3)

my_servo_left.throttle = 0.0
my_servo_right.throttle = 0.0
time.sleep(0.4)

my_servo_left.throttle = 0.5
my_servo_right.throttle = -0.5  # Turn in place

# ------ Behavior Functions ------

def search():
    print("we're on white!")
    print("Colour", line_sensor)
    # Move forward slowly while searching
    my_servo_left.throttle = -0.15
    my_servo_right.throttle = -0.15

def black_line():
    print("on black line!")
    print("Colour", line_sensor)
    # Stop, back up, and turn around
    my_servo_left.throttle = 0.0
    my_servo_right.throttle = 0.0
    time.sleep(0.2)

    my_servo_left.throttle = -0.7
    my_servo_right.throttle = -0.6
    time.sleep(3)

    my_servo_left.throttle = -0.2
    my_servo_right.throttle = -0.2
    time.sleep(1.3)

def enemy_found():
    print("I see you!")
    # Spin in place aggressively (presumably to face or engage the enemy)
    my_servo_left.throttle = 0.5
    my_servo_right.throttle = -0.5

# ------ Main Loop ------
while True:
    if button.value == False:  # Button pressed
        robot_active = True
        contact = False  # Possibly for touch logic (not used here)

    if robot_active:
        line_sensor = mapped_voltage(analog_in)
        distance = distance_sensor_front.get_distance(prev_distance)

        if line_sensor > black_min:
            black_line()
        else:
            if distance < 60:
                enemy_found()
            else:
                search()

    time.sleep(0.02)  # Small delay to prevent CPU overload
