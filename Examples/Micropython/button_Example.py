#Transmiter code
import time
from machine import Pin

gp22 = machine.Pin(22, machine.Pin.OUT)
gp23 = machine.Pin(23, machine.Pin.OUT)
gp24 = machine.Pin(25, machine.Pin.OUT)

gp22.value(1)
gp23.value(1)
gp24.value(1)

button1 = Pin(22, Pin.IN, Pin.PULL_UP) 
button2 = Pin(23, Pin.IN, Pin.PULL_UP)
button3 = Pin(24, Pin.IN, Pin.PULL_UP)

        
while 1:
    val1 = button1.value()
    val2 = button2.value()
    val3 = button3.value()
    print("val1 = ",val1)
    print("val2 = ",val2)
    print("val3 = ",val3)
    time.sleep(0.2)


