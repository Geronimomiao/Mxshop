# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     views_base
   Description :
   Author :       wsm
   date：          19-2-6
-------------------------------------------------
   Change Activity:
                   19-2-6:
-------------------------------------------------
"""
__author__ = 'wsm'

import json

from django.views.generic.base import View
from django.http import HttpResponse, JsonResponse

from goods.models import Goods

# class GoodsListView(View):
#     def get(self, request):
#         '''
#         通过 django 的 view 实现商品列表页
#         :param request:
#         :return:
#         '''
#         json_list = []
#         goods = Goods.objects.all()[:10]
#         for good in goods:
#             json_dict = {}
#             json_dict['name'] = good.name
#             json_dict['category'] = good.category.name
#             json_dict['market_price'] = good.market_price
#             json_list.append(json_dict)
#
#         return HttpResponse(json.dumps(json_list), content_type='application/json')

# from django.forms.models import model_to_dict
#
# class GoodsListView(View):
#
#     def get(self):
#         json_list = []
#         goods = Goods.objects.all()[:10]
#         for good in goods:
#             json_dict = model_to_dict(good)
#             json_list.append(json_dict)
#
#         return HttpResponse(json.dumps(json_list), content_type='application/json')

from django.core import serializers

class GoodsListView(View):

    def get(self, request):
        goods = Goods.objects.all()[:10]
        json_data = serializers.serialize('json', goods)

        return HttpResponse(json_data, content_type='application/json')