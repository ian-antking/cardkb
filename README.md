# Raspberry Pi Card Keyboard

A script for using the M5Stack CardKB with Raspberry Pi

## Setting your pi to us layout

In order for buttons to return the correct symbols, the keyboard layout will need to be set to us on your Pi. You can do this by running:

```bash
sudo nano /etc/default/keyboard
```

and changing `XKBLAYOUT` to `us`:

```ini

# KEYBOARD CONFIGURATION FILE

# Consult the keyboard(5) manual page.

XKBMODEL="pc105"
XKBLAYOUT="us"
XKBVARIANT=""
XKBOPTIONS=""

BACKSPACE="guess"
```

## Enable I²C

The cardKB communicates over I²C, make sure this is enabled on your raspberry pi. You can find a tutorial on how to do so [here](https://www.raspberrypi-spy.co.uk/2014/11/enabling-the-i2c-interface-on-the-raspberry-pi/).

## Connect CardKB to Raspberry Pi

Connect the wires on the CardKB JST connector to the appropriate pin on the Raspberry Pi. 

![CardKB/Raspberry Pi I²C connection](https://github.com/ian-antking/cardkb/blob/master/docs/wiring.png?raw=true)

You may need to improvise a connection solution with breadboard wires like so:

![Assembled a raspberry pi and hyperpixel](https://github.com/ian-antking/cardkb/blob/master/docs/assembled-pi-keyboard.jpg?raw=true)

## Load the uinput module

You will need to load the uinput module to allow python-uinput to input key presses. You can check if it is loaded with:

```bash
lsmod | grep uinput
```

If nothing is displayed, then the module is not loaded. To load the module, run:

```bash
modprobe uinput
```

To load the module automatically on startup, run:

```bash
sudo nano /etc/modules
```
add `uinput` at the bottom of the file. Save and then reboot.

## Install CardKB via PyPI

```bash
sudo apt update
sudo apt install python3-smbus python3-uinput python3-pip
sudo pip install --break-system-packages cardkb
```

## Test CardKB

```bash
sudo cardkb &
```

> [!IMPORTANT]  
> By default, the python script listens to `/dev/i2c-1`, you can change this by adding an argument to the start command.
> `sudo cardkb 11 &`

## Running CardKB when Raspberry Pi starts

We can use systemd to run the CardKB script as a service. To do so, you can use the `cardkb.service` from source code:

```bash
sudo curl -L -o /etc/systemd/system/cardkb.service https://raw.githubusercontent.com/ian-antking/cardkb/main/cardkb.service
```

> [!IMPORTANT]  
> If you are running cardkb on a i2c bus other than 1, then you will need to edit the `cardkb.service` file to add the bus number to the end of the `ExecStart` line like so:
> `ExecStart=/usr/local/bin/cardkb 11`

```bash
sudo systemctl daemon-reload
sudo systemctl enable cardkb.service
sudo reboot
```

When your Pi restarts, your cardkb should be working, allowing you to log in.
