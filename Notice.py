# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 10:08:29 2020

@author: McLaren
"""

from twilio.rest import Client

#STEP1: 去twilio.com注册账户获取token,sid. 详见：https://blog.csdn.net/qq_31801903/article/details/81060448
#STEP2: 调用函数测试下发送是否成功，手机是否收到短信
#trial acount预存15美元，每条短信0.028美元，即免费账户可以发送500条短信
auth_token = '3f2c01d7c226e883277d9f8e12bd3662'   
account_sid = 'AC1479745816c663038aadfdb5b89e65fb'

client = Client(account_sid,auth_token)

def sent_message(phone_number=17702184376,text='【FGO】: Detect a special drop item.'):
    mes = client.messages.create(
        from_='+16782939184',  #填写在active number处获得的号码 
        body=text,
        to='+86'+str(phone_number)   #填写自己的手机号码
    )
    print(" Message send OK")



