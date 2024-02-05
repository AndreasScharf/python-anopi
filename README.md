
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

### Function: scale_value

#### Description

The `scale_value` function is designed to scale raw analog input values based on the specified input type. This is useful when working with different types of analog sensors that provide input signals within specific ranges. The function utilizes an enum called `AnalogInputType` to define the input types. The scaling is performed linearly between a minimum and maximum scaled value.

#### Parameters

- `input_type` (AnalogInputType): The type of analog input signal, such as `AnalogInputType.mA_4_20`.
- `raw_value` (float): The raw analog input value to be scaled.
- `min` (float): The minimum scaled value. Defaults to 0.
- `max` (float): The maximum scaled value. Defaults to 100.
- `cutoff` (boolean, default=True): If set to True, the scaled value is constrained to be within the specified range (min to max).

### Returns

A tuple containing the scaled value and an error message:
- Scaled Value (float): The scaled output value between `min` and `max`.
- Error Message (str): An empty string if successful, or an error message if any issues occur during scaling.

#### Example

```python
from python_anopi import AnoPi, AnalogInputType

a = AnoPi()

# Example 1: Scaling a 4-20mA analog input
raw_value, err = a.ai_mA(0) # read analog input channel 0: 15mA
value, err = a.scale_value(AnalogInputType.mA_4_20, raw_value, min=10, max=90)
print(value)  # Output: 50.0
print(err)    # Output: None

# Example 2: Scaling a 0-20mA analog input with cutoff disabled
raw_value, err = a.ai_mA(1) # read analog input channel 1: 18mA
value, err = a.scale_value(AnalogInputType.mA_0_20, raw_value, min=0, max=100, cutoff=False)
print(value)  # Output: 90.0
print(err)    # Output: None
```


### Digital Input (9-30V) GPIO Pin Configurations

The Digital Input PINs can be used as normal GPIOs of the Raspberry Pi. Connect the DI0+ to the 9-30V Signal and DI0- to your GND.
Depending on the GPIO mode (`GPIO.BOARD` or `GPIO.BCM`), the digital input pins are configured as follows:

### GPIO.BOARD Mode:

- `pinDI0`: 7
- `pinDI1`: 11
- `pinDI2`: 13
- `pinDI3`: 15

### GPIO.BCM Mode:

- `pinDI0`: 4
- `pinDI1`: 17
- `pinDI2`: 27
- `pinDI3`: 22

## Example: Using Digital Input in GPIO.BOARD Mode

Here's an example of using the digital input `pinDI0` in `GPIO.BOARD` mode with the RPi.GPIO library:

```python
import RPi.GPIO as GPIO
from python_anopi import AnoPi

# Set up GPIO mode
GPIO.setmode(GPIO.BOARD)

a = AnoPi()
# Set up the pin for digital input
# Assuming you want to use pinDI0 in GPIO.BOARD mode
GPIO.setup(a.pinDI0, GPIO.IN)

# Example: Reading digital input
digital_input_value = GPIO.input(a.pinDI0)

print(digital_input_value) 

# Clean up GPIO settings
GPIO.cleanup()
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

