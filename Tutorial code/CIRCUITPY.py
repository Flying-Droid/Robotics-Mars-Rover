import time
import board
import pwmio
from adafruit_motor import servo
from rc import RCReceiver
from arcade_drive_servo import Drive

'''

# ----------- Color sensor -----------------

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)

sensor.enable_color = True

while True:
    r, g, b, c = sensor.color_data
    print("Red:", r, "Green:", g , "Blue:", b, "Clear:", c)
    time.sleep(1)




#------------ Oled screen -------------

displayio.release_displays()

oled_reset = board.D9

i2c = board.I2C()
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=oled_reset)

WIDTH = 128
HEIGHT = 64  # Change to 32 if needed
BORDER = 5

display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=WIDTH, height=HEIGHT)

for i in range(5):
    print("index:", i)
    time.sleep(1)
'''

#-----------------------------------------

pwm = pwmio.PWMOut(board.D5, duty_cycle=2 ** 15, frequency=50)
my_servo = servo.Servo(pwm)

rc = RCReceiver(ch1 = board.D10, ch2 = board.D11, ch3 = None, ch4 = None,
ch5 = board.D12, ch6 = board.D13)


drive = Drive(left_pin=board.D0, right_pin=board.D1)

while True:
    spin = rc.read_channel(1) # spin
    throttle = rc.read_channel(2) # throttle

    if spin is not None and throttle is not None:
        drive.drive(spin,throttle)
        print("spin", spin, "throttle", throttle)


'''
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

'''



