#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.conf.urls import url
from .views import import_data

urlpatterns = [
    url(regex=r'^import/$', view=import_data, name='data_import'),
]