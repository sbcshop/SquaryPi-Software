#Receiver code
import utime
from machine import Pin, UART,SPI,ADC
import time
import st7789
import vga1_8x16 as font1
import vga2_8x8 as font
import vga1_16x32 as font
import vga1_16x16 as font2

battery = machine.ADC(26)

spi = SPI(1, baudrate=40000000, sck=Pin(10), mosi=Pin(11))
tft = st7789.ST7789(spi,240,240,reset=Pin(12, Pin.OUT),cs=Pin(9, Pin.OUT),dc=Pin(8, Pin.OUT),backlight=Pin(13, Pin.OUT),rotation=1)

def info():
    tft.init()
    utime.sleep(0.2)
    tft.text(font,"SB-COMPONENTS", 0,0)
    tft.fill_rect(0, 40, 210,10, st7789.RED)
    
    tft.text(font,"SQUARYPI", 0,55,st7789.YELLOW)
    tft.text(font,"BATTERY", 0,110,st7789.YELLOW)
    tft.text(font,"MEASURE", 0,150,st7789.YELLOW)
    tft.fill_rect(0, 90, 210, 10, st7789.BLUE)
    time.sleep(1)
    tft.fill(0) #clear screen
     
info()

def _map(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

while True:
    potreading = battery.read_u16()
    
    potreading = potreading * 3.3 / 65535
    potreading = round(potreading, 2) # Keep only 2 digits
    potreading = potreading*2
    print("potADC: ",potreading)
    batt_per = str(_map(potreading, 2.75, 4.2, 0, 100))
    tft.text(font,str(potreading)+'V', 75,50,st7789.YELLOW)
    tft.text(font,batt_per+'%', 75,100,st7789.GREEN)
    time.sleep(0.05)
    tft.text(font,str(potreading)+'V', 75,50,st7789.BLACK)
    tft.text(font,batt_per+'%', 75,100,st7789.BLACK)
    time.sleep(0.05)
    