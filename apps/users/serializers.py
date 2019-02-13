# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     serializers
   Description :
   Author :       wsm
   date：          19-2-12
-------------------------------------------------
   Change Activity:
                   19-2-12:
-------------------------------------------------
"""
__author__ = 'wsm'
import re
from datetime import datetime, timedelta

from rest_framework import serializers
from django.contrib.auth import get_user_model

from Mxshop.settings import REGEX_MOBILE
from .models import VerifyCode
from utils.sms import SendMessage

User = get_user_model()


class SmsSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=11)

    def validate_mobile(self, mobile):
        '''
        验证 手机号码
        :param data:
        :return:
        '''
        # 验证手机号码是否合法
        if not re.match(REGEX_MOBILE, mobile):
            raise serializers.ValidationError('手机号输入错误')

        # 手机是否注册
        if User.objects.filter(mobile=mobile).count():
            raise serializers.ValidationError('用户已经存在')

        # 验证码发送频率
        # one_mintes_age = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)
        # if VerifyCode.objects.filter(add_time__gt=one_mintes_age, mobile=mobile):
        #     raise serializers.ValidationError("距离上一次发送未超过60s")

        return mobile