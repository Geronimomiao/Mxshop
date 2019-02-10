# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     filters
   Description :
   Author :       wsm
   date：          19-2-7
-------------------------------------------------
   Change Activity:
                   19-2-7:
-------------------------------------------------
"""
__author__ = 'wsm'

import django_filters
from django.db.models import Q
from django_filters import rest_framework as filters

from .models import Goods

class GoodsFilter(filters.FilterSet):
    pricemin = filters.NumberFilter(field_name="shop_price", lookup_expr='gte')
    pricemax = filters.NumberFilter(field_name="shop_price", lookup_expr='lte')
    # 模糊查询
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    top_category = django_filters.NumberFilter(method='top_category_filter')

    def top_category_filter(self, queryset, name, value):
        return queryset.filter(Q(category_id=value)|Q(category__parent_category_id=value)|Q(category__parent_category__parent_category_id=value))

    class Meta:
        model = Goods
        fields = ['pricemin', 'pricemax', 'name']
