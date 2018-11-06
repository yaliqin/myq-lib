#   this file is a file to test method in MyQAPI.py
#! /usr/bin/env python3
from MyQAPI import MyQAPI
from constants import Const
import time
from SendEmail import send_mail

r= MyQAPI()
r.usr="my_user_email"
r.pwd="my_password"
doorOpenCnt = [0,0]
longTime =3

r.login()

starttime=time.time()
while True:
    doorInfo=r.get_door_info() #doorInfo consists id,name,state
    for index in range(len(doorInfo)):
        if doorInfo[index][2]==Const.doorState['DoorOpen']:
            doorOpenCnt[index] += 1
            print (index, doorOpenCnt[index])
        else:
            doorOpenCnt[index] = 0
        if doorOpenCnt[index] > longTime:
            print(doorInfo[index][1],"is open",doorOpenCnt[index],"minutes")
            send_mail(longTime)
            resp= r.setDeviceState('desireddoorstate',Const.doorState['DoorClose'],Const.doorName[doorInfo[index][1]])
            print(resp)
    time.sleep(60.0 - ((time.time() - starttime) % 60.0))



