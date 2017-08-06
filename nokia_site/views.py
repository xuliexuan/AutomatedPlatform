# -*- coding: utf-8 -*-

# Create your views here.
from django.shortcuts import render, HttpResponse, render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView
from nokia_site import models

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

    # def get_context_data(self, **kwargs):
    #     context = super(HomePageView, self).get_context_data(**kwargs)
    #     context['glucose_count'] = Glucose.objects.count()
    #
    #     return context




