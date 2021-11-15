# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 22:50:06 2021

@author: Paul

This program is used for testing only
"""




import Base_func_wormhole as Base_func
#import FGO_optional_func as op
import Serial_wormhole as Serial
#import time
#import win32con, win32api, win32gui
import pyautogui as ag
import Global_Config as gc
import time
import sys


fuse = Base_func.Fuse()

def time_out_check():           #checks once and ONLY once!
    
    timeoutFlag1, Position = Base_func.match_template("Time_out1")
    if not(timeoutFlag1):
        return
    retryFlag = False
    attempt_num = 0
    while not(retryFlag):
        retryFlag, retryPos = Base_func.match_template("Retry")
        attempt_num +=1
        if attempt_num >= 10:
            print("time_out_check(): Unexpected Error")
            sys.exit(0)
    Serial.touch(retryPos[0],retryPos[1])        #retry pressed
    fuse.increase_time_out()
    fuse.alarm()


def one_pool():
    depleted = False
    Serial.touch(485,400,1,3)
    while not(depleted):
        Serial.touch(460,350,10,0.25)
        depleted, Postion = Base_func.match_template("refill_pool")
        

def pool_rewards(pool_num):
    for i in range(pool_num):
        depleted = False
        Serial.touch(485,400,1,3)
        
        fuse.reset()
        fuse.set_acceptable_time(1.5,90)
        while not(depleted):
            time_out_check()
            Serial.touch(460,350,5,0.25)
            depleted, Position = Base_func.match_template("refill_pool")
            fuse.increase()
            fuse.alarm()
        fuse.reset()
        
        # Serial.touch(1115,205)      #重置奖池
        time.sleep(1)
        Serial.touch(Position[0],Position[1])
        Serial.touch(820,475)       #执行
        refilled = False
        
        fuse.set_acceptable_time(0.2)
        while not(refilled):
            time_out_check()
            refilled, Position2 = Base_func.match_template("refill_done")
            fuse.increase()
            fuse.alarm()
        fuse.reset()
        Serial.touch(Position2[0],Position2[1])
        print("Pool %d is done" % (i+1))
        


def getpos():
    Base_func.init_wormhole()
    orgpos = ag.position()
    zero_x = gc.const_interface_origin[0]
    zero_y = gc.const_interface_origin[1]
    px = orgpos[0] - zero_x
    py = orgpos[1] - zero_y
    return (px, py)


def Accident_Quit_Check():
    homeFlag, iconPos = Base_func.match_template("Accident_Quit")
    if homeFlag:
        EnterLoginFlag = EnterMenuFlag = ExitLastBattleFlag = CloseNotificationFlag = False
        # Serial.mouse_touch_raw(iconPos,5)  #点击FGO图标
        Serial.touch(89,162)
        Base_func.init_wormhole()
        
        while not(EnterLoginFlag):
            EnterLoginFlag, Position = Base_func.match_template("EnterLoginInterface")
        Serial.touch(Position[0],Position[1])
        # Serial.touch(650,315,1,10)      #轻触屏幕开始
        
        while not(EnterMenuFlag):
            EnterMenuFlag, Position = Base_func.match_template("EnterMenu")
        Serial.touch(Position[0],Position[1])
        # Serial.touch(650,315,1,15)      #轻触进入主菜单
        
        while not(ExitLastBattleFlag):
            ExitLastBattleFlag, Position = Base_func.match_template("ExitLastBattle")
        Serial.touch(Position[0],Position[1])
        # Serial.touch(490,465,1,10)      #不进入前次战斗

        while not(CloseNotificationFlag):
            CloseNotificationFlag, Position = Base_func.match_template("Close_Notification")
        Serial.touch(Position[0],Position[1],1,1)        
        # Serial.touch(1160,35,1,1)       #关闭通知
        Serial.touch(377,458,1,1)       #关闭友情点获得情况
        Serial.touch(965,305,1,10)       #点击活动
        Serial.mouse_swipe((1215,150),(1215,470),0.5)   #下拉至底部
 

def main():
    Base_func.init_wormhole()
    # Serial.mouse_move((1170,570))
    # print(getpos())
    pool_rewards(10)
    # Accident_Quit_Check()
    # ques, pos = Base_func.match_template("Gold_apple")
    # print("Variable ques is now:", ques)

        
if __name__=="__main__":
	main()

# op.FriendPointSummon(2.5)
# for i in range(10):
#     op.Upgrade()
#     op.FriendPointSummon()



# fusea = Base_func.Fuse()
# fusea.increase()


#Base_func.match_template('Maxlvl')

#(790,215) (125,330) (125,450)

#Serial.mouse_swipe((125,210),(125,580),0.5)


# def material_select():
#     Serial.mouse_move((125,210))
#     Serial.mouse_hold()
#     time.sleep(1)       #1.5 originally
#     Serial.mouse_move((790,215))
#     Serial.mouse_move((125,330))
#     Serial.mouse_move((125,450))
#     Serial.mouse_move((125,580))
#     time.sleep(0.5)
#     Serial.mouse_release()


