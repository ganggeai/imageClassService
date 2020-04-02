# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 18:25:00 2020

@author: gangge
"""

import requests

#read image file as binary data
data=0
with open('elephant1.jpg','br') as f:
    data =f.read()
print(len(data))
rsp=requests.post(url='http://localhost:5000/predict',data=data)
print(rsp.status_code)
print(rsp.content.decode())
