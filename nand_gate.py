import machine
import neopixel
import time

pixel_pin = 16
pixel = neopixel.NeoPixel(machine.Pin(pixel_pin), 1)

input_pins = [machine.Pin(i, machine.Pin.IN) for i in range(16)] + [machine.Pin(i, machine.Pin.IN) for i in range(26, 30)]

def all_pins_high(pins):
    return all(pin.value() for pin in pins)

while True:
    if not all_pins_high(input_pins):
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
