# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 22:46:30 2020

@author: McLaren
"""
import sys
sys.path.append(r'F:\FGO_Project') 
import Serial

#换人服
def Chaldea_Combat_Uniform(*args):
    def Hanlder(*args):
        if args[0]==1:                     #加攻
            Serial.touch(760,266)        
        elif args[0]==2:                   #眩晕
            Serial.touch(835,266)        
        elif args[0]==3:                   #换人
            Serial.touch(920,266)                           
            Serial.touch(630+(args[2]-1)*170,300)        
            Serial.touch(120+(args[1]-1)*170,300)        
            Serial.touch(530,530)
            
    Hanlder(*args)
 
#热带夏日
def Tropical_Summer(*args):
    def Hanlder(*args):
        if args[0]==1:
            Serial.touch(760,266)
            Position = (280+(args[1]-1)*250,350)  #蓝魔放与宝具威力提升，技能选人
            Serial.touch(Position[0],Position[1])
        elif args[0]==2:
            Serial.touch(835,266)
            Position = (280+(args[1]-1)*250,350)  #蓝卡暴击星集中度提升，技能选人
            Serial.touch(Position[0],Position[1])
        elif args[0]==3:                   
            Serial.touch(920,266)                           
            Position = (280+(args[1]-1)*250,350)  #充能10%，技能选人
            Serial.touch(Position[0],Position[1])
            
    Hanlder(*args)
    
#模板
def Template(*args):
    def Hanlder(*args):
        if args[0]==1:
            Serial.touch(760,266)
            #写一技能要点的位置，可加参数
        elif args[0]==2:
            Serial.touch(835,266)
            #写二技能要点的位置，可加参数
        elif args[0]==3:                   
            Serial.touch(920,266)                           
            #写三技能要点的位置，可加参数
            
    Hanlder(*args)
    