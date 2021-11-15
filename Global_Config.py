# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 22:16:33 2021

@author: Paul
"""
import win32con, win32api


default_dir = r"C:\Users\Paul\Desktop\FGO_Bluetooth_Assistant"
template_path_str = "C:/Users/Paul/Desktop/FGO_Bluetooth_Assistant/Template/"
const_phone = "iPhone12"


config = {"iPhone6":{"name":"Wormhole(iPhone)","width":1122,"height":649,"x_deviation":0, "y_deviation":0},
          "iPhone12":{"name":"Wormhole(Paul)","width":1357,"height":649,"x_deviation":0, "y_deviation":0},
          "iPadmini4":{"name":"Wormhole(iPad (2))","width":1122,"height":860,"x_deviation":0, "y_deviation":105}
         } 

# const_position = win32api.GetSystemMetrics(win32con.SM_CXSCREEN) - \
#                     (config[const_phone]["length"] - 21)
                    
# const_interface_origin = (const_position+21, 0+16)

const_position = win32api.GetSystemMetrics(win32con.SM_CXSCREEN) - \
                    (config[const_phone]["width"] - config[const_phone]["x_deviation"] - 21)
                    
const_interface_origin = (const_position+21+config[const_phone]["x_deviation"], 0+16+config[const_phone]["y_deviation"])

num_GoldApple_used = 0
num_SilverApple_used = 0
num_Craft = 0


enhancedFilterInit_bool = True
materialFilterInit_bool = True
servantFilterInit_bool = True



#请修改变量default_dir，template_path_str，const_phone
#default_dir为你的程序根目录
#template_path_str可通过下方函数得到，函数参数为修改后的default_dir，结果输出在终端
#const_phone为你的设备型号，config有待完善
#请勿在输入虫洞激活码后更改计算机名称，这有可能导致你的电脑被识别为一台新的计算机
#请在软件运行时打开引导式访问以防止顶部通知带来的误触
#软件开始运行前，请将python IDE最小化，将虫洞窗口锁定在顶部，打开记事本软件并且全屏化

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