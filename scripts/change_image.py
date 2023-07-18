#!/usr/bin/env python3

from PIL import Image
import os

#The path leading to folder with files 
path = "supplier-data/images/"
list_images = os.listdir(path)
#Open image and change size and format
for file in list_images:
    #Use try-except to formate only image file
    try:
        #Open image file in order to change size and format
        im = Image.open(path+file)
        #print (im.format, im.size) 
        os.remove(path+file)
        im.convert("RGB").resize((600, 400)).save(path+file[:3]+'.jpeg', "JPEG")
        print ("Save file: ", path+file[:3]+".jpg")
    except Exception as e:
        #The message should appears if file is not image 
        print ("Error: ",path+file, type(e))



