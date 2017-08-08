#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.conf.urls import url
from .views import HelpPageView

urlpatterns = [
    url(regex=r'help', view=HelpPageView.as_view(), name='help'),

]