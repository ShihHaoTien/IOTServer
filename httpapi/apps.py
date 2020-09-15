'''
Author: your name
Date: 2020-09-14 22:36:01
LastEditTime: 2020-09-14 22:37:13
LastEditors: your name
Description: In User Settings Edit
FilePath: \IOTServer\httpapi\apps.py
'''
from django.apps import AppConfig


class HttpapiConfig(AppConfig):
    name = 'httpapi'


import os

#两数相加
def add(x,y):
    return x+y