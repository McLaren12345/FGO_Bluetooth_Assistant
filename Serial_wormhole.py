# -*- coding: utf-8 -*-
"""
Created on Sun May 16 12:32:19 2021

@author: McLaren
"""

import sys
import win32con, win32api
import time
sys.path.append(r'D:\Software\FGO_Project') 
import Base_func_wormhole as Base_func


xy_zero = (Base_func.global_position+21+Base_func.config[Base_func.phone]["bias"], 0+16)    
#投屏界面的像素位置(1080,607)

def port_open(port_no):
    pass

def port_close():
    pass

def mouse_click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
    time.sleep(0.15)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)
    time.sleep(0.15)

def mouse_hold():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
    time.sleep(0.3)
    
def mouse_release():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)
    time.sleep(0.3) 
    
def mouse_set_zero():
    win32api.SetCursorPos([xy_zero[0],xy_zero[1]])

def mouse_move(xy_new,key=0):
    win32api.SetCursorPos([xy_zero[0]+xy_new[0],xy_zero[1]+xy_new[1]])
    time.sleep(0.3)
    
def mouse_swipe(From,To,delay=0.1):
    mouse_move(From,key=0)
    mouse_hold()
    time.sleep(1.5)
    mouse_move(To,key=1)
    time.sleep(delay)
    mouse_release()

def touch(X_Position,Y_Position,times=1):
    for i in range(times):
        mouse_move((X_Position,Y_Position))
        mouse_click()       
