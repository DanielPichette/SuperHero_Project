from django.shortcuts import render
from django.http import HttpResponse
from .models import Hero
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
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

def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        secret_identity = request.POST.get("secret identity")
        main_power = request.POST.get("main power")
        secondary_power = request.POST.get("secondary power")
        catchphrase = request.POST.get("catchphrase")
        new_hero = Hero(name=name, secret_identity=secret_identity, main_power=main_power, secondary_power=secondary_power, catchphrase=catchphrase)
        new_hero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        return render(request, 'superheroes/create.html')
