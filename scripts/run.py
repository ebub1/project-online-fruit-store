#!/usr/bin/env python3
import os
import requests

#The path leading to folder with files and upload url
path = "supplier-data/descriptions/"
list_files = os.listdir(path)
url = "http://34.67.228.205/fruits/"
#Open txt file, convert to json and upload it 
for file_name in list_files:
    #Declare dictionary to store info from txt file
    descr = {}
    with open(path+file_name, "r") as file:
        #open txt file and take necessary info
        lines = file.readlines()
        descr['name'] = lines[0].strip()
        descr['weight'] = int(''.join(filter(str.isdigit, lines[1])))
        descr['description'] = lines[2].strip()
        descr['image_name'] = file_name[:3]+".jpeg"
    #upload info from dict as json file
    r = requests.post(url, descr, "application/json")
    print ("Response code for ", path+file," is ",  r.status_code)

