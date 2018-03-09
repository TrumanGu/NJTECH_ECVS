# -*- coding: utf-8 -*-
# @Time    : 2018/3/6 23:34
# @Author  : TrumanGu
# @Email   : 1227085585@qq.com
# @File    : urls.py
# @Software: PyCharm

app_name = "comment"
from django.conf.urls import include, url
from comment.views import IndexView, DetailView

urlpatterns = [
    url(r'^detail-(?P<sid>\d+)$',DetailView,name='detail'),

]
