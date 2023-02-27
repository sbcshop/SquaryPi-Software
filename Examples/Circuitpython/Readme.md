### Working with CircuitPython
### Display Images using Circuit Python

To start working working with this ***Example code of circuit python***, you have to upload the firmware of circuit pyhton provide in this ***directory(Display Images)***. For how to uplaod firmware [click here](https://shop.sb-components.co.uk/blogs/posts/getting-started-with-python-micro-pythonP) for ***quick guidance of circuit pyhton.***

* After uploading firmware you will see your board as flash drive in your computer system.

Now, open the folder Display_Images, inside this folder their is sub-folder one is ***picture_display.py from PC and another one is Display images from SDCard*** folder inside this folder their is a file ***display_image_sdcard_circuitpython.py*** save or run this file for display images.

 * **Display Images from PC** -> For display images in EncroPi we use CircuitPython because it is very easy, it is developed by adafruit industries, First of all, we need to insert the circuit python to the roundypi(it is circuit python firmware "adafruit-circuitpython-raspberry_pi_pico-en_US-7.1.1.uf2").   
You can also display your custom images, for this you need to go "images" folder and save your images by changing its formate and resolution according to lcd display.
You can online convert any image to BMP image (the size must be 240x240), i a website below(there are various website)
https://image.online-convert.com/convert-to-bmp
Now, you need to run the python code file provided in this folder (i.e, images_display.py).
    
  * **Display Images From SD Card** -> For this, we need to insert the circuit python to the roundypi(it is circuit python firmware "adafruit-circuitpython-raspberry_pi_pico-en_US-7.1.1.uf2"). 
 Now, follow all the process of **Display Images from PC**,you only have to simply save the images containing in this directory (Do not save images in any directory when storing in SDCard). Finally, run the python code provided in this directory (i.e, display_image_sdcard_circuitpython.py)

Note - All liberary file dhould be saved in Lib folder of Circuit python.
