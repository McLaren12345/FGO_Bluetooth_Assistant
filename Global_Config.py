# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 22:16:33 2021

@author: Paul
"""
import win32con, win32api


default_dir = r"G:\FGO\FGO_Bluetooth_Assistant"
template_path_str = "G:/FGO/FGO_Bluetooth_Assistant/Template/"
const_phone = "iPhone12"




config = {"iPhone6":{"name":"Wormhole(iPhone)","length":1122,"bias":0},
          "iPhone12":{"name":"Wormhole(Paul)","length":1357,"bias":117}}

const_position = win32api.GetSystemMetrics(win32con.SM_CXSCREEN) - \
                    (config[const_phone]["length"] - config[const_phone]["bias"] - 21)
                    
const_interface_origin = (const_position+21+config[const_phone]["bias"], 0+16)


num_GoldApple_used = num_SilverApple_used = num_Craft = 0



#请修改变量default_dir，template_path_str，const_phone
#default_dir为你的程序根目录
#template_path_str可通过下方函数得到，函数参数为修改后的default_dir，结果输出在终端
#const_phone为你的设备型号，config有待完善

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