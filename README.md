
# python-anopi
## General
### This is a library for the implementation of the AnoPi Header in a python environment
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
This code example is for the usage of a current loop sensor. \nThe sensor offset can range from 0-3.
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
### Analog input scaling
In most applications current loop representing a scale from a sensor e.g. a level meter for a tank.
For these application we provided a simple function which let`s you scale your messurements

```
from python_anopi import AnoPi
from python_anopi import AnalogInputType 

a = AnoPi()

value, err = a.ai_V(0) # For Analog Input 0

value, err = a.scale_value(AnalogInputType.mA_4_20, value, min=0, max=100)

print('level: {value}% '.format(value=value))
```
## Electrical wiring
### !!!Warning!!! Industrial level voltages and currents can be hazardous, only assable this if you are a trained expert and know what you are doing.

