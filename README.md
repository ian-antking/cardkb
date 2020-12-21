# Raspberry Pi Card Keyboard

A script for using the M5Stack CardKB with Raspberry Pi

## Setting your pi to us layout

In order for buttons to return the correct symbols, the keyboard layout will need to be set to us on you pi. You can do this by running:

```bash
sudo nano /etc/default/keyboard
```

and changing `XKBLAYOUT` to `us`:

```
# KEYBOARD CONFIGURATION FILE

# Consult the keyboard(5) manual page.

XKBMODEL="pc105"
XKBLAYOUT="us"
XKBVARIANT=""
XKBOPTIONS=""

BACKSPACE="guess"
```

## Enable i2C
The cardKB communicates over i2C, make sure this is enabled on your raspberry pi. You can find a tutorial on how to do so [here](https://www.raspberrypi-spy.co.uk/2014/11/enabling-the-i2c-interface-on-the-raspberry-pi/).
