import machine
import neopixel
import time

pixel_pin = 16 # pixel pin
pixel = neopixel.NeoPixel(machine.Pin(pixel_pin), 1)


input_pins = [machine.Pin(i, machine.Pin.IN) for i in range(8, 15)] # pin array define

def count_high_pins(pins):
    return sum(pin.value() for pin in pins)

while True:
     if count_high_pins(input_pins) >= 7: # if all the pins are high then light it up
        pixel[0] = (84, 0, 159)
        pixel.write()
        time.sleep(1)
    else:
        pixel[0] = (0, 0, 0) if # if all pins are not high then dont light up
        pixel.write()
        time.sleep(0.1)

