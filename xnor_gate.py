import machine
import neopixel
import time

pixel_pin = 16
pixel = neopixel.NeoPixel(machine.Pin(pixel_pin), 1)

input_pins = [machine.Pin(i, machine.Pin.IN) for i in range(16)] + [machine.Pin(i, machine.Pin.IN) for i in range(26, 30)]

def count_high_pins(pins):
    return sum(pin.value() for pin in pins)

while True:
    if count_high_pins(input_pins) % 2 == 0:
        pixel[0] = (0, 255, 0)
        pixel.write()
        time.sleep(1)

        pixel[0] = (0, 0, 255)
        pixel.write()
        time.sleep(1)
        
        pixel[0] = (0, 255, 0)
        pixel.write()
        time.sleep(1)
    else:
        pixel[0] = (0, 0, 0)
        pixel.write()
        time.sleep(0.1)
