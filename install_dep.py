import json
import pip
import os

with open('dependancies.json') as json_data:
    d = json.load(json_data)
    for i in d:
    	print (i)
    	for package in d[i]:
    		version = d[i][package]
    		print ("installing"+package+"=="+version)
    		os.system("pip install " + package +"=="+version)
    		print("installed")
    		