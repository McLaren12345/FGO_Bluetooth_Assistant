# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 10:37:11 2019

@author: McLaren
"""


import serial
import time
 
ser = serial.Serial()

def port_open(port_no):
    ser.port = port_no      #设置端口号
    ser.baudrate = 9600     #设置波特率
    ser.bytesize = 8        #设置数据位
    ser.stopbits = 1        #设置停止位
    ser.parity = "N"        #设置校验位
                            
    if(ser.isOpen()):
        print("串口已经打开")
    else: 
        ser.open()          #打开串口,要找到对的串口号才会成功
        if(ser.isOpen()):
            print("串口打开成功")
        else:
            print("串口打开失败")
        
 
def port_close():
    ser.close()
    if (ser.isOpen()):
        print("串口关闭失败")
    else:
        print("串口关闭成功")
 
def send(Position0,Position1):
    if (ser.isOpen()):
        Position0=round(Position0*100/1080)
        Position1=round(Position1*100/607)
        if Position0<16:
            Position0 = '0'+hex(Position0)[2:]
        else:
            Position0 = hex(Position0)[2:]
        if Position1<16:
            Position1 = '0'+hex(Position1)[2:]
        else:
            Position1 = hex(Position1)[2:]    
            
        send_data = Position0+Position1+'FF'
        #ser.write(send_data.encode('utf-8'))  #utf-8 编码发送
        ser.write(bytes.fromhex(send_data))  #Hex发送
        #print("发送成功",send_data)
    else:
        print("发送失败",'像素位置：{}%,{}%'.format(round(Position0*100/1080),round(Position1*100/607)))
    wait_for_flag()

def wait_for_flag():
    time.sleep(1)     #sleep() 与 inWaiting() 最好配对使用
    num=ser.inWaiting()
    torient_time = 0
    while True:
        torient_time+=1
        if (ser.read(num)==b'\xff')or(torient_time==25):
            break
        else:
            time.sleep(1)
            num=ser.inWaiting()
    #time.sleep(1)
#bytes.fromhex(hex(99)[2:])

xy_old=(0,0)    #投屏界面的像素位置(1080,607)

def mouse_click():
    ser.write(serial.to_bytes([0x08, 0x00, 0xA1, 0x02, 1, 0, 0, 0]))
    ser.write(serial.to_bytes([0x08, 0x00, 0xA1, 0x02, 0, 0, 0, 0]))
    time.sleep(0.3)

def mouse_hold():
    ser.write(serial.to_bytes([0x08, 0x00, 0xA1, 0x02, 1, 0, 0, 0]))
    time.sleep(0.3)
    
def mouse_release():
    ser.write(serial.to_bytes([0x08, 0x00, 0xA1, 0x02, 0, 0, 0, 0]))
    time.sleep(0.3) 
    
def mouse_set_zero():
    global xy_old
    for i in range(6):
        ser.write(serial.to_bytes([0x08, 0x00, 0xA1, 0x02, 0, 128, 128, 0]))
    xy_old=(0,0)
#    ser.write(serial.to_bytes([0x08, 0x00, 0xA1, 0x02, 0, 0, 127, 0]))
#    ser.write(serial.to_bytes([0x08, 0x00, 0xA1, 0x02, 0, 0, 68, 0]))

def mouse_swipe(From,To,delay=0.1):
    mouse_move(From,key=0)
    mouse_hold()
    time.sleep(1.5)
    mouse_move(To,key=1)
    time.sleep(delay)
    mouse_release()
    
def mouse_move(xy_new,key=0):
    global xy_old
    dx = round((xy_new[0]-xy_old[0])/1080*122/20.8*127)
    dy = round((xy_new[1]-xy_old[1])/607*68/11.5*127)
    X = list()
    Y = list()
    if dx > 0:
        # 向着X正方向移动
        max = 127
        cyc_x = dx//max
        mod_x = dx%max
        for i in range(0, cyc_x):
            X.append(max)
        if mod_x != 0:
            X.append(mod_x)
    else:
        # 向着X负方向移动
        dx = -dx
        max = 127
        cyc_x = dx//max
        mod_x = dx%max
        for i in range(0, cyc_x):
            X.append(256 - max)
        if mod_x != 0:
            X.append(256 - mod_x)
    if dy > 0:
        # 向着Y正方向移动
        max = 127
        cyc_y = dy // max
        mod_y = dy % max
        for i in range(0, cyc_y):
            Y.append(max)
        if mod_y != 0:
            Y.append(mod_y)
    else:
        # 向着Y负方向移动
        dy = -dy
        max = 127
        cyc_y = dy // max
        mod_y = dy % max
        for i in range(0, cyc_y):
            Y.append(256 - max)
        if mod_y != 0:
            Y.append(256 - mod_y)

    if len(X) > len(Y):
        for i in range(len(X) - len(Y)):
            Y.append(0)
    elif len(Y) > len(X):
        for i in range(len(Y) - len(X)):
            X.append(0)

    for i in range(len(X)):
        ser.write(serial.to_bytes([0x08, 0x00, 0xA1, 0x02, key, X[i], Y[i], 0]))
    time.sleep(0.3)
    xy_old = xy_new


def touch(X_Position,Y_Position,times=1):
    if(ser.isOpen()):
        for i in range(times):
             mouse_move((X_Position,Y_Position))
             mouse_click()       
    else:
        print("发送失败，串口未打开")
