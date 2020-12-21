#!/usr/bin/python

import smbus
from uinput import Device 
from ascii_codes import ascii
from keys import keys

bus = smbus.SMBus(1)
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