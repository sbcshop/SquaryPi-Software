from machine import Pin, SPI
from Lib_SquaryPi import accelerometer
import st7789
import vga1_bold_16x32 as font
import time 

axi = accelerometer()
axi.initialize()
spi = SPI(1, baudrate=40000000, sck=Pin(10), mosi=Pin(11))
tft = st7789.ST7789(spi,240,240,reset=Pin(12, Pin.OUT),cs=Pin(9, Pin.OUT),dc=Pin(8, Pin.OUT),backlight=Pin(13, Pin.OUT),rotation=1)#SPI interface for tft screen

SENSITIVITY = 5

def info():
    tft.init()
    time.sleep(0.5)#time delay
   
    tft.text(font,"SQUARY-PI", 10,10,st7789.YELLOW)# print on tft screen
    tft.fill_rect(0, 50, 240,10, st7789.RED)#display red line on tft screen
    
    tft.text(font,"ACCELEROMETER", 10,70 ,st7789.GREEN)
    tft.fill_rect(0, 105, 240,10, st7789.RED)

info()
time.sleep(2)

tft.fill(0)

while True:
    x = int(axi.read_x()/2)
    y = int(axi.read_y()/2)
    z = int(axi.read_z()/2)
    print(x, y, z)
    time.sleep(0.05)
    
    if x >= 700 and x <= 2300:
        tft.fill(0)
        #tft.text(font,"Tilting Left", 30,60,st7789.RED)
        tft.fill_rect(30, 100, 40, 40, st7789.RED)
        print(x)
        print("Tilting Left")
        time.sleep(0.05)
        
    elif x <=250:
        tft.fill(0)
        #tft.text(font,"Tilting Right", 30,60,st7789.RED)
        tft.fill_rect(200, 100, 40, 40, st7789.RED)
        print("Tilting Right")
        time.sleep(0.05)
    elif y >= 700:
        tft.fill(0)
        #tft.text(font,"Tilting Frunt", 10,90,st7789.RED)
        tft.fill_rect(100, 0, 40, 40, st7789.RED)
        print(y)
        print("Tilting Forward")
        time.sleep(0.05)
        
    elif y <=550:
        print("Tilting Backward")
        #tft.text(font,"Tilting Back", 10,90,st7789.RED)
        tft.fill(0)
        tft.fill_rect(100, 200, 40, 40, st7789.RED)
        time.sleep(0.05)
    else:
         print("")
         tft.fill(0)
         print("Please tilt")
         tft.text(font,"Tilt Please", 10,90,st7789.RED)
        #tft.fill(0)
        #tft.fill_rect(100, 200, 40, 40, st7789.RED)
         time.sleep(0.05)
