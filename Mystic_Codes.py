# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 22:46:30 2020

@author: McLaren
"""

import sys
import Serial_wormhole as Serial
import Global_Config as gc

sys.path.append(gc.default_dir)


# 换人服
def Chaldea_Combat_Uniform(*args):
    def Hanlder(*args):
        if args[0] == 1:  # 加攻
            Serial.touch(gc.position["MasterSkillLeftBias"], gc.position["MasterSkillVerticalPosition"])
        elif args[0] == 2:  # 眩晕
            Serial.touch(gc.position["MasterSkillLeftBias"] + gc.position["MasterSkillGap"],
                         gc.position["MasterSkillVerticalPosition"])
        elif args[0] == 3:  # 换人
            Serial.touch(gc.position["MasterSkillLeftBias"] + gc.position["MasterSkillGap"] * 2,
                         gc.position["MasterSkillVerticalPosition"])
            Serial.touch(
                gc.position["ChangeOrderServantLeftBias"] + (args[2] + 2) * gc.position["ChangeOrderServantGap"],
                gc.position["ChangeOrderServantVerticalPosition"])
            Serial.touch(
                gc.position["ChangeOrderServantLeftBias"] + (args[1] - 1) * gc.position["ChangeOrderServantGap"],
                gc.position["ChangeOrderServantVerticalPosition"])
            Serial.touch_button(gc.button["ChangeOrderDecideButton"])

    Hanlder(*args)


# 热带夏日
def Tropical_Summer(*args):
    def Hanlder(*args):
        if args[0] == 1:
            Serial.touch(gc.position["MasterSkillLeftBias"], gc.position["MasterSkillVerticalPosition"])
            Position = (gc.position["SelectCharacterLeftBias"] + (args[1] - 1) * gc.position["SelectCharacterGap"],
                        gc.position["SelectCharacterVerticalPosition"])  # 蓝魔放与宝具威力提升，技能选人
            Serial.touch(Position[0], Position[1])
        elif args[0] == 2:
            Serial.touch(gc.position["MasterSkillLeftBias"] + gc.position["MasterSkillGap"],
                         gc.position["MasterSkillVerticalPosition"])
            Position = (gc.position["SelectCharacterLeftBias"] + (args[1] - 1) * gc.position["SelectCharacterGap"],
                        gc.position["SelectCharacterVerticalPosition"])  # 蓝卡暴击星集中度提升，技能选人
            Serial.touch(Position[0], Position[1])
        elif args[0] == 3:
            Serial.touch(gc.position["MasterSkillLeftBias"] + gc.position["MasterSkillGap"] * 2,
                         gc.position["MasterSkillVerticalPosition"])
            Position = (gc.position["SelectCharacterLeftBias"] + (args[1] - 1) * gc.position["SelectCharacterGap"],
                        gc.position["SelectCharacterVerticalPosition"])  # 充能10%，技能选人
            Serial.touch(Position[0], Position[1])

    Hanlder(*args)


# 模板
def Template(*args):
    def Hanlder(*args):
        if args[0] == 1:
            Serial.touch(gc.position["MasterSkillLeftBias"], gc.position["MasterSkillVerticalPosition"])
            # 写一技能要点的位置，可加参数
        elif args[0] == 2:
            Serial.touch(gc.position["MasterSkillLeftBias"] + gc.position["MasterSkillGap"],
                         gc.position["MasterSkillVerticalPosition"])
            # 写二技能要点的位置，可加参数
        elif args[0] == 3:
            Serial.touch(gc.position["MasterSkillLeftBias"] + gc.position["MasterSkillGap"] * 2,
                         gc.position["MasterSkillVerticalPosition"])
            # 写三技能要点的位置，可加参数

    Hanlder(*args)
