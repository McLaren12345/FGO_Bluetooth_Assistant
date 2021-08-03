# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 22:16:33 2021

@author: Paul
"""

import sys
import win32con, win32api
sys.path.append(r'C:\Users\Paul\Desktop\Modified')




const_phone = "iPhone12"

const_config = {"iPhone6":{"name":"Wormhole(iPhone)","length":1122,"bias":0},
          "iPhone12":{"name":"Wormhole(Paul)","length":1357,"bias":117}}

const_position = win32api.GetSystemMetrics(win32con.SM_CXSCREEN) - \
                    (const_config[const_phone]["length"] - const_config[const_phone]["bias"] - 21)
                    
const_interface_origin = (const_position+21+const_config[const_phone]["bias"], 0+16)



