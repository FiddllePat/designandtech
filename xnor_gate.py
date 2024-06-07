import machine
import neopixel
import time

# Pin for the NeoPixel
pixel_pin = 16
pixel = neopixel.NeoPixel(machine.Pin(pixel_pin), 1)

# Define pins 8-14 as input pins
input_pins = [machine.Pin(i, machine.Pin.IN) for i in range(8, 14)]

def count_high_pins(pins):
    return sum(pin.value() for pin in pins)

while True:
    high_pin_count = count_high_pins(input_pins)
    if (high_pin_count // 2) != 0:
        pixel[0] = (84, 0, 159)  # Purple color
    else:
        pixel[0] = (0, 0, 0)  # Turn off
    pixel.write()
    time.sleep(0.1)  # Check the pins every 0.1 seconds

