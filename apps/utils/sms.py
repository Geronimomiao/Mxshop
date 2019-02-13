# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sms
   Description :
   Author :       wsm
   date：          19-2-12
-------------------------------------------------
   Change Activity:
                   19-2-12:
-------------------------------------------------
"""
__author__ = 'wsm'

import requests, hashlib
from random import choice

class SendMessage(object):

    def __init__(self):
        self.smsapi = "http://api.smsbao.com/sms?"
        self.user = 'wangsimiao'
        self.password = self.md5('Geronimo1701')


    def md5(self, str):
        m = hashlib.md5()
        m.update(str.encode("utf8"))
        return m.hexdigest()


    def send(self, phone, code='', msg='您的验证码是{code}. 如非本人操作请忽略本短信'):
        self.phone = phone
        self.content = '[MxShop]' + msg.format(code=code)
        params = {
            'u': self.user,
            'p': self.password,
            'm': self.phone,
            'c': self.content
        }
        requests.get(self.smsapi, params=params)


if __name__ == '__main__':
    t = SendMessage()
    t.send(13001380337)