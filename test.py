from python_anopi import AnoPi
from python_anopi import AnalogInputType as AIT


# a = AnoPi(adresses=[0x46, 0x47, 0x4A, 0x48, 0x4B, 0x49])
a = AnoPi()

for i in range(4):
    
    
    raw_value, err = a.ai_mA(i)
    value, err = a.scale_value(AIT.mA_0_20, raw_value, 0, 100)
    print('AI {index}: {raw_value}mA {value}'.format(index=i, raw_value=raw_value, value=value))
    value, err = a.ai_V(i)
    print('AI {index}: {value}V \n'.format(index=i, value=value))


