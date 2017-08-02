#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.conf.urls import url
from .views import login_view


urlpatterns = [
    url(regex=r'^login/$', view=login_view, name='login'),

]