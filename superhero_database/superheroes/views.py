from django.shortcuts import render
from django.http import HttpResponse
from .models import Hero
# Create your views here.

def index(request):
    all_heroes = Hero.objects.all()
    context = {
        'all_heroes': all_heroes
    }
    return render(request, 'superheroes/index.html', context)

def detail(request, hero_id):
    hero = Hero.objects.get(pk=hero_id)
    context = {
        'hero': hero
    }
    return render(request, 'superheroes/detail.html', context)
