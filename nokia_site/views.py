# -*- coding: utf-8 -*-

# Create your views here.
from django.shortcuts import render, HttpResponse, render_to_response
from django.template import RequestContext
from nokia_site import models

# Create your views here.

def index(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        # add databases
    models.UserInfo.objects.create(user=username, pwd=password)

    # read data from databses
    user_list = models.UserInfo.objects.all()

    # return HttpResponse("hello world!")
    return render(request, "index.html", {"data":user_list})


def highchartsTry(request):
    if request.method == 'GET':
        topMusics = [
            ["晴天",1329.656],
            ["告白气球",248.533],
            ["演员",175.353],
            ["Five Hundred Miles",121.012],
            ["Booty Music",111.814],
            ["超越无限",105.345],
            ["刚刚好",104.539],
            ["你还要我怎样",102.994],
            ["夜空中最亮的星",84.444],
            ["全世界谁倾听你 ",64.522],
        ]

        lists = []
        for music_info in topMusics:
            lists.append(music_info)
        return render(request, 'base.html', {'lists': lists})



