# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     serializer
   Description :
   Author :       wsm
   date：          19-2-6
-------------------------------------------------
   Change Activity:
                   19-2-6:
-------------------------------------------------
"""
__author__ = 'wsm'


from rest_framework import serializers

from goods.models import Goods, GoodsCategory


# 类似于 form 但可以序列化成 json
# class GoodsSerializer(serializers.Serializer):
#     name = serializers.CharField(required=True, max_length=100)
#     click_num = serializers.IntegerField(default=0)
#     goods_front_image = serializers.ImageField()

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = GoodsCategory
        fields = '__all__'


class GoodsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Goods
        # fields = ('name', 'click_num', 'market_price', 'add_time')
        fields = '__all__'