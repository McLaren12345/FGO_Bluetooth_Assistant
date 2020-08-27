# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 20:17:33 2020

@author: McLaren
"""

import sys
sys.path.append(r'F:\FGO_Project') 
import Serial
import Base_func
import time

#无限池抽取函数
def InfinatePool():
    Serial.port_open('com5')
    Serial.mouse_set_zero()
    Serial.mouse_move((320,360))
    for i in range(100):
        Serial.mouse_click()

#友情池抽取函数
def FriendPointSummon():
    Serial.port_open('com5')
    time.sleep(0.5)
    
    Serial.mouse_set_zero()

    Serial.touch(540,472)
    
    Serial.touch(707,480,2)
    time.sleep(1)
    Serial.touch(647,570,8)    
        
    while True:
        Serial.touch(707,480,1)
        time.sleep(1)
        Serial.touch(647,570,7)
    
#搓丸子
def MakeCraftEssenceEXCard():
    Serial.port_open('com5')
    Serial.mouse_set_zero()
    
    while True:
        Serial.touch(720,280)
        time.sleep(0.5)
        Serial.mouse_swipe((150,250),(600,600),0.5)
        Serial.touch(990,570,3)
        time.sleep(0.5)
        Serial.touch(720,507,10)
    
if __name__=='__main__':
	FriendPointSummon()
    