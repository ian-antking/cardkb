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

## Install Software

Install smbus and python-uinput:

```bash
sudo apt install python3-smbus
```

```bash
sudo pip3 install python-uinput
```

clone this repository:

```
git clone https://github.com/ian-antking/cardkb.git
```

Run the script and check buttons return expected characters:

```bash
sudo python3 cardkb &
```

By default, the python script listens to `/dev/i2c-1`, you can change this by adding an argument to the start command.

```bash
sudo python3 cardkb 11 &
```

## Running CardKB when Raspberry Pi starts

We can use systemd to run the CardKB script as a service. To do so, create a unit file:

```bash
sudo nano /lib/systemd/system/cardkb.service
```

Add the following:

```
[Unit]
Description=Service for using CardKB with Raspberry Pi
After=multi-user.target

[Service]
Type=idle
ExecStart=/usr/bin/python3 /home/pi/cardkb

[Install]
WantedBy=multi-user.target
```

This service file assumes that you have cloned the cardkb repo to /home/pi. If this is not the case, you will need to change the file path. 

```
...
ExecStart=/usr/bin/python3 /home/ian/cardkb
...
```

Likewise, if you are running cardkb on a i2c bus other than one, then you will need to add the bus number to the end of the `ExecStart` line like so:

```
...
ExecStart=/usr/bin/python3 /home/pi/cardkb 11
...
```

Save the file and exit. Now run the following commands to reload the systemctl daemon, enable the cardkb service and restart the pi:

```bash
sudo systemctl daemon-reload
sudo systemctl enable cardkb.service
sudo reboot
```

When your Pi restarts, your cardkb should be working, allowing you to log in.


