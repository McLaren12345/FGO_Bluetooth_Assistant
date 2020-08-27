# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 13:08:08 2020

@author: McLaren
"""

import time
import sys
import random
sys.path.append(r'F:\FGO_Project')  
import Base_func
import cv2 as cv

#TreasureDeviceStartXPosition = 286
#TreasureDeviceEndXPosition = 414
#TreasureDeviceStartYPosition = 220
#TreasureDeviceEndYPosition = 300
#TreasureDeviceXBias = 195
#
#CardStartXPosition = 45
#CardEndXPosition = 176
#CardStartYPosition = 425
#CardEndYPosition = 520
#CardXBias = 214

#SkillStartXPosition = 29
#SkillEndXPosition = 62
#SkillStartYPosition = 500
#SkillEndYPosition = 525
#SkillXBias = 80
#SkillServantBias = 269

def DetectTreasureDevice(img,TreasureDevice_no,err=0.85):
    crop = img[220:300,286+TreasureDevice_no*195:414+TreasureDevice_no*195]
    
    for i,element in enumerate(['Buster','Art','Quick']):
        temppath = 'F:/FGO_Project/Template/TreasureDevice_' + element +'.jpg'

        player_template = cv.imread(temppath)
        player = cv.matchTemplate(crop, player_template, cv.TM_CCOEFF_NORMED)

        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(player)
        
        if max_val>err:
            return True
    
    return False

#可用宝具检测函数，返回可用的宝具位置列表，如[1,2]表示1、2号位英灵的宝具可用（需在选卡界面检测）
def GetAvailableTreasureDevice():
    img = Base_func.window_capture()
    
    AvailableTreasureDeviceList = []
    
    for i in range(3):
        Flag = DetectTreasureDevice(img,i)
        if Flag==True:
            AvailableTreasureDeviceList.append(i+1)
            
    return AvailableTreasureDeviceList

def DetectCardColor(img,Card_no,err=0.85):
    crop = img[425:520,45+Card_no*214:176+Card_no*214]
    
    for i,element in enumerate(['Buster','Art','Quick']):
        temppath = 'F:/FGO_Project/Template/' + element +'.jpg'

        player_template = cv.imread(temppath)
        player = cv.matchTemplate(crop, player_template, cv.TM_CCOEFF_NORMED)

        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(player)
        
        if max_val>err:
            return True, element
    
    return False, 'None'

#卡牌颜色目标获取函数，返回五张卡的颜色值，如['Art','Buster',...,'Quick']
def GetCardIndex():
    img = Base_func.window_capture()
    
    CardIndex = []
    
    for Card_no in range(5):
        Flag, CardColor = DetectCardColor(img,Card_no)
        if Flag==True:
            CardIndex.append(CardColor)
        else:
            CardIndex.append('None')
            
    return CardIndex

def DetectAvailableSkill(img,Servant_no,err=0.8):
    croplist = [img[500:528,29+Servant_no*269+Skill_no*80:65+Servant_no*269+Skill_no*80] for Skill_no in range(3)]
    ServantAvailableSkill = []
    
    for i,crop in enumerate(croplist):
        temppath = 'F:/FGO_Project/Template/SkillColdTime.jpg'

        player_template = cv.imread(temppath)
        player = cv.matchTemplate(crop, player_template, cv.TM_CCOEFF_NORMED)

        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(player)
        
        if max_val>err:
            pass
        else:
            ServantAvailableSkill.append(i+1)
    
    return ServantAvailableSkill

#英灵可用技能获取函数，返回值形如：[[1,2],[3],[]],表示1号位英灵的1、2技能可用；2号位英灵3技能可用，3号位英灵无可用技能
def GetAvailableSkillIndex():
    img = Base_func.window_capture()
    
    AvailableSkillIndex = []
    
    for Servant_no in range(3):
        AvailableSkillIndex.append(DetectAvailableSkill(img,Servant_no))
            
    return AvailableSkillIndex