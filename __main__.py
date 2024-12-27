#!/usr/bin/python

import smbus
from uinput import Device 
from ascii_codes import ascii
from keys import keys
import sys
import time
import traceback

i2c_bus = 1 if len(sys.argv) <= 1 else int(sys.argv[1])

toggle_keys = {0x77, 0x61, 0x73, 0x64} # W, A, S and D
toggle_states = {key: False for key in toggle_keys}

bus = smbus.SMBus(i2c_bus)
address = 0x5f

with Device(keys) as device:
    while True:
        for key, state in toggle_states.items():
            if state:
                button = ascii[key]
                device.emit_combo(button)

        try: 
            data = bus.read_byte(address)
        except Exception:
            traceback.print_exc()
            data = 0x00

        if data in ascii:
            if data in toggle_keys:
                toggle_states[data] = not toggle_states[data]
            else:
                button = ascii[data]
                device.emit_combo(button)

        time.sleep(0.05)