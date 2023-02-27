### Working with CircuitPython
### Display Images using Circuit Python

<img src = "https://github.com/sbcshop/SquaryPi-Software/blob/main/images/imgpi.png"/>



* Install **CircuitPython** in SquaryPi
First, push the boot button, then connect the USB; do not release the button until the USB is connected to the laptop. Next you'll see a new gadget called "RPI-RP2." Drag the "firmware circuitpython.uf2" file to this device, as indicated in Figure:
     this is the official website, or yoy can download from here https://circuitpython.org/board/raspberry_pi_pico/
     <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img13.png" />  
     When you properly insert the circuitpython then you see a new device that looks like the below image:-
     <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img11.png" />
    
     After this go to run->select interpreter,choose device and port
         <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img18.png" />
         <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img19.png" />
         <img src= "https://github.com/sbcshop/RoundyPi/blob/main/images/img20.png" />
    

Now, enter the CircuitPython folder; within this folder, there are two sub-folders: ***Display pictures from PC*** and ***Display images from SDCard***. There is a file ***display image.py*** inside these folders that you may save or execute to display images (save as code.py to have the code run automatically when the power is turned on).

 * **Display Images from PC** -> For display images in EncroPi we use CircuitPython because it is very easy, it is developed by adafruit industries, First of all, we need to insert the circuit python to the roundypi(it is circuit python firmware "firmware_circuitpython.uf2").   
You can also display your custom images, for this you need to go "images" folder and save your images by changing its formate and resolution according to lcd display.
You can online convert any image to BMP image (the size must be 240x240), i a website below(there are various website)
https://image.online-convert.com/convert-to-bmp
Now, you need to run the python code file provided in this folder (i.e, images_display.py).
    
  * **Display Images From SD Card** -> For this, we need to insert the circuit python to the roundypi(it is circuit python firmware "firmware_circuitpython.uf2"). 
 Now, follow all the process of **Display Images from PC**,you only have to simply save the images containing in this directory (Do not save images in any directory when storing in SDCard). Finally, run the python code provided in this directory (i.e, display_image_sdcard_circuitpython.py)

Note - All liberary file dhould be saved in Lib folder of Circuit python.
