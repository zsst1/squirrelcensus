from django.shortcuts import render
from django.http import HttpResponse
from .models import Sighting
from django.template import loader
from django.shortcuts import redirect
from .forms import SightingForm

def map(request):
    sightings = Sighting.objects.all()
    template = loader.get_template('squirrel/map.html') 
    context = {'sightings' : sightings}
    return HttpResponse(template.render(context,request))


def sightings(request):
    item_list = Sighting.objects.all()
    template_sightings =  loader.get_template('squirrel/sightings.html')
    context = {
            'item_list' : item_list 
    }
    return HttpResponse(template_sightings.render(context,request))

def details(request,squirrel_id):
    squirrel = Sighting.objects.get(id = squirrel_id)
    if request.method == 'GET':
        form = SightingForm(instance = squirrel)
    context = {
            'form':form,
    }
    return render(request, 'squirrel/details.html', context)
   

def update(request,unique_squirrel_id):
    squirrel = Sighting.objects.get(unique_squirrel_id = unique_squirrel_id)
    if request.method == 'POST':
        form = SightingForm(request.POST, instance = squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'/squirrel/sightings/unique_squirrel_id')
    else:
        form = SightingForm(instance = squirrel)
    context = {
            'form' : form,
    }
    
    return render(request, 'squirrel/update.html', context)


def add(request):
    if request.method == 'POST':
        form = SightingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'squirrel/sightings/add/')
    else:
        form = SightingForm()

    context = {
            'form' : form
    }

    return render(request, 'squirrel/add.html', context)


def stats(request):
    template = loader.get_template('squirrel/stats.html')
    context = {}
    return HttpResponse(template.render(context,request))





