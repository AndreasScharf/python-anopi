from ina219 import INA219
from ina219 import DeviceRangeError
from enum import Enum
import RPi.GPIO as GPIO

"""
python-anopi.

A python library for AnoPi Hat.
"""

__version__ = "0.3.1"
__author__ = 'Andreas Scharf'
__credits__ = 'frapp GmbH'

class AnalogInputType(Enum):
    """
    Enumeration representing different types of analog input signals.

    Enum Values:
    - `mA_4_20` (int): Analog input signal in the range of 4-20 mA.
    - `mA_0_20` (int): Analog input signal in the range of 0-20 mA.
    - `v_0_10` (int): Analog input voltage signal in the range of 0-10 V.
    - `v_0_45` (int): Analog input voltage signal in the range of 0-4.5 V.

    Note:
    - These values are used to identify and distinguish different types of analog input signals.
    - The enum values are integers representing the unique identifier for each input type.

    Example:
    >>> input_type = AnalogInputType.mA_4_20
    >>> print(input_type.value)
    1

    Usage:
    - Use the enum values to specify the type of analog input when working with related functions or classes.
    - Enum values can be compared for equality or used in switch-like statements.

    """
    mA_4_20 = 1
    mA_0_20 = 2
    v_0_10 = 3
    v_0_45 = 4
    
class AnoPi(object):
    def __init__(self , adresses=[0x40, 0x41, 0x44, 0x45]):
        self.ohm_shunt = 0.5  # standardwert für den eingebauten Shunt, später dann 0.5 Ohm
        max_current = 0.08
        
        #error Messages
        self.e_msg_anopi = 'Err: No AnoPi Hat attached'
        self.e_msg_index = 'Err: Index out of Range'
        self.e_msg_current_loop = 'Err: current loop interrupted'
        self.e_msg_short_circuit = 'Error during measurement: Short circuit detected.'
        
        self.inas = []
        adresse_range = 4
        if adresses and len(adresses):  # only if i set my own adresses
            adresse_range = len(adresses)
            
            
        for i in range(adresse_range):
            offset = i
            if offset >= 2:
                offset = offset + 2
            try:
                if adresses: #only if i set my own adresses
                    ina = INA219(self.ohm_shunt, max_current, busnum=1, address=adresses[i])
                else:
                    ina = INA219(self.ohm_shunt, max_current, busnum=1, address=(0x40 + offset))
                ina.configure(ina.RANGE_16V, ina.GAIN_1_40MV)
                self.inas.append(ina)
            except Exception as e:
                print(e)
                print(self.e_msg_anopi)
                
        mode = GPIO.getmode()
        
        if mode == GPIO.BOARD:
            self.pinDI0 = 7
            self.pinDI1 = 11
            self.pinDI2 = 13
            self.pinDI3 = 15
        else:
            self.pinDI0 = 4
            self.pinDI1 = 17
            self.pinDI2 = 27
            self.pinDI3 = 22

        
    def ai_mA(self, index):
        """
        Retrieves the measured current in milliamperes (mA) from an analog input channel.

        Parameters:
        - index (int): The index of the analog input channel. Should be in the range [0, 3].

        Returns:
        tuple: A tuple containing the measured current value and an error message.
            - Measured Current (float): The measured current in milliamperes.
            - Error Message (str): Empty string if successful, or an error message if any issues occur during the measurement.

        Note:
        - The index parameter specifies which analog input channel to read.
        - The function returns a tuple containing the measured current value and an error message (if any).

        Examples:
        >>> value, err = ai_mA(0)
        >>> print(value)
        15.3
        >>> print(err)
        None

        >>> value, err = ai_mA(2)
        >>> print(value)
        None
        >>> print(err)
        'Error No AnoPi Hat attached.'

        >>> value, err = ai_mA(1)
        >>> print(value)
        None
        >>> print(err)
        'Error during measurement: Short circuit detected.'

        """
        if 0 > index < 4:
            return (None, self.e_msg_index)
        if not len(self.inas):
            return (None, self.e_msg_anopi)

        try:
            return (self.inas[index].current(), None)
        except:
            return (None, self.e_msg_short_circuit)
        
        
    def ai_V(self, index):
        if 0 > index < 4:
            return (None, self.e_msg_index)
        if not len(self.inas):
            return (None, self.e_msg_anopi)


        return (self.inas[index].voltage(), None)
    
    def scale_value(self, input_type, raw_value, min, max, cutoff=True):
        """
        Scales a raw analog input value based on the specified input type.

        Parameters:
        - input_type (AnalogInputType): The type of analog input, e.g., AnalogInputType.mA_4_20.
        - raw_value (float): The raw analog input value to be scaled.
        - min (float): The minimum scaled value. Defaults to 0.
        - max (float): The maximum scaled value. Defaults to 100.
        - cutofff (boolean, default = True): The scaled value is only between min and max

        Returns:
        tuple: A tuple containing the scaled value and an error message.
            - Scaled Value (float): The scaled output value between min_value and max_value.
            - Error Message (str): Empty string if successful, or an error message if any issues occur during scaling.

        Example:
        >>> value, err = scale_value(AnalogInputType.mA_4_20, 15.0, min=10, max=90)
        >>> print(value)
        50.0
        >>> print(err)
        ''

        Note:
        - The AnalogInputType enum is assumed to be defined and imported before using this function.
        - The function assumes linear scaling for simplicity.
        """
        
        a = 4
        b = 20
        if input_type == AnalogInputType.mA_4_20 and raw_value < a * 0.9:
            return (None, self.e_msg_current_loop)
        
        if input_type == AnalogInputType.mA_0_20:
            a = 0
        elif input_type == AnalogInputType.v_0_10:
            a = 0
            b = 10
        elif input_type == AnalogInputType.v_0_45:
            a = 0
            b = 4.5
        
        #calculate sensor linear scaling values
        m = (max - min) / (b - a)
        t = min - m * a
        
        #calculate measurement value
        calc = raw_value * m + t
        
        #check if messurement value is out of range
        if calc < min and cutoff:
            calc = min
        elif calc > max and cutoff:
            calc = max
            
        return (calc, None)