#!/usr/bin/env python3

import requests
import os
from PIL import Image

#The path leading to folder with files and upload url
path = "supplier-data/images/"
list_images = os.listdir(path)
url = "http://localhost/upload/"
#
for file in list_images:
    #Try to open image file and upload it
    try:
        im = Image.open(path+file)
        with open(path+file, 'rb') as opened_file:
            r = requests.post(url, files={'file': opened_file})
        print ("Response code for ", path+file," is ",  r.status_code)
    except Exception as e:
        #The message should appears if file is not image 
        print ("Error: ",path+file, type(e))
