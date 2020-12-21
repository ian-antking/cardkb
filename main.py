#!/usr/bin/python

import smbus
import uinput

bus = smbus.SMBus(1)
address = 0x5f

ascii = {
    0x1B: uinput.KEY_ESC,
    0x31: uinput.KEY_1,
    0x32: uinput.KEY_2,
    0x33: uinput.KEY_3,
    0x34: uinput.KEY_4,
    0x35: uinput.KEY_5,
    0x36: uinput.KEY_6,
    0x37: uinput.KEY_7,
    0x38: uinput.KEY_8,
    0x39: uinput.KEY_9,
    0x30: uinput.KEY_0,
    0x08: uinput.KEY_BACKSPACE,
    0xB5: uinput.KEY_UP,
    0x09: uinput.KEY_TAB,
    0x71: uinput.KEY_Q,
    0x77: uinput.KEY_W,
    0x65: uinput.KEY_E,
    0x72: uinput.KEY_R,
    0x74: uinput.KEY_T,
    0x79: uinput.KEY_Y,
    0x75: uinput.KEY_U,
    0x69: uinput.KEY_I,
    0x6F: uinput.KEY_O,
    0x70: uinput.KEY_P,
    0xB6: uinput.KEY_DOWN,
    0x61: uinput.KEY_A,
    0x73: uinput.KEY_S,
    0x64: uinput.KEY_D,
    0x66: uinput.KEY_F,
    0x67: uinput.KEY_G,
    0x68: uinput.KEY_H,
    0x6A: uinput.KEY_J,
    0x6B: uinput.KEY_K,
    0x6C: uinput.KEY_L,
    0x0D: uinput.KEY_ENTER,
    0xB4: uinput.KEY_LEFT,
    0x7A: uinput.KEY_Z,
    0x78: uinput.KEY_X,
    0x63: uinput.KEY_C,
    0x76: uinput.KEY_V,
    0x62: uinput.KEY_B,
    0x6E: uinput.KEY_N,
    0x6D: uinput.KEY_M,
    0x2C: uinput.KEY_COMMA,
    0x2E: uinput.KEY_DOT,
    0x20: uinput.KEY_SPACE,
    0xB7: uinput.KEY_RIGHT,
    0x51: [uinput.KEY_LEFTSHIFT, uinput.KEY_Q]
}

keys = [
    uinput.KEY_ESC,
    uinput.KEY_1,
    uinput.KEY_2,
    uinput.KEY_3,
    uinput.KEY_4,
    uinput.KEY_5,
    uinput.KEY_6,
    uinput.KEY_7,
    uinput.KEY_8,
    uinput.KEY_9,
    uinput.KEY_0,
    uinput.KEY_BACKSPACE,
    uinput.KEY_UP,
    uinput.KEY_TAB,
    uinput.KEY_Q,
    uinput.KEY_W,
    uinput.KEY_E,
    uinput.KEY_R,
    uinput.KEY_T,
    uinput.KEY_Y,
    uinput.KEY_U,
    uinput.KEY_I,
    uinput.KEY_O,
    uinput.KEY_P,
    uinput.KEY_DOWN,
    uinput.KEY_A,
    uinput.KEY_S,
    uinput.KEY_D,
    uinput.KEY_F,
    uinput.KEY_G,
    uinput.KEY_H,
    uinput.KEY_J,
    uinput.KEY_K,
    uinput.KEY_L,
    uinput.KEY_ENTER,
    uinput.KEY_LEFT,
    uinput.KEY_Z,
    uinput.KEY_X,
    uinput.KEY_C,
    uinput.KEY_V,
    uinput.KEY_B,
    uinput.KEY_N,
    uinput.KEY_M,
    uinput.KEY_COMMA,
        uinput.KEY_DOT,
    uinput.KEY_SPACE,
    uinput.KEY_RIGHT,
    uinput.KEY_LEFTSHIFT
]

with uinput.Device(keys) as device:
    while True:
        data = bus.read_byte(address)
        if data:
            button = ascii[data]
            if isinstance(button, list):
                device.emit_combo(button)
            else:
                device.emit_click(ascii[data])