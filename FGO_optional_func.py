# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 20:17:33 2020

@author: McLaren
"""

import sys
import Serial_wormhole as Serial 
import time
import Base_func_wormhole as Base_func
#import pyautogui as ag
import Global_Config as gc

sys.path.append(gc.default_dir) 


fuse = Base_func.Fuse()

'''
#无限池抽取函数
def InfinatePool():
    Serial.mouse_set_zero()
    Serial.mouse_move((320,360))
    for i in range(100):
        Serial.mouse_click()

def getpos():
    orgpos = ag.position()
    zero_x = 1479
    zero_y = 16
    px = orgpos[0] - zero_x
    py = orgpos[1] - zero_y
    return (px, py)
'''

def main_click_menu():                  #主菜单
    Serial.touch(995,575)               
    time.sleep(1)   
    
def main_click_exit():                  #左上角关闭
    Serial.touch(85,40)                 
    time.sleep(1)

def menu_click_enhance():               #主菜单：强化
    Serial.touch(400,550)               
    time.sleep(1)    
    
def menu_click_store():                 #主菜单：商店
    Serial.touch(680,550)               
    time.sleep(1) 
    
def menu_click_summon():                #主菜单：召唤
    Serial.touch(540,545)               
    time.sleep(1)    
           
def store_click_sell():                 #商店：灵基贩卖
    Serial.touch(815,295)               
    time.sleep(1)
    
def enhance_click_essence():            #强化：概念礼装强化
    Serial.touch(820,400)               
    time.sleep(1)
    
def full_click_enhance():               #背包已满提示：强化
    Serial.touch(540,400)               
    time.sleep(1)
    
def full_click_sell():                  #背包已满提示：贩卖
    Serial.touch(295,400)               
    time.sleep(1)

def upgrade_click_filter():             #礼装/从者界面：筛选
    Serial.touch(820,110) 
    time.sleep(0.5)
    
def filter_click_default():             #筛选：回到初始设定
    Serial.touch(375,465) 
    time.sleep(0.2)

def essencefilter_click_rareness(starnum):  #礼装选择界面：稀有度
    Serial.touch((855-(starnum-1)*155),220) #155为选项间隔，此数值有待进一步精确确认
    time.sleep(0.2)
    
def servantfilter_click_type(type_name):    #从者选择界面：类型
    if type_name == "Servant":
        Serial.touch(360,240) #从者
        time.sleep(0.2)
    elif type_name == "Exp":
        Serial.touch(540,240) #经验值
        time.sleep(0.2)
    elif type_name == "FuFu":
        Serial.touch(720,240) #芙芙
        time.sleep(0.2) 
    else:
        print("unkown type")
        
def filter_click_apply():               #筛选：决定
    Serial.touch(700,535)
    time.sleep(0.5)
    
def upgrade_click_order():              #礼装/从者界面：顺序类型
    Serial.touch(945,110) 
    time.sleep(0.5)
  
def order_smartfilterOn(OnOffBool):     #顺序类型：智能筛选
    Flag,Position = Base_func.match_template("SmartFilterOff")    
    if (Flag and OnOffBool) or (not(Flag) and not(OnOffBool)): #smart filter now off, and we need it on
        Serial.touch(485,395) #turn on/off smart filter
        time.sleep(0.2)    

def upgrade_ascend(UpDownBool):         #礼装/从者界面：升降序
    Flag,Position = Base_func.match_template("DownOrder")
    if (Flag and UpDownBool) or (not(Flag) and not(UpDownBool)): #descending order now, we need the opposite
        Serial.touch(Position[0],Position[1]) #change to ascending order
        time.sleep(0.5)
    

#友情池1次抽取
def FriendPointSummon(delay=0):   
    Flag,Position = Base_func.match_template("Continue") #是否有继续10连按钮
    if not(Flag):       #无按钮  
        Flag,Position = Base_func.match_template("FreeSummon") 
        if Flag:        #免费友情点10连
            Serial.touch(540,472)            
        else:           #付费友情点10连
            Serial.touch(702,480)
            
    Flag,Position = Base_func.match_template("BoxFull")  
    if Flag:            #背包满
        return Flag,Position
    
    time.sleep(1)        
    Serial.touch(702,480)   #决定，开始召唤
    time.sleep(1+delay)     #依据网络状况改动，delay为第一次召唤的额外加载时间
    Serial.touch(647,570,6) #速点      
    Flag,Position = Base_func.match_template("BoxFull")
    return Flag,Position    


#满背包的类型判断，可为从者、礼装、纹章
def FullBoxType():
    Flag, Position = Base_func.match_template("ServantFull")
    if Flag:
        return "Servant"
    Flag, Position = Base_func.match_template("EssenceFull")
    if Flag:
        return "Essence"
    return "Heraldry"   #need further development
   

#筛选、排序礼装，使狗粮礼装排在前
def Filter_Order_change(filteredObject, smartfilter_on, ascending_order):  
    upgrade_click_filter()
    filter_click_default()    
    if (filteredObject == "Essence"):
        essencefilter_click_rareness(2)
        essencefilter_click_rareness(1)
    elif (filteredObject == "Servant"):
        Serial.mouse_swipe((955,205),(955,505),0.5) #scroll to bottom
        time.sleep(0.5)
        servantfilter_click_type("Servant")
    elif (filteredObject == "ExpFuFu"):
        Serial.mouse_swipe((955,205),(955,505),0.5) #scroll to bottom
        time.sleep(0.5)
        servantfilter_click_type("Exp")
        servantfilter_click_type("FuFu")              
    filter_click_apply()
          
    upgrade_click_order()
    if (filteredObject == "Essence"):
        Serial.touch(270,200) #level order, hard coded
    else:
        Serial.touch(270,325) #rareness order
      
    order_smartfilterOn(smartfilter_on)
    filter_click_apply()
    upgrade_ascend(ascending_order)
        

#贩卖所有友情池抽取的从者
def clear_servants():
    Filter_Order_change("Servant", True, True)
    
    Flag,Position = Base_func.match_template("Dense")     
    while not(Flag):
        fuse.increase()
        Serial.touch(30,568)
        time.sleep(1)
        Flag,Position = Base_func.match_template("Dense")
        fuse.alarm()
    fuse.reset()
    
    Serial.mouse_swipe((125,210),(125,580),8.5) #batch selection 
    Serial.touch(970,565) #decide
    time.sleep(1)
    Serial.touch(710,520) #decide
    time.sleep(1)
    Serial.touch(540,525) #close
    time.sleep(1)


#检查丸子上锁情况，如果没有上锁则自动上锁
def lock():     
    Locked, Position = Base_func.match_template("Lock")
    if not(Locked):
        Serial.touch(25,300)   #点击统一锁定
        time.sleep(0.5)
        Serial.touch(120,215) #first
        time.sleep(0.5)
        Serial.touch(25,205)   #点击选择对象
        time.sleep(0.5)


#检查丸子是否满级        
def maxlvl_check():  
    Maxlvl, Position = Base_func.match_template("Maxlvl")
    if Maxlvl:
        # Serial.touch(166,340) #选择需要强化的礼装
        # time.sleep(0.5)
        # lock()
        # Serial.touch(120,215) #first
        # time.sleep(1)
        return True
    return False

#选择需要强化的丸子礼装
def essence_choose():
    Serial.touch(166,340) #选择需要强化的礼装
    time.sleep(1)
    lock()
    Serial.touch(120,215) #默认选择第一个
    time.sleep(1)
        

#升级丸子
def Upgrade():
    Serial.touch(720,280)
    time.sleep(1)
    Serial.mouse_swipe((125,210),(125,580),0.5)
    time.sleep(0.2)
    Serial.touch(990,570)
    time.sleep(1)    
    InterfaceSign, Positiion = Base_func.match_template("UpgradeInterface") 
    if not(InterfaceSign):      #没能回到强化界面，没有剩余材料了
        return True  
    Serial.touch(990,570)
    time.sleep(0.5)
    Serial.touch(720,507,10)
    return False


#搓丸子直到材料耗尽或者达到指定目标
def MaxLevelMaterial(finished, target):
    Serial.touch(166,340) #选择需要强化的礼装
    time.sleep(1)
    Filter_Order_change("Essence", True, False) #筛选及调整顺序        
    lock()                                      #上锁第一个
    Serial.touch(120,215)                       #选定第一个
    time.sleep(1)
    
    Serial.touch(720,280)                       #选择材料
    time.sleep(1)
    Filter_Order_change("Essence", False, True) #筛选及调整顺序
    time.sleep(0.2)
    Serial.mouse_swipe((125,210),(125,580),0.5) #batch selection 
    Serial.touch(990,570,4)                     #确定材料，确定强化
    time.sleep(0.2)
    Serial.touch(720,507,10)                    #确定以及速点
        
                                                  #满级重新选择
    if maxlvl_check():
        finished += 1     
        if finished == target:
            return finished
        else:
            essence_choose()
                 
    #fuse may be required
    empty = False
    while not(empty):                           #重复升级至材料耗尽或到达指定目标数量
        empty = Upgrade()
        if maxlvl_check():                         #完成了一个大丸子
            finished += 1
            if finished == target:
                return finished
            else:
                essence_choose()
                
    main_click_exit()   #材料耗尽，退出材料选择界面
    return finished

        

        
#全自动搓50级丸子，参数为所需丸子个数，进入友情池界面以开始
#(1479,16)
def FullAutoEXCards(cardnum):   
    Flag,Position = Base_func.match_template("FriendPointSummon",False, 0.95)
    if not(Flag):
        print("Please enter summon interface")
        sys.exit(0)
    
    finished = 0
    print("Program starts in 10 seconds, please leave your mouse")
    time.sleep(10)
    print("Program starts!")
    time.sleep(1)
    
    
    while (finished < cardnum):      
        print("Friend Point Summon Icon Found")
       
        #第一次召唤需要加载，所以加入2.5秒延迟
        full, Position = FriendPointSummon(2.5)
        
        #重复召唤直到满背包
        while not(full):
            full, Position = FriendPointSummon()
            
        fullType = FullBoxType() 
        time.sleep(1)
                    
        if fullType == "Essence":                  #概念礼装满
            full_click_enhance()
            finished = MaxLevelMaterial(finished, cardnum)
            main_click_exit()
            main_click_menu()
            menu_click_store()
            store_click_sell()
            clear_servants()
            main_click_exit()       
        elif fullType == "Servant":                #从者满
            full_click_sell()
            clear_servants()
            main_click_exit()
            main_click_menu()
            menu_click_enhance()
            enhance_click_essence()
            finished = MaxLevelMaterial(finished, cardnum)
            main_click_exit()    
        else:
            print("heraldry full")                 #纹章满
            sys.exit(0)
        
        main_click_menu()
        menu_click_summon()
        Flag = False
        while not(Flag):
            Serial.touch(45,305)
            time.sleep(0.5)
            Flag,Position = Base_func.match_template("FriendPointSummon",False, 0.95)
        print("%d Max-Level EXCard Finished" % finished)
        
    print("ALL DONE!")


            
def main():
    Base_func.init_wormhole()
    FullAutoEXCards(1)                  #参数在这里改！！！！！！！！
    

if __name__=="__main__":
    main()
    

'''
1Fuse 持续报错问题有待解决
2经验值芙芙是否需要移入保管室
3丸子50级满级后的锁定有待解决（已解决）
4友情点不足情况仍须考虑
5丸子满级，未耗尽材料，但第一个材料位置不足5个导致无法满破而影响升满50级
6背包内由于有过多种火和芙芙导致无法继续召唤
7素材较少无法批量选中，只能选中一个
'''