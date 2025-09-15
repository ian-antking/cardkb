#!/usr/bin/python

import smbus
from uinput import Device
from cardkb.ascii_codes import ascii
from cardkb.keys import keys
import sys
import time
import traceback

def print_help():
    print("""
CardKB - M5Stack Card Keyboard for Raspberry Pi

Usage:
  sudo cardkb [I2C_BUS]

Arguments:
  I2C_BUS    Optional. I²C bus number to use (default: 1).

Options:
  -h, --help  Show this help message and exit.
""")

def main():
    if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
        print_help()
        sys.exit(0)
     
    i2c_bus = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    bus = smbus.SMBus(i2c_bus)
    address = 0x5F

    with Device(keys) as device:
        while True:
            try:
                data = bus.read_byte(address)
            except Exception:
                traceback.print_exc()
                data = 0x00

            if data in ascii:
                button = ascii[data]
                device.emit_combo(button)

            time.sleep(0.05)

if __name__ == "__main__":
    main()
