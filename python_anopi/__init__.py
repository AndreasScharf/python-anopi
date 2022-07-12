from ina219 import INA219
from ina219 import DeviceRangeError
from enum import Enum

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
                ina = INA219(self.ohm_shunt, max_current, None, address=(0x40 + offset))
                ina.configure(ina.RANGE_32V, ina.GAIN_AUTO)
                self.inas.append(ina)
            except:
                print(self.e_msg_anopi)
        
            
        
    def ai_mA(self, index):
        if 0 > index < 4:
            return (None, self.e_msg_index)
        if not len(self.inas):
            return (None, self.e_msg_anopi)

        return (self.inas[index].voltage(), None)
    def ai_V(self, index):
        if 0 > index < 4:
            return (None, self.e_msg_index)
        if not len(self.inas):
            return (None, self.e_msg_anopi)

        return (self.inas[index].voltage(), None)
    
    def scale_value(self, input_type, value, min, max):
        a = 4
        b = 20
        if input_type == 2:
            a = 0
        elif input_type == 3:
            a = 0
            b = 10
        
        m = (max - min) / (b - a)
        t = min - m * a
        
        return value * m + t