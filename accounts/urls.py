#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.conf.urls import url
from .views import login_view, SignUpView
from django.contrib.auth.views import (
    password_reset,
    password_reset_done,
    logout,
)

urlpatterns = [
    url(regex=r'^login/$', view=login_view, name='login'),
    url(regex=r'^password/reset/$', view=password_reset, name='password_reset'),
    url(regex=r'^password/reset/done/$', view=password_reset_done, name='password_reset_done'),
    url(regex=r'^signup/', view=SignUpView.as_view(), name='signup',),
    url(regex=r'^logout/$', view=logout, kwargs={'next_page': '/accounts/login/'}, name='logout'),
]