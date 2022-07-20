
# python-anopi
## General
### This is a library for the implementation of the AnpPi Header in a python environment
## Installation
```
pip install python-anopi
```
## Get started
### The most important thing is, that you need to activiate I2C on Raspberry Pi
For futher Information have a look at that link
https://www.raspberrypi-spy.co.uk/2014/11/enabling-the-i2c-interface-on-the-raspberry-pi/

## Usage
### Read analog input current loop e.g. (4 - 20mA)
```
from python_anopi import AnoPi

a = AnoPi()

value, err = a.ai_mA(0) # For Analog Input 0
print('AI 0: {value}mA'.format(value=value))

```
### Read analog input voltage e.g. (0 - 10V)
```
from python_anopi import AnoPi

a = AnoPi()

value, err = a.ai_V(0) # For Analog Input 0
print('AI 0: {value}V'.format(value=value))

```
