import machine
import neopixel
import time

# Pin for the NeoPixel
pixel_pin = 16
pixel = neopixel.NeoPixel(machine.Pin(pixel_pin), 1)

# Define pins 8-14 as input pins
input_pins = [machine.Pin(i, machine.Pin.IN) for i in range(8, 14)]

def all_pins_high(pins):
    return all(pin.value() for pin in pins)

while True:
    if not all_pins_high(input_pins):
        pixel[0] = (84, 0, 159)  # Purple color
        pixel.write()
    else:
        pixel[0] = (0, 0, 0)  # Turn off
        pixel.write()
    time.sleep(0.1)  # Check the pins every 0.1 seconds

