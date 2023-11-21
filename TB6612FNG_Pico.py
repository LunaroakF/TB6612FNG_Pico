import machine
import time

#for Raspberry Pi Pico by hehu
class TB6612FNG:
    def __init__(self, Ain1Pin, Ain2Pin, ApwmPin, Bin1Pin, Bin2Pin, BpwmPin, towards, stbyPin, defaultFREQUENCY):
        #定义引脚特殊注释:towards为1或-1改变行驶方向，defaultFREQUENCY为默认频率
        if towards == -1:
            self.towards = -1
        else:
            self.towards = 1
        #定义目标输出引脚输出
        self.Ain1 = machine.Pin(Ain1Pin, machine.Pin.OUT)
        self.Ain2 = machine.Pin(Ain2Pin, machine.Pin.OUT)
        self.Bin1 = machine.Pin(Bin1Pin, machine.Pin.OUT)
        self.Bin2 = machine.Pin(Bin2Pin, machine.Pin.OUT)
        self.stby = machine.Pin(stbyPin, machine.Pin.OUT)
        self.Apwm = machine.PWM(machine.Pin(ApwmPin))
        self.Bpwm = machine.PWM(machine.Pin(BpwmPin))
        self.Apwm.freq(defaultFREQUENCY)
        self.Bpwm.freq(defaultFREQUENCY)
        self.Apwm.duty_u16(0)#MAX = 65535
        self.Bpwm.duty_u16(0)#duty = 65535*i/100
        
    def drive(self, speed):
        if speed > 100:
            speed = 100
        elif speed < -100:
            speed = -100
        self.stby.on()
        speed = speed * self.towards
        if speed >= 0:
            self.A_forward(abs(speed))
            self.B_forward(abs(speed))
        else:
            self.A_backward(abs(speed))
            self.B_backward(abs(speed))

    def brake(self):
        self.Bin1.on()
        self.Bin2.on()
        self.Ain1.on()
        self.Ain2.on()
        self.Apwm.duty_u16(0)
        self.Bpwm.duty_u16(0)
        
    def standby(self):
        self.stby.off()

    def A_brake(self):
        self.Ain1.on()
        self.Ain2.on()
        self.Apwm.duty_u16(0)
    
    def B_brake(self):
        self.Bin1.on()
        self.Bin2.on()
        self.Bpwm.duty_u16(0)
    
    def A_forward(self, speed):
        self.Ain1.on()
        self.Ain2.off()
        self.Apwm.duty_u16(int(65535*speed/100))
    
    def A_backward(self, speed):
        self.Ain1.off()
        self.Ain2.on()
        self.Apwm.duty_u16(int(65535*speed/100))

    def B_forward(self, speed):
        self.Bin1.on()
        self.Bin2.off()
        self.Bpwm.duty_u16(int(65535*speed/100))
    
    def B_backward(self, speed):
        self.Bin1.off()
        self.Bin2.on()
        self.Bpwm.duty_u16(int(65535*speed/100))
    
    def __del__(self):
        self.standby()
        self.Apwm.duty_u16(0)
        self.Bpwm.duty_u16(0)
    


