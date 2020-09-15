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
# Create your views here.

@csrf_exempt
def switch(request):
    switch_res={
        "status":"",
        "date":datetime.now()
    }
    print('method:'+request.method)
    print('body:'+request.body.decode())
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
                switch_res['status']='on'
                print("POST ON SUCCESS")
            elif action=='off':
                switch_res['status']='off'
                print("POST OFF SUCCESS")
            else:
                switch_res['status']="none"
                print("ERROR: NONE ACTION")
    switch_res['date']=datetime.now()
    return JsonResponse(switch_res)

