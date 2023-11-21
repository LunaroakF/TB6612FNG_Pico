# TB6612FNG_Pico
micropython TB6612FNG motor controller for Raspberry Pi Pico  
为树莓派pico使用micropython编写的TB6612电机驱动板驱动程序  
经测试该驱动可在Pico与PicoW上运行，其他的没有测试我不太清楚  
## Example
```python
from TB6612FNG_Pico import TB6612FNG

Abin1 = 13
Abin2 = 14
Apwm = 15
Bbin1 = 11
Bbin2 = 10
Bpwm = 9
Stay = 12
towards = 1 #"1" to forward & "-1" to backward
defaultfrequency = 1000

FNG = TB6612FNG(Abin1,Abin2,Apwm,Bbin1,Bbin2,Bpwm,towards,Stay,defaultfrequency)

FNG.drive(50)#0~100
```
