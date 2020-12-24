#!/usr/bin/python

import smbus
from uinput import Device 
from ascii_codes import ascii
from keys import keys
import sys

i2c_bus = int(sys.argv[1] or 1)

bus = smbus.SMBus(i2c_bus)
address = 0x5f


with Device(keys) as device:
    while True:
        data = bus.read_byte(address)
        if data:
            try:
                button = ascii[data]
                if isinstance(button, list):
                    device.emit_combo(button)
                else:
                    device.emit_click(button)
            except Exception as error:
                print(error)