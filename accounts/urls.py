#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.conf.urls import url
from .views import login_view, SignUpView, UserSettingsView
from django.contrib.auth.views import (
    password_reset,
    password_reset_done,
    logout,
    password_change,
    password_change_done,
)

urlpatterns = [
    url(regex=r'^login/$', view=login_view, name='login'),
    url(regex=r'^password/reset/$', view=password_reset, name='password_reset'),
    url(regex=r'^password/reset/done/$', view=password_reset_done, name='password_reset_done'),
    url(regex=r'^signup/', view=SignUpView.as_view(), name='signup',),
    url(regex=r'^logout/', view=logout, kwargs={'next_page': '/accounts/login/'}, name='logout'),
    url(regex=r'^password/change/$', view=password_change, name='password_change'),
    url(regex=r'^password/change/done/$', view=password_change_done, name='password_change_done'),
    url(regex=r'^settings/', view=UserSettingsView.as_view(), name='usersettings'),
]