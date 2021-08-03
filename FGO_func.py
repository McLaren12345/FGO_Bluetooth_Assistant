# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 10:51:36 2019

@author: McLaren
"""
import time
import sys
from tqdm import tqdm
import random
sys.path.append(r'F:\FGO_Project') 
import Serial_wormhole as Serial 
#import Base_func
import Base_func_wormhole as Base_func
import Mystic_Codes
#from Notice import sent_message

class state:
    def HasBackToMenu(self):
        Flag,Position = Base_func.match_template('Menu_button')
        print('Flag now: ', Flag, "Position now: ", Position )
        while bool(1-Flag):
            time.sleep(0.1)       ############### Original value is 1
            Flag,Position = Base_func.match_template('Menu_button')
            if Flag:
                break
            Flag,Position = Base_func.match_template('reenter_battle')
            if Flag:
                break
            
    def WaitForBattleStart(self):
        Flag,Position = Base_func.match_template('Attack_button')
        while bool(1-Flag):
            time.sleep(1)        
            Flag,Position = Base_func.match_template('Attack_button')    
            
    def WaitForFriendShowReady(self):
        Flag,Position = Base_func.match_template('friend_sign')
        while bool(1-Flag):
            time.sleep(1)       
            Flag,Position = Base_func.match_template('friend_sign')
            if Flag:
                break
            Flag,Position = Base_func.match_template('no_friend')
            if Flag:
                break

Current_state = state()

num_Craft = 0
num_GoldApple_used = 0
num_SilverApple_used = 0

def enter_battle():   
    Current_state.HasBackToMenu()
        #确认已经返回菜单界面，或检测到连续出击按键
    Flag,Position = Base_func.match_template('reenter_battle') 
    if Flag:
        Serial.touch(705,475)       
        print(' ')
        print(' Reenter battle success')    
        return
    
    Flag,Position = Base_func.match_template('LastOrder_sign') 
    if Flag:
        Serial.touch(Position[0]+230,Position[1]+50)       
        print(' ')
        print(' Enter battle success')
    else:
        Serial.touch(791,155)
        print(' ')
        print(' Enter battle by clicking the default position')
    
def apple_feed(): 
    global num_GoldApple_used, num_SilverApple_used
    time.sleep(1.5)
    Flag,Position = Base_func.match_template('AP_recover')
    if Flag:
        Flag,Position = Base_func.match_template('Silver_apple')
        if Flag:
            Serial.touch(709,Position[1])
            time.sleep(1.5)            
            Flag,Position = Base_func.match_template('Feedapple_decide')
            Serial.touch(Position[0],Position[1])
            num_SilverApple_used += 1
            print(' Feed silver apple success')
        else:
            Flag,Position = Base_func.match_template('Gold_apple')
            if Flag:
                Serial.touch(709,Position[1])
                time.sleep(1.5)                
                Flag,Position = Base_func.match_template('Feedapple_decide')
                Serial.touch(Position[0],Position[1])  
                num_GoldApple_used += 1
                print(' Feed gold apple success')
            else:
                print(' No apple remain')
                Serial.touch(0,0)                
                sys.exit(0)
    else:
        print(' No need to feed apple')
        
def find_friend(servant):       #test, 0.9 original
    Current_state.WaitForFriendShowReady()
    
    Flag,Position = Base_func.match_template(servant+'_skill_level',False,0.85)
    time_limit_flag = 1
    #找310CBA直到找到为止
    while bool(1-Flag):
        print(' Didn\'t find {}, retry. Attempt{}'.format(servant,time_limit_flag))
        if time_limit_flag>1:
            time.sleep(15)          
        #Flag,Position = Base_func.match_template('Refresh_friend')
        Serial.touch(710,110)       
        time.sleep(1.5)
        Flag,Position = Base_func.match_template('Refresh_decide')
        Serial.touch(Position[0],Position[1])

        Current_state.WaitForFriendShowReady()
   
        Flag,Position = Base_func.match_template(servant+'_skill_level',False,0.85)
        time_limit_flag+=1
        
    if Flag:
        print(' Success find',servant)
        Serial.touch(Position[0],Position[1]-60)
        time.sleep(1.5)               
        Serial.touch(1005,570)       
        print(' Start battle button pressed')
        
def budao():
    while True:
        while True:
            time.sleep(1)
            Flag,Position = Base_func.match_template('Battlefinish_sign')
            if Flag:
                break
            Flag,Position = Base_func.match_template('Attack_button')
            if Flag:
                break
        Flag,Position = Base_func.match_template('Attack_button')
        if Flag:
            Serial.touch(960,510)   #点击attack按钮 
            time.sleep(1)       
            Card_index = random.sample(range(0,4),3) #随机三张牌   
            Serial.touch(115+(Card_index[0])*215,430)          
            Serial.touch(115+(Card_index[1])*215,430)  
            Serial.touch(115+(Card_index[2])*215,430)
            print(' Card has pressed')        
        else:
            break
        
def quit_battle():
    global num_Craft
    time.sleep(15)
    while True:
        time.sleep(1)
        Flag,Position = Base_func.match_template('Battlefinish_sign')
        if Flag:
            break
        Flag,Position = Base_func.match_template('Attack_button')
        if Flag:
            break
    Flag,Position = Base_func.match_template('Attack_button')
    if Flag:
        print(' 翻车，进入补刀程序')          #翻车检测
        #Serial.mouse_set_zero()
        #sent_message(text='【FGO】: Encounter a battle error.')        
        budao()
    print(' Battle finished')
    time.sleep(1)
    Flag,Position = Base_func.match_template('Rainbow_box')  #检测是否掉礼装，若掉落则短信提醒
    if Flag:
        #sent_message()
        num_Craft += 1
    Serial.touch(986,565,6)    
    Serial.touch(235,525,2)                #拒绝好友申请
    Serial.mouse_set_zero()         #鼠标复位,防止误差累积
    print(' Quit success')
    time.sleep(1)
        
def Master_skill(func = Mystic_Codes.Chaldea_Combat_Uniform, *args):
    Serial.touch(1010,266)               #御主技能按键
    func(*args)
    time.sleep(1)    
    Current_state.WaitForBattleStart()
    print(' Master skill{} has pressed'.format(args[0]))
    time.sleep(1)
    
def character_skill(character_no,skill_no,para=None):   #角色编号，技能编号，选人（可选）
    Position = (65+(character_no-1)*270+(skill_no-1)*80,488)
    Serial.touch(Position[0],Position[1])    
    if para != None:
        Position = (280+(para-1)*250,350)  #技能选人
        Serial.touch(Position[0],Position[1])        
    time.sleep(3)         #等待技能动画时间
    Current_state.WaitForBattleStart()
    print(' Character{}\'s skill{} has pressed'.format(character_no,skill_no))
    
def card(TreasureDevice_no=1):    
    Serial.touch(960,510)   #点击attack按钮 
    time.sleep(2)       
    Serial.touch(350+(TreasureDevice_no-1)*200,200)   #打手宝具,参数可选1-3号宝具位
    Card_index = random.sample(range(0,4),2) #随机两张牌   
    Serial.touch(115+(Card_index[0])*215,430)          
    Serial.touch(115+(Card_index[1])*215,430)    
    print(' Card has pressed')
    
def battle(): 
    #判断是否进入战斗界面
    #Serial.mouse_set_zero()         #鼠标复位,防止误差累积
    time.sleep(8)                          #等待战斗开始
    Current_state.WaitForBattleStart()    
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
    card()
    time.sleep(10)
    Current_state.WaitForBattleStart()
    card()
    time.sleep(10)
    Current_state.WaitForBattleStart()
    card()

def FGO_process(times=1,servant='CBA'):
    for i in tqdm(range(times)):
        times-=1
        enter_battle()
        apple_feed()
        find_friend(servant)
        battle()        
        quit_battle()                
        print(' ')
        print(' {}times of battles remain.'.format(times))
        print(' Currently {} Gold Apples, {} Silver Apples used, {} Crafts droped.'.format(num_GoldApple_used,num_SilverApple_used,num_Craft))
      
def main(port_no,times=1,servant='CBA'):
    Serial.port_open(port_no)   #写入通讯的串口号
    Serial.mouse_set_zero()
    FGO_process(times,servant)
    Serial.port_close()
    print(' All done!') 
        
if __name__=='__main__':
	main('com5',1)


