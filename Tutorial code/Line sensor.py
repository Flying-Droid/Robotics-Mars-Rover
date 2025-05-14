import time
import board
from analogio import AnalogIn
from adafruit_simplemath import map_range

analog_in_sensor = AnalogIn(board.A0)

def read_analog_sensor(pin):
   return round(map_range(analog_in_sensor.value, 0, 65536, 0,100))
  #value, old_minumium, old_maximuim, new_min, new_max

while True:
   print(read_analog_sensor(analog_in_sensor))
   time.sleep(0.1)
