#!/usr/bin/python

import smbus
from uinput import Device 
from ascii_codes import ascii
from keys import keys
import sys
import time
import traceback

i2c_bus = 1 if len(sys.argv) <= 1 else int(sys.argv[1])

bus = smbus.SMBus(i2c_bus)
address = 0x5f


with Device(keys) as device:
    while True:
        try: 
            data = bus.read_byte(address)
        except Exception:
            traceback.print_exc()
            data = 0x00
        #print(format(data,'02x'))
        if data in ascii:
            button = ascii[data]
            device.emit_combo(button)
        time.sleep(0.05);
