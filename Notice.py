# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 10:08:29 2020

@author: McLaren
"""

import Global_Config as gc
import smtplib
from email.mime.text import MIMEText

subject = "FGO脚本提示信息"  # 主题


def config_check() -> bool:
    if not gc.email_notice:
        return False
    elif gc.msg_from == "" or gc.msg_to == "" or gc.passwd == "":
        print(" Need to correctly complete email config before using email notice!")
        return False
    else:
        return True


def send_message(text="【FGO】: Detect a special drop item."):
    if not config_check():
        return
        # 正文
    msg = MIMEText(text, "plain", "utf-8")
    msg["Subject"] = subject
    msg["From"] = gc.msg_from
    msg["To"] = gc.msg_to

    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        s.login(gc.msg_from, gc.passwd)
        s.sendmail(gc.msg_from, gc.msg_to, msg.as_string())
        print("发送成功")
    except s.SMTPException:
        print("发送失败")
    finally:
        s.quit()
