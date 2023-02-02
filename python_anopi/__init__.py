from ina219 import INA219
from ina219 import DeviceRangeError
from enum import Enum
import RPi.GPIO as GPIO

"""
python-anopi.

A python library for AnoPi Hat.
"""

__version__ = "0.1.0"
__author__ = 'Andreas Scharf'
__credits__ = 'frapp GmbH'

class AnalogInputType(Enum):
    mA_4_20 = 1
    mA_0_20 = 2
    v_0_10 = 3
    
class AnoPi(object):
    def __init__(self ):
        self.ohm_shunt = 0.5  # standardwert für den eingebauten Shunt, später dann 0.5 Ohm
        max_current = 0.1
        
        #error Messages
        self.e_msg_anopi = 'Err: No AnoPi Hat attached'
        self.e_msg_index = 'Err: Index out of Range'
        self.e_msg_current_loop = 'Err: current loop interrupted'
        
        self.inas = []
        for i in range(4):
            offset = i
            if offset >= 2:
                offset = offset + 2
            try:
                ina = INA219(self.ohm_shunt, max_current, busnum=1, address=(0x40 + offset))
                ina.configure(ina.RANGE_32V, ina.GAIN_AUTO)
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
        if 0 > index < 4:
            return (None, self.e_msg_index)
        if not len(self.inas):
            return (None, self.e_msg_anopi)

        return (self.inas[index].current(), None)
    def ai_V(self, index):
        if 0 > index < 4:
            return (None, self.e_msg_index)
        if not len(self.inas):
            return (None, self.e_msg_anopi)

        return (self.inas[index].voltage(), None)
    
    def scale_value(self, input_type, value, min, max):
        print(input_type)
        a = 4
        b = 20
        if input_type == AnalogInputType.mA_4_20 and value < a * 0.9:
            return (None, self.e_msg_current_loop)
        
        if input_type == AnalogInputType.mA_0_20:
            a = 0
        elif input_type == AnalogInputType.v_0_10:
            a = 0
            b = 10
        
        m = (max - min) / (b - a)
        t = min - m * a
        
        return (value * m + t, None)