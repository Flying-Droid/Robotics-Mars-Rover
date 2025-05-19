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

'''
#------ OLED screen ------
displayio.release_displays()

oled_reset = board.D9

# Use for I2C
i2c = board.I2C()
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=oled_reset)

WIDTH = 128
HEIGHT = 64  # Change to 32 if needed
BORDER = 5

display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=WIDTH, height=HEIGHT)

'''
button= DigitalInOut(board.D2)
button.direction=Direction.INPUT
button.pull= Pull.UP

analog_in = AnalogIn(board.A0)
new_min = 0
new_max = 100
pwm = pwmio.PWMOut(board.D0, duty_cycle=2 ** 15, frequency=50)
pwm2 = pwmio.PWMOut(board.D1, duty_cycle=2 ** 15, frequency=50)
my_servo_right = servo.Servo(pwm)
my_servo_left = servo.Servo(pwm)
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
while True:
    if button.value == False:
        robot_active = True

    elif robot_active == True:
        line_sensor = mapped_voltage(analog_in)  # Replace with your init sensor

        if line_sensor > black_min:
            print("on black line!")
            print(line_sensor)
            # Stop
            my_servo_left.throttle = 0.0
            my_servo_right.throttle = 0.0
            time.sleep(0.2)
            # Backup
            my_servo_left.throttle = -0.5
            my_servo_right.throttle = -0.5
            time.sleep(0.3)
            # Turn around
            my_servo_left.throttle = 0.5
            my_servo_right.throttle = -0.5
            time.sleep(0.75)
            # Consider turning on debug LED 1 here

        elif air_min < line_sensor < air_max:
            print("lifted up in the air!")
            print(line_sensor)
            my_servo_left.throttle = 0.5
            my_servo_right.throttle = 0.5
            # Consider turning on debug LED 2 here

        else:
            print("we're on white!")
            print(line_sensor)
            my_servo_left.throttle = 0.5
            my_servo_right.throttle = 0.5
            # Consider turning off all LEDs here

        time.sleep(0.02)


