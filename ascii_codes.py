import uinput

ascii = {
  # number row
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

  # top row
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

  # home row
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

  # bottom row
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

  # arrow keys
    0xB4: uinput.KEY_LEFT,
    0xB5: uinput.KEY_UP,
    0xB6: uinput.KEY_DOWN,
    0xB7: uinput.KEY_RIGHT,

    # number row symbols
    0x21: [uinput.KEY_LEFTSHIFT, uinput.KEY_1],
    0x40: [uinput.KEY_LEFTSHIFT, uinput.KEY_APOSTROPHE],
    0x23: [uinput.KEY_LEFTSHIFT, uinput.KEY_BACKSLASH],
    0x24: [uinput.KEY_LEFTSHIFT, uinput.KEY_4],
    0x25: [uinput.KEY_LEFTSHIFT, uinput.KEY_5],
    0x5E: [uinput.KEY_LEFTSHIFT, uinput.KEY_6],
    0x26: [uinput.KEY_LEFTSHIFT, uinput.KEY_7],
    0x2A: [uinput.KEY_LEFTSHIFT, uinput.KEY_8],
    0x28: [uinput.KEY_LEFTSHIFT, uinput.KEY_9],
    0x29: [uinput.KEY_LEFTSHIFT, uinput.KEY_0],
    0x7B: [uinput.KEY_LEFTSHIFT, uinput.KEY_LEFTBRACE],
    0x7D: [uinput.KEY_LEFTSHIFT, uinput.KEY_RIGHTBRACE],

    # top row symbols
    0x5B: uinput.KEY_LEFTBRACE,
    0x5D: uinput.KEY_RIGHTBRACE,
    0x2f: uinput.KEY_SLASH,
    0x5C: uinput.KEY_BACKSLASH, #outputs `#``
    0x7C: [uinput.KEY_LEFTSHIFT, uinput.KEY_SLASH], #outputs `?`
    0x7E: [uinput.KEY_LEFTSHIFT, uinput.KEY_BACKSLASH],
    0x27: uinput.KEY_APOSTROPHE,
    0x22: [uinput.KEY_LEFTSHIFT, uinput.KEY_2],

    # bottom row symbols
    0x3B: uinput.KEY_SEMICOLON,
    0x3A: [uinput.KEY_LEFTSHIFT, uinput.KEY_SEMICOLON],
    0x60: uinput.KEY_GRAVE,
    0x2B: [uinput.KEY_LEFTSHIFT, uinput.KEY_EQUAL],
    0x2D: uinput.KEY_MINUS,
    0x5F: [uinput.KEY_LEFTSHIFT, uinput.KEY_MINUS],
    0x3D: uinput.KEY_EQUAL,
    0x3F: [uinput.KEY_LEFTSHIFT, uinput.KEY_SLASH],
    0x3C: [uinput.KEY_LEFTSHIFT, uinput.KEY_COMMA],
    0x3E: [uinput.KEY_LEFTSHIFT, uinput.KEY_DOT],

    # top row capitals
    0x51: [uinput.KEY_LEFTSHIFT, uinput.KEY_Q],
    0x57: [uinput.KEY_LEFTSHIFT, uinput.KEY_W],
    0x45: [uinput.KEY_LEFTSHIFT, uinput.KEY_E],
    0x52: [uinput.KEY_LEFTSHIFT, uinput.KEY_R],
    0x54: [uinput.KEY_LEFTSHIFT, uinput.KEY_T],
    0x59: [uinput.KEY_LEFTSHIFT, uinput.KEY_Y],
    0x55: [uinput.KEY_LEFTSHIFT, uinput.KEY_U],
    0x49: [uinput.KEY_LEFTSHIFT, uinput.KEY_I],
    0x4F: [uinput.KEY_LEFTSHIFT, uinput.KEY_O],
    0x50: [uinput.KEY_LEFTSHIFT, uinput.KEY_P],

    # home row capitals
    0x41: [uinput.KEY_LEFTSHIFT, uinput.KEY_A],
    0x53: [uinput.KEY_LEFTSHIFT, uinput.KEY_S],
    0x44: [uinput.KEY_LEFTSHIFT, uinput.KEY_D],
    0x46: [uinput.KEY_LEFTSHIFT, uinput.KEY_F],
    0x47: [uinput.KEY_LEFTSHIFT, uinput.KEY_G],
    0x48: [uinput.KEY_LEFTSHIFT, uinput.KEY_H],
    0x4A: [uinput.KEY_LEFTSHIFT, uinput.KEY_J],
    0x4B: [uinput.KEY_LEFTSHIFT, uinput.KEY_K],
    0x4C: [uinput.KEY_LEFTSHIFT, uinput.KEY_L],

    # bottom row capitals
    0x5A: [uinput.KEY_LEFTSHIFT, uinput.KEY_Z],
    0x58: [uinput.KEY_LEFTSHIFT, uinput.KEY_X],
    0x43: [uinput.KEY_LEFTSHIFT, uinput.KEY_C],
    0x56: [uinput.KEY_LEFTSHIFT, uinput.KEY_V],
    0x42: [uinput.KEY_LEFTSHIFT, uinput.KEY_B],
    0x4E: [uinput.KEY_LEFTSHIFT, uinput.KEY_N],
    0x4D: [uinput.KEY_LEFTSHIFT, uinput.KEY_M],
}