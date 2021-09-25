# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 22:16:33 2021

@author: Paul
"""
import win32api
import win32con

# 请修改变量default_dir，template_path_str，const_phone
# default_dir为你的程序根目录
# template_path_str可通过下方函数得到，函数参数为修改后的default_dir，结果输出在终端
# const_phone为你的设备型号，config有待完善

default_dir = r"G:\FGO\FGO_Bluetooth_Assistant"
template_path_str = "G:/FGO/FGO_Bluetooth_Assistant/Template/"
const_phone = "iPhone12"

# name为虫洞窗口名称，后面括号里的iPhone名称需要修改
# length为虫洞窗口拉伸到纵向649像素后，横向的像素数量，bias为两侧蓝条的宽度（版本更新后已无，写0即可）
# 以上推荐使用文件下的 WinSpy 来调试获取

config = {"iPhone6": {"name": "Wormhole(iPhone)", "length": 1122, "bias": 0},
          "iPhone12": {"name": "Wormhole(Paul)", "length": 1355, "bias": 0},
          "iPadmini4": {"name": "Wormhole(iPad (2))", "length": 1358, "bias": 117}}

const_position = win32api.GetSystemMetrics(win32con.SM_CXSCREEN) - \
                 (config[const_phone]["length"] - config[const_phone]["bias"] - 21)

const_interface_origin = (const_position + 21 + config[const_phone]["bias"], 0 + 16)

# 按键与位置全局配置区
position = {
    "CardLeftBias": 115,  # 第一张卡牌与界面左侧距离
    "CardVerticalPosition": 430,  # 卡牌距顶端垂直距离
    "CardGap": 215,  # 卡牌间距
    "NoblePhantasmLeftBias": 350,  # 第一张宝具与界面左侧距离
    "NoblePhantasmVerticalPosition": 200,  # 宝具距顶端垂直距离
    "NoblePhantasmGap": 200,  # 宝具卡牌间距
    "CharacterSkillLeftBias": 65,  # 战斗界面中英灵第一张技能按键与界面左侧距离
    "CharacterSkillVerticalPosition": 488,  # 技能按键距顶端垂直距离
    "ServantGap": 270,  # 战斗界面中英灵间距
    "CharacterSkillGap": 80,  # 技能按键间距间距
    "SelectCharacterLeftBias": 280,  # 选人界面第一个英灵与界面左侧距离
    "SelectCharacterVerticalPosition": 350,  # 选人界面英灵中心距顶端垂直距离
    "SelectCharacterGap": 250,  # 选人界面英灵间距
    "MasterSkillVerticalPosition": 266,  # 御主技能按键距顶端垂直距离
    "MasterSkillLeftBias": 760,  # 第一个御主技能按键距与界面左侧距离
    "MasterSkillGap": 80,  # 御主技能按键距顶端垂直距离
    "ChangeOrderServantLeftBias": 120,
    "ChangeOrderServantGap": 170,
    "ChangeOrderServantVerticalPosition": 300
}

button = {
    "DefaultBattlePosition": (791, 155),  # 默认的关卡位置（右上角）
    "ReenterBattleButton": (705, 475),  # “连续出击“按键
    "FeedAppleDecideButton": (710, 470),  # 吃苹果决定按键
    "RefreshFriendButton": (720, 110),  # 刷新好友按键
    "RefreshFriendDecideButton": (705, 475),  # 刷新好友决定按键
    "AttackButton": (960, 510),  # 攻击按键
    "NextStep": (986, 565),  # 下一步按键（关卡结束后确认战利品时右下角的按键）
    "RefuseFriendRequest": (235, 525),  # 拒绝好友申请按键
    "MasterSkillButton": (1010, position["MasterSkillVerticalPosition"]),  # 御主技能按键
    "StartBattleButton": (1005, 570),  # 开始战斗按键
    "ChangeOrderDecideButton": (530, 530)  # 御主换人技能决定按键
}


num_GoldApple_used = 0
num_SilverApple_used = 0
num_Craft = 0

enhancedFilterInit_bool = True
materialFilterInit_bool = True
servantFilterInit_bool = True

'''
def path_str(root_dir):
    local_str = list(root_dir)
    for i in range(len(root_dir)):
        char = root_dir[i]
        if char == "\\":
            local_str[i] = "/"
    local_str = ''.join(local_str)
    local_str += "/Template/" 
    print(local_str)
    return local_str       
    


path_str(default_dir)
'''
