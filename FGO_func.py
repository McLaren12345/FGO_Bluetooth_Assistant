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

def enter_battle():
    menuFlag,Position1 = Base_func.match_template("Menu_button")
    reenterFlag,Position2 = Base_func.match_template("reenter_battle")
    #print('Flag now: ', menu, "Position now: ", Position )   
    
    while not(menuFlag or reenterFlag):
        time.sleep(1)       #Original value is 1
        menuFlag,Position1 = Base_func.match_template("Menu_button")
        reenterFlag,Position2 = Base_func.match_template("reenter_battle")
        fuse.increase()
        fuse.alarm()        
    fuse.reset()
    
    if menuFlag:
        LastOrderFlag,Position3 = Base_func.match_template("LastOrder_sign")
        if LastOrderFlag:
            Serial.touch(Position3[0]+230,Position3[1]+50)
            print("Entered last order success")
            return "LastOrder"
        else:
            Serial.touch(791,155)
            print("Entered default success")
            return "Default"
    elif reenterFlag:
        Serial.touch(705,475) 
        print("Reentered battle success") 
        return "Reenter"
    else:
        print("ReadyToBattle Error")
        sys.exit(0)
        
        
def WaitForBattleStart():
    Flag,Position = Base_func.match_template("Attack_button")
    while not(Flag):
        time.sleep(1)        
        Flag,Position = Base_func.match_template("Attack_button")  
        fuse.increase()
        fuse.alarm()
    fuse.reset()

        
def WaitForFriendShowReady():
    friendFlag,Position = Base_func.match_template("friend_sign")
    noneFlag,Position2 = Base_func.match_template("no_friend")    
    while not(friendFlag or noneFlag):
        time.sleep(1)       
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
    
    silverFlag,silverPosition = Base_func.match_template("Silver_apple")          #check similarity between highlight and normal icon   
    if silverFlag:
        Serial.touch(709,silverPosition[1])
        time.sleep(1.5)            
        Serial.touch(710,470)   #决定
        gc.num_SilverApple_used += 1
        print(" Feed silver apple success")
        return
    
    goldFlag,goldPosition = Base_func.match_template("Gold_apple")
    if goldFlag:
        Serial.touch(709,goldPosition[1])
        time.sleep(1.5)                
        Serial.touch(710,470) #决定
        gc.num_GoldApple_used += 1
        print(" Feed gold apple success")
        return
    
    print(" No apple remain")
    Serial.touch(0,0)                
    sys.exit(0)
        
        
def find_friend(servant):
    WaitForFriendShowReady()    
    foundFlag,Position = Base_func.match_template(servant+"_skill_level")
    attemptnum = 1
    #找310CBA直到找到为止
    while not(foundFlag):
        print(" Didn't find {}, retry. Attempt{}".format(servant,attemptnum))
        #Flag,Position = Base_func.match_template('Refresh_friend')
        Serial.touch(720,110)   #refresh     
        time.sleep(0.5)
        #Flag,Position = Base_func.match_template('Refresh_decide')
        Serial.touch(705,475)   #decide
        WaitForFriendShowReady()   
        foundFlag,Position = Base_func.match_template(servant+"_skill_level")
        attemptnum += 1
        time.sleep(11) 
        
    print(" Success find",servant)
    Serial.touch(Position[0],Position[1]-60)
    time.sleep(1.5)               

     
def budao():   
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
    time.sleep(15)
    finFlag,Position = Base_func.match_template("Battlefinish_sign")
    attackFlag,Position = Base_func.match_template("Attack_button")
    while not(finFlag or attackFlag):
        finFlag,Position = Base_func.match_template("Battlefinish_sign")
        attackFlag,Position = Base_func.match_template("Attack_button")
    if finFlag:
        pass
    elif attackFlag:
        print(" 翻车，进入补刀程序")          #翻车检测
        budao()
    print(" Battle finished")
    time.sleep(1)
    rainbowFlag,Position = Base_func.match_template("Rainbow_box")  #检测是否掉礼装，若掉落则短信提醒  
    if rainbowFlag:
        gc.num_Craft += 1
    Serial.touch(986,565,6)    
    Serial.touch(235,525,2)                #拒绝好友申请
    Serial.mouse_set_zero()         #鼠标复位,防止误差累积
    print(" Quit success")
    time.sleep(1)


#improve        
def Master_skill(func = Mystic_Codes.Chaldea_Combat_Uniform, *args):
    Serial.touch(1010,266)               #御主技能按键
    func(*args)
    time.sleep(1)    
    WaitForBattleStart()
    print(" Master skill{} has pressed".format(args[0]))
    time.sleep(1)

    
def character_skill(character_no,skill_no,para=None):   #角色编号，技能编号，选人（可选）
    charPos = (65+(character_no-1)*270+(skill_no-1)*80,488)
    Serial.touch(charPos[0],charPos[1])    
    if para != None:
        targetPos = (280+(para-1)*250,350)  #技能选人
        Serial.touch(targetPos[0],targetPos[1])        
    time.sleep(3)         #等待技能动画时间
    WaitForBattleStart()
    print(" Character{}'s skill{} has pressed".format(character_no,skill_no))

    
def card(NoblePhantasm_no=1):    
    Serial.touch(960,510)   #点击attack按钮 
    time.sleep(2)       
    Serial.touch(350+(NoblePhantasm_no-1)*200,200)   #打手宝具,参数可选1-3号宝具位
    Card_index = random.sample(range(0,4),2) #随机两张牌   
    Serial.touch(115+(Card_index[0])*215,430)          
    Serial.touch(115+(Card_index[1])*215,430)    
    print(" Card has pressed")
    
def battle(): 
    #判断是否进入战斗界面
    #Serial.mouse_set_zero()         #鼠标复位,防止误差累积
    Serial.touch(1005,570)      
    print(" Start battle button pressed")
    time.sleep(8)                          #等待战斗开始
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
    character_skill(3,1,1)
    character_skill(2,1,1)
    character_skill(1,2)
    Master_skill(Mystic_Codes.Tropical_Summer, 2,1,1)    
    card()
    time.sleep(10)
    WaitForBattleStart()
    
    character_skill(3,3,1)
    card()
    time.sleep(10)
    WaitForBattleStart()
    
    character_skill(2,3,1)
    character_skill(2,2)
    character_skill(3,2)
    character_skill(1,1)
    card()

def FGO_process(times=1,servant="CBA"):
    for i in range(times):
        times-=1
        enter_battle()
        apple_feed()
        find_friend(servant)
        
        battle()        
        quit_battle()                
        print(" ")
        print(" {}times of battles remain.".format(times))
        print(" Currently {} Gold Apples, {} Silver Apples used, {} Crafts droped.".format(gc.num_GoldApple_used,gc.num_SilverApple_used,gc.num_Craft))
      
def main():
    #Serial.port_open(port_no)   #写入通讯的串口号
    Base_func.init_wormhole()
    Serial.mouse_set_zero()
    FGO_process(1,"CBA")
    #Serial.port_close()
    print(" All done!") 
        
if __name__=="__main__":
	main()


