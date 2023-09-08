
# python-anopi
## General
### Raspberry Pi 4-20mA, 0-10V analog input 
Experience the versatility and efficiency of industrial sensor connectivity with our Raspberry Pi Shield. With the ability to read both 4-20mA and 0-10V analog inputs through a single interface, monitoring and control have never been simpler. Plus, our included open-source Python library gives you the power to customize and automate your sensor interactions to fit your specific needs. Upgrade your IoT setup today with the ultimate Raspberry Pi Shield for industrial sensor interfacing
### https://shop.frappgmbh.de/AnoPi-Raspberry-Header
## Installation
```
pip install python-anopi
```
## Get started
### The most important thing is, that you need to activate I2C on Raspberry Pi
For further Information have a look at that link
https://www.raspberrypi-spy.co.uk/2014/11/enabling-the-i2c-interface-on-the-raspberry-pi/

## Usage
### Read analog input current loop e.g. (4 - 20mA)
This code example is for the usage of a current loop sensor. The sensor offset can range from 0-3.
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
In most applications current loop representing a scale from a sensor e.g., a level meter for a tank.
For this application we provided a simple function which lets you scale your measurements

```
from python_anopi import AnoPi
from python_anopi import AnalogInputType 

a = AnoPi()

value, err = a.ai_V(0) # For Analog Input 0

value, err = a.scale_value(AnalogInputType.mA_4_20, value, min=0, max=100)

print('level: {value}% '.format(value=value))
```
## Electrical wiring
### !!!Warning!!! Industrial level voltages and currents can be hazardous, only assemble this if you are a trained expert and know what you are doing.

### Current loop
![current loop wiring](/examples/wiring/Anschluss_Stromschleife.PNG)

### Voltage measurement 

![Voltage measurement  wiring](/examples/wiring/Anschluss_Spannungspegel.PNG)

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

## Contact

info@frappgmbh.de

Project Link: [https://github.com/AndreasScharf/python-anopi](https://github.com/AndreasScharf/python-anopi)

<p align="right">(<a href="#top">back to top</a>)</p>

