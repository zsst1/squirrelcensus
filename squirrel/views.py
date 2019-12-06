from django.shortcuts import render
from django.http import HttpResponse
from .models import Sighting
from django.template import loader

def map(request):
    template = loader.get_template('squirrel/map.html')
    context = {} 
    return HttpResponse(template.render(context,request))


def sightings(request):
    item_list = Sighting.objects.all()
    template_sightings =  loader.get_template('squirrel/sightings.html')
    context = {'item_list' : item_list }
    return HttpResponse(template_sightings.render(context,request))


def update(request):
    return HttpResponse('update')


def add(request):
    return HttpResponse('add')


def stats(request):
    return HttpResponse('stats')





