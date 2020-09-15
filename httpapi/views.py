'''
Author: Shi
Date: 2020-09-14 22:36:01
LastEditTime: 2020-09-14 22:41:45
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \IOTServer\httpapi\views.py
'''
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpRequest
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from . import apps 
from django.conf import settings
# Create your views here.

STATE='FIRST'

@csrf_exempt
def switch(request):
    switch_res={
        "status":"",
        "date":datetime.now()
    }
    print('method:'+request.method)
    print('body:'+request.body.decode())
    global STATE
    if request.method=='POST':
        if request.body.decode()=='':
            switch_res['status']="none"
            print("ERROR: NULL BODY")
        else:
            body=eval(request.body)
            if "action" in body.keys():
                action=body['action']
            else:
                action=''
            if action=='on':
                STATE='on'
                switch_res['status']=STATE
                print("POST ON SUCCESS")
            elif action=='off':
                STATE='off'
                switch_res['status']=STATE
                print("POST OFF SUCCESS")
            else:
                switch_res['status']="none"
                print("ERROR: NONE ACTION")
    switch_res['date']=datetime.now()
    return JsonResponse(switch_res)

@csrf_exempt
def get_status(request):
    status_res={
        "status":STATE
    }
    print('method:'+request.method)
    print('body:'+request.body.decode())
    if request.method=='GET':
        return JsonResponse(status_res)
    else:
        status_res['status']="none"
        return JsonResponse(status_res)
        

