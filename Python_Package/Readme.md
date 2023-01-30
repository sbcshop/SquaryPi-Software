### Working with SquaryPi
Follow the steps below to start working with our SquaryPi board:

* Step.1 - Ater Downloading and extracting the Zip file the current repository in your computer system, locate the ***Python_Package*** directory and open it.
* step.2 - Now, you will see two folder, one is of Examples and 2nd is of Library folder.
* step.3 - Open the python files contains in both folder in ***Thonny IDE***.
* step.4 - Now, connect your board (updated firmware) via USB to your computer and save the library file as it is in RP2040 of your squaryPi board. If are working first time with Thonny and python files ***Please see our other documentation for how to handle python files in details*** or you can just [click here](https://shop.sb-components.co.uk/blogs/posts/getting-started-with-python-micro-python) for guidance of using circuit python and micropython.
* step.5 - After saving liberary file, open one of our Examples provided in it and run in by pressing Run button in Thonny.

**Note:** We have provide two example codes of Micropython one is of Tilt indication along X and Y axis another one is of Auisition of Accelrometer data to SD card.


### Display Images using Circuit Python

To start working working with this ***Example code of circuit python***, you have to upload the firmware of circuit pyhton provide in this ***directory(Display Images)***. For how to uplaod firmware [click here](https://shop.sb-components.co.uk/blogs/posts/getting-started-with-python-micro-pythonP) for ***quick guidance of circuit pyhton.***

* After uploading firmware you will see your board as flash drive in your computer system.

Now, open the folder Display_Images, inside this folder their is sub-folder one is ***Display_Images from PC and another one is Display images from SDCard*** folder.

 * **Display Images from PC** -> For display images in EncroPi we use CircuitPython because it is very easy, it is developed by adafruit industries, First of all, we need to insert the circuit python to the roundypi(it is circuit python firmware "adafruit-circuitpython-raspberry_pi_pico-en_US-7.1.1.uf2").   
You can also display your custom images, for this you need to go "images" folder and save your images by changing its formate and resolution according to lcd display.
You can online convert any image to BMP image (the size must be 240x240), i a website below(there are various website)
https://image.online-convert.com/convert-to-bmp
Now, you need to run the python code file provided in this folder (i.e, images_display.py).
    
  * **Display Images From SD Card** -> For this, we need to insert the circuit python to the roundypi(it is circuit python firmware "adafruit-circuitpython-raspberry_pi_pico-en_US-7.1.1.uf2"). 
 Now, follow all the process of **Display Images from PC**,you only have to simply save the images containing in this directory (Do not save images in any directory when storing in SDCard). Finally, run the python code provided in this directory (i.e, display_image_sdcard_circuitpython.py)


