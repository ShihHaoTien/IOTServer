'''
Author: your name
Date: 2020-09-15 15:06:03
LastEditTime: 2020-09-16 09:56:59
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \IOTClient\client.py
'''
#!usr/bin/python
# -*- coding: utf-8 -*-

import json
import requests
import time
'''
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(13, GPIO.OUT)
'''
while True:
    response = requests.get(url='http://175.24.28.177:8000/httpapi/get_status/', json={"type": "status"})
    status = json.loads(response.text).get('status')
    if "on" == status:
        print("status:" + status)
        #GPIO.output(13, True)  # 将GPIO13设置为高电平，点亮LED
    elif "off" == status:
        print("status:" + status)
        #GPIO.output(13, False)      # 将GPIO13设置为低电平，熄灭LED
    else:
        print("null")
    print(time.ctime())
    time.sleep(1)
