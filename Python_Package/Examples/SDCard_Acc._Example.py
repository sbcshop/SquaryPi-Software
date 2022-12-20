from machine import Pin, SPI
import os
from Lib_SquaryPi import accelerometer, SDCard
import st7789
import vga1_bold_16x32 as font
import time 

axi = accelerometer()
sd=SDCard()
axi.initialize()

x_axis = []        # the x, y, and z axis data is collected in 3 lists  
y_axis = []
z_axis = []

spi = SPI(1, baudrate=40000000, sck=Pin(10), mosi=Pin(11))
tft = st7789.ST7789(spi,240,240,reset=Pin(12, Pin.OUT),cs=Pin(9, Pin.OUT),dc=Pin(8, Pin.OUT),backlight=Pin(13, Pin.OUT),rotation=1)#SPI interface for tft screen

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

#while True:
x = str(axi.read_x()/2)
y = str(axi.read_y()/2)
z = str(axi.read_z()/2)

time.sleep(0.05)

x_axis.append(x)     # writing new value in each list
y_axis.append(y)
z_axis.append(z)


def file_exists(fname):
  try:
    with open(fname):
      pass
    return True
  except OSError:
     return False

sd=SDCard()
vfs = os.VfsFat(sd)
os.mount(vfs, "/fc")
print("Filesystem check")
print(os.listdir("/fc")) # check the files in sd card
fn = "/fc/Sensor_Read.txt"
print("Single block read/write")

#################################################

with open(fn, "a") as f:  # append data to file
    n = f.write("{} \n".format(x))
    n = f.write("{} \n".format(y))
    n = f.write("{} \n".format(z))
    f.close()
    print(n, "bytes written")
#################################################

#################################################
with open(fn, "r") as f:  # read data from file
    result = f.read()
    f.close()
    print(result)
    print(len(result), "bytes read")
os.umount("/fc")
#################################################
