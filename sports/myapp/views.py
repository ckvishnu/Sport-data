from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from .models import *
# Create your views here.

def home(request):
    return render(request,"page.html")

def add(request):
    name=request.POST['name']
    email=request.POST['email']
    country=request.POST['country']
    game=request.POST['game']
    score=request.POST['score']
    if data.objects.filter(name=name).exists():
        player_change=data.objects.get(name=name)
        player_change.total_score+=int(score)
        player_change.number_of_games+=1
        player_change.save()
        return render(request,"page.html")
    else:
        a=1
        player_list=data(name=name,email=email,country=country,number_of_games=a,total_score=score)
        player_list.save()
        return render(request,"page.html")

def display(request):
    player_list=data.objects.all()
    return render(request,"page.html",{'player':player_list})
        

