from python_anopi import AnoPi
from python_anopi import AnalogInputType as AIT
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

a = AnoPi()

for i in range(4):
    value, err = a.ai_mA(i)
    value = 4
    (value, err) = a.scale_value(AIT.mA_4_20, value, 0, 100)
    print('AI {index}: {value}mA'.format(index=i, value=value))
    value, err = a.ai_V(i)
    print('AI {index}: {value}V \n'.format(index=i, value=value))


GPIO.setup(a.pinDI0, GPIO.IN)
print(GPIO.input(a.pinDI0))