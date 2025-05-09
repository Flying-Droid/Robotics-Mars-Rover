#import necessary moduals
import time
import board
import pwmio
from adafruit_motor import servo
from rc import RCReceiver
from arcade_drive_servo import Drive
import busio
import adafruit_apds9960.apds9960
import displayio
import terminalio
import adafruit_displayio_ssd1306


#------------ Oled screen -------------

#code for oled
displayio.release_displays()
#initiallising vairibles
i2c = busio.I2C(board.SCL, board.SDA)

oled_reset = board.D9

display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=oled_reset)

WIDTH = 128
HEIGHT = 64  # Change to 32 if needed
BORDER = 5

display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=WIDTH, height=HEIGHT)






# ----------- Color sensor -----------------


sensor = adafruit_apds9960.apds9960.APDS9960(i2c)

sensor.enable_color = True#enabling our sensors
sensor.enable_proximity = True

# ----------- Servos -----------------
#code for servos
#initiallising vairibles
pwm = pwmio.PWMOut(board.D5, duty_cycle=2 ** 15, frequency=50)
pwm2 = pwmio.PWMOut(board.D2, duty_cycle=2 ** 15, frequency=50)
my_servo = servo.Servo(pwm)#servos
arm= servo.Servo(pwm2)#drill

# ----------- Controler signals -----------------

#code for channles
rc = RCReceiver(ch1 = board.D10, ch2 = board.D11, ch3 = None, ch4 = None,
ch5 = board.D12, ch6 = board.D13)

# code for reote control dive
drive = Drive(left_pin=board.D0, right_pin=board.D1)
#function to move the arm up and down
def operate_drill(deploy):
     if deploy is not None: # must not be None to do something with the output
        if deploy == False: # if switch is up bring up drill
            arm.angle = 0 # set the servo to 0 Degrees, the min point

        elif deploy == True:#if sitch is down bring the drill down
            arm.angle = 180


def read_colour_sensor(num_colours, num_average):#code to read the sensor thrice and to average them
    x = (r+g+b+c)/num_colours

    y = (r+g+b+c)/num_colours

    z = (r+g+b+c)/num_colours


    average = (x+y+x)/num_average

    print("This is the average:", average)





while True:
    #initialising channnels and colours and proximity and calling on the operate_drill function
    spin = rc.read_channel(1) # spin
    throttle = rc.read_channel(2) # throttle
    arm_turn= rc.read_channel(5)
    screen= rc.read_channel(6)
    r, g, b, c = sensor.color_data
    proximity = sensor.proximity
    operate_drill(arm_turn)


    if spin is not None and throttle is not None:
        drive.drive(spin,throttle)#code to make the robot drive

    if screen is not None:
        if screen== 0:
            read_colour_sensor(4,3)# when the sitch is down it gives the average of the colours

            #print("Red:", r, "Green:", g , "Blue:", b, "Clear:", c)

        elif screen==1:
            print("Proximity:", proximity)# prints the proximity
        else:
            print("Closed")#if the switch is in the up position do nothing


    time.sleep(0.02)  # Maintains sync





