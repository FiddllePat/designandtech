import machine
import neopixel
import time

pixel_pin = 16 # pin for neopixel
pixel = neopixel.NeoPixel(machine.Pin(pixel_pin), 1)

brightness = 0.1 
red_color = (int(255 * brightness), 0, 0) # rgb red colour

pixel[0] = red_color
pixel.write() # sets the neopixel

pins = [8, 9, 10, 11, 12, 13, 14] # array of pins

for pin_number in pins:
    pin = machine.Pin(pin_number, machine.Pin.OUT)
    pin.value(1)
  # ^ set to high (3.3v pin)

while True:
    time.sleep(1)
  # keep the code running ^
