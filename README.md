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

## Connect CardKB to Raspberry Pi

Connect the wires on the CardKB JST connector to the appropriate pin on the Raspberry Pi. 

![CardKB/Raspberry Pi i2C connection](https://github.com/ian-antking/cardkb/blob/master/docs/wiring.png?raw=true)

You may need to improvise a connection solution with breadboard wires like so:

![Assembled a raspberry pi and hyperpixel](https://github.com/ian-antking/cardkb/blob/master/docs/assembled-pi-keyboard.jpg?raw=true)
