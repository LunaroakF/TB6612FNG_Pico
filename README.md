# TB6612FNG_PicoW
micropython TB6612FNG motor controller for Raspberry Pi PicoW  
为树莓派picoW使用micropython编写的TB6612电机驱动板驱动程序  
## Example
```python
from TB6612FNG_PicoW import TB6612FNG
Abin1 = 13
Abin2 = 14
Apwm = 15
Bbin1 = 11
Bbin2 = 10
Bpwm = 9
Stay = 12
FNG = TB6612FNG(Abin1,Abin2,Apwm,Bbin1,Bbin2,Bpwm,1,Stay,1000)# TB6612电机驱动 1 = forwards -1 = backwards defaultfrequency = 1000
FNG.drive(50)#0~100
```
