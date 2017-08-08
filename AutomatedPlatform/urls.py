"""AutomatedPlatform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from core.views import HomePageView
from data_manage.views import dashboard

urlpatterns = [
    url(regex=r'^admin/', view=admin.site.urls),
    url(regex=r'^$', view=HomePageView.as_view(), name='home'),
    url(regex=r'^dashboard/$', view=dashboard, name='dashboard'),

    url(r'^accounts/', include('accounts.urls')),
    url(r'^core/', include('core.urls')),
    url(r'^data_manage/', include('data_manage.urls'))
]
