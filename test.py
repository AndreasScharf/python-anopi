from python_anopi import AnoPi
from python_anopi import AnalogInputType as AIT


a = AnoPi(adresses=[0x46, 0x47, 0x4A, 0x48, 0x4B, 0x49])

for i in range(4):
    
    
    value, err = a.ai_mA(i)
    #(value, err) = a.scale_value(AIT.mA_4_20, value, 0, 100)
    print('AI {index}: {value}mA'.format(index=i, value=value))
    value, err = a.ai_V(i)
    print('AI {index}: {value}V \n'.format(index=i, value=value))


