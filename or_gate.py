import machine
import neopixel
import time

pixel_pin = 16
pixel = neopixel.NeoPixel(machine.Pin(pixel_pin), 1)
input_pins = [machine.Pin(i, machine.Pin.IN) for i in range(16)] + [machine.Pin(i, machine.Pin.IN) for i in range(26, 30)]

def any_pin_high(pins):
    return any(pin.value() for pin in pins)

while True:
    if any_pin_high(input_pins):
        pixel[0] = (0, 255, 0)  # Green
        pixel.write()
        time.sleep(1)

        pixel[0] = (0, 0, 255)  # Blue
        pixel.write()
        time.sleep(1)
        
        pixel[0] = (0, 255, 0)  # Green
        pixel.write()
        time.sleep(1)
    else:
        pixel[0] = (0, 0, 0)  # Turn off the LED if no inputs are high
        pixel.write()
        time.sleep(0.1)  # Wait for a short time before checking again
