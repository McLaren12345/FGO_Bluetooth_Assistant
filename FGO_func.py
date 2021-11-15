# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 10:51:36 2019

@author: McLaren
"""
import time
import sys
import random
import Serial_wormhole as Serial 
import Base_func_wormhole as Base_func
import Mystic_Codes
import Global_Config as gc
#from Notice import sent_message


sys.path.append(gc.default_dir) 
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

        
        
def Accident_Quit_Check():
    homeFlag, iconPos = Base_func.match_template("Accident_Quit")
    if not(homeFlag):
        return
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
        

def enter_battle():
    menuFlag,Position1 = Base_func.match_template("Menu_button")
    reenterFlag,reenterPos = Base_func.match_template("reenter_battle")
    #print('Flag now: ', menu, "Position now: ", Position )
    fuse.reset()      
    fuse.set_acceptable_time(1)
    while not(menuFlag or reenterFlag):
        time.sleep(1)       #Original value is 1
        menuFlag,Position1 = Base_func.match_template("Menu_button")
        reenterFlag,reenterPos = Base_func.match_template("reenter_battle")
        fuse.increase()
        fuse.alarm()        
    fuse.reset()
    
    if menuFlag:
        LastOrderFlag,LastOrderPos = Base_func.match_template("LastOrder_sign")
        if LastOrderFlag:
            Serial.touch(LastOrderPos[0]+230,LastOrderPos[1]+50)
            print("Entered last order success")
            return "LastOrder"
        else:
            # Serial.touch(791,155)
            Serial.touch(930,200)
            print("Entered default success")
            return "Default"
    elif reenterFlag:
        # Serial.touch(705,475)
        Serial.touch(reenterPos[0],reenterPos[1]) 
        print("Reentered battle success") 
        return "Reenter"
    else:
        print("ReadyToBattle Error")
        sys.exit(0)
        
        
def WaitForBattleStart():
    fuse.reset()
    fuse.set_acceptable_time(0.2)
    ReadyFlag,Position = Base_func.match_template("Attack_button")
    while not(ReadyFlag):
        time_out_check()
        Serial.touch(935,60,1,0.1)
        time.sleep(0.1)        
        ReadyFlag,Position = Base_func.match_template("Attack_button")  
        fuse.increase()
        fuse.alarm()
    fuse.reset()

        
def WaitForFriendShowReady():
    fuse.reset()
    fuse.set_acceptable_time(0.3)
    friendFlag,Position = Base_func.match_template("friend_sign")
    noneFlag,Position2 = Base_func.match_template("no_friend")    
    while not(friendFlag or noneFlag):
        time_out_check()
        time.sleep(0.2)       
        friendFlag,Position = Base_func.match_template("friend_sign")
        noneFlag,Position2 = Base_func.match_template("no_friend")
        fuse.increase()
        fuse.alarm()
    fuse.reset()

    
def apple_feed(): 
    
    time.sleep(1.5)
    recoverFlag,Position = Base_func.match_template("AP_recover")
    if not(recoverFlag):
        print(" No need to feed apple")
        return
    
    silverFlag,silverPosition = Base_func.match_template("Silver_apple")  
    if silverFlag:
        Serial.touch(silverPosition[0]+280,silverPosition[1])
        time.sleep(1.5)            
        # Serial.touch(710,470)   #决定
        Serial.touch(825,470)
        gc.num_SilverApple_used += 1
        print(" Feed silver apple success")
        return
    
    goldFlag,goldPosition = Base_func.match_template("Gold_apple")
    if goldFlag:
        Serial.touch(goldPosition[0]+280,goldPosition[1])
        # Serial.touch(830,silverPosition[1])
        time.sleep(1.5)                
        # Serial.touch(710,470)   #决定
        Serial.touch(825,470)
        gc.num_GoldApple_used += 1
        print(" Feed gold apple success")
        return
    
    print(" No apple remain")
    Serial.touch(0,0)                
    sys.exit(0)
        
        
def find_friend(servant):
    WaitForFriendShowReady()
    time.sleep(1)    
    foundFlag,charPos = Base_func.match_template(servant+"_skill_level",False,0.8)
    attemptnum = 1
    #找310CBA直到找到为止
    fuse.set_acceptable_time(12,72)
    while not(foundFlag):
        print(" Didn't find {}, retry. Attempt{}".format(servant,attemptnum))
        #Flag,Position = Base_func.match_template('Refresh_friend')
        # Serial.touch(720,110)   #refresh 
        Serial.touch(790,110)
        time.sleep(0.5)
        #Flag,Position = Base_func.match_template('Refresh_decide')
        # Serial.touch(705,475)   #decide
        Serial.touch(820,475)
        WaitForFriendShowReady()   
        foundFlag,charPos = Base_func.match_template(servant+"_skill_level",False,0.8)
        if (foundFlag):
            break;
        attemptnum += 1
        time.sleep(11)
        fuse.increase()
        fuse.alarm()
        
    print("Found",servant)
    fuse.reset()
    Serial.touch(charPos[0],charPos[1]-60)
    # Serial.touch(Position[0],Position[1])
    time.sleep(1.5)               

     
def budao():   #!
    finFlag = False
    attackFlag = False
    while not(finFlag):
        Serial.touch(960,510)   #点击attack按钮 
        time.sleep(1)       
        Card_index = random.sample(range(0,4),3) #随机三张牌   
        Serial.touch(115+(Card_index[0])*215,430)          
        Serial.touch(115+(Card_index[1])*215,430)  
        Serial.touch(115+(Card_index[2])*215,430)
        print(" Card has pressed")
        while not(finFlag or attackFlag):
            finFlag,Position = Base_func.match_template("Battlefinish_sign")
            attackFlag,Position = Base_func.match_template("Attack_button")
 
        
def quit_battle():
    fuse.reset()
    fuse.set_acceptable_time(0.1)
    time.sleep(15)
    finFlag,Position = Base_func.match_template("Battlefinish_sign")
    attackFlag,Position = Base_func.match_template("Attack_button")
    while not(finFlag or attackFlag):
        time_out_check()
        finFlag,Position = Base_func.match_template("Battlefinish_sign")
        attackFlag,Position = Base_func.match_template("Attack_button")
        fuse.increase()
        fuse.alarm()
    fuse.reset()
    if finFlag:
        pass
    elif attackFlag:
        print(" 翻车，进入补刀程序")          #翻车检测
        budao()
    print(" Battle finished")
    time.sleep(0.5)
    rainbowFlag,Position = Base_func.match_template("Rainbow_box")  #检测是否掉礼装，若掉落则短信提醒  
    if rainbowFlag:
        gc.num_Craft += 1
    Serial.touch(986,565,10,0.3)
    # Serial.touch(1290,670,6)     
    # Serial.touch(235,525,2,0.3)         # 拒绝好友申请
    Serial.touch(395,515,2,0.3)
    # Serial.touch(490,650)           #拒绝好友,结束
    # Serial.mouse_set_zero()         #鼠标复位,防止误差累积
    print(" Quit success")
    time.sleep(1)


#improve        
def Master_skill(func = Mystic_Codes.Chaldea_Combat_Uniform, *args):
    # Serial.touch(1010,266)               #御主技能按键
    Serial.touch(1185,265)                  #全面屏
    func(*args)
    time.sleep(1)    
    WaitForBattleStart()
    print(" Master skill{} has pressed".format(args[0]))
    time.sleep(1)
    #! (1165 + 95(x-1),335)

    
def character_skill(character_no,skill_no,para=None):   #角色编号，技能编号，选人（可选）
    # charPos = (65+(character_no-1)*270+(skill_no-1)*80,488)
    charPos = (105+(character_no-1)*265+(skill_no-1)*75,470)    #全面屏
    Serial.touch(charPos[0],charPos[1])    
    if para != None:
        # targetPos = (280+(para-1)*250,350)  #技能选人
        targetPos = (400+(para-1)*255,375)  #技能选人，全面屏
        Serial.touch(targetPos[0],targetPos[1])        
    time.sleep(0.5)         #等待技能动画时间,3 originally
    WaitForBattleStart()
    print(" Character{}'s skill{} has pressed".format(character_no,skill_no))

    
def card(NoblePhantasm_no=1):    
    # Serial.touch(960,510)   #点击attack按钮 
    Serial.touch(1115,505)
    time.sleep(1.5)       
    # Serial.touch(350+(NoblePhantasm_no-1)*200,200)   #打手宝具,参数可选1-3号宝具位 #
    Serial.touch(465+(NoblePhantasm_no-1)*200,150,1,0.3)  #200 !
    Card_index = random.sample(range(0,4),2) #随机两张牌   
    # Serial.touch(115+(Card_index[0])*215,430)          
    # Serial.touch(115+(Card_index[1])*215,430) 
    Serial.touch(230+(Card_index[0])*215,405,1,0.3)          
    Serial.touch(230+(Card_index[1])*215,405,1,0.3)
    print(" Card has pressed")
    
def battle(): 
    #判断是否进入战斗界面
    #Serial.mouse_set_zero()         #鼠标复位,防止误差累积
    # Serial.touch(1005,570)  
    Serial.touch(1170,540)          #开始任务，全面屏
    print(" Start battle button pressed")
    time.sleep(0.5)                          #等待战斗开始
    WaitForBattleStart()    
    #time.sleep(6)                   #等待6秒，因为礼装效果掉落暴击星会耗时
    """
    #Turn1
    character_skill(3,1,1)
    character_skill(2,1,1)
    character_skill(1,2)  
    card()
    
    #Serial.mouse_set_zero()         #鼠标复位,防止误差累积
    time.sleep(10)                          #等待战斗动画播放完成
    Current_state.WaitForBattleStart()
    #Turn2
    character_skill(3,3,1)
    Master_skill(Mystic_Codes.Chaldea_Combat_Uniform, 3,3,2)
    character_skill(3,3)
    character_skill(3,2)
    card()    
    
    #Serial.mouse_set_zero()         #鼠标复位,防止误差累积
    time.sleep(10)                          #等待战斗动画播放完成
    Current_state.WaitForBattleStart()
    #Turn3
    character_skill(3,1,1)
    character_skill(2,3,1)
    card()
    """
    character_skill(1,3)
    character_skill(2,2)
    character_skill(2,3,1)
    character_skill(3,1)
    character_skill(3,2,2)
    character_skill(3,3,2)
    Serial.touch(1185,265,1,0.3)
    Serial.touch(945+70*(1-1),265,1,0.3)
    # Serial.touch(400,375,1,0.3)
    time.sleep(0.5)
    WaitForBattleStart()
    Serial.touch(1185,265,1,0.3)
    Serial.touch(945+70*(3-1),265,1,0.3)
    Serial.touch(230+170*(3-1),290,1,0.3)
    Serial.touch(230+170*(5-1),290,1,0.3)
    Serial.touch(655,520,1,0.3)
    time.sleep(0.5)
    WaitForBattleStart()
    character_skill(3,1)
    character_skill(3,2,2)
    character_skill(3,3,2)
    card()
    time.sleep(10)
    WaitForBattleStart()
    

    card(2)
    time.sleep(10)
    WaitForBattleStart()
    
    character_skill(1,1)
    character_skill(1,2,2)
    character_skill(1,3,2)
    card(2)

def FGO_process(times=1,servant="CBA"):
    for i in range(times):
        # Accident_Quit_Check()
        times-=1
        enter_battle()
        apple_feed()
        find_friend(servant)        
        battle()        
        quit_battle()                
        print(" ")
        print(" {}times of battles remain.".format(times))
        print(" Currently {} Gold Apples, {} Silver Apples used, {} Crafts droped.".format(gc.num_GoldApple_used,gc.num_SilverApple_used,gc.num_Craft))
    Serial.touch(490,475)           #关闭,全面屏
      
def main():
    Base_func.init_wormhole()
    for i in range(10,0,-1):
        print("Program Starts In %d " % i)
        time.sleep(1)
    print("Program Starts, Enjoy!")
    Serial.mouse_set_zero()
    FGO_process(200,"Caber")
    print(" All done!") 
        
if __name__=="__main__":
	main()

#全神贯注情况下人类玩家，连续战斗无刷新无苹果约为1分38秒，主界面进入有苹果约为1分49秒，
#均包含速点和避免连携的情况
#模板匹配时，无法分别不同模板的明暗区别，所以需要模板内有明暗对照来做区分

