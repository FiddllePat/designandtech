import machine
import neopixel
import time

# Pin for the NeoPixel
pixel_pin = 16
pixel = neopixel.NeoPixel(machine.Pin(pixel_pin), 1)

# Define pins 8-14 as input pins
input_pins = [machine.Pin(i, machine.Pin.IN) for i in range(8, 15)]

def any_pin_high(pins):
    return any(pin.value() for pin in pins)

while True:
    if any_pin_high(input_pins):
        pixel[0] = (84, 0, 159)
        pixel.write()
        time.sleep(1)
    else:
        pixel[0] = (0, 0, 0) # turn off the pin
        pixel.write()
        time.sleep(0.1) 
