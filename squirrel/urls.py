
from . import views
from django.urls import path

urlpatterns = [
        path('', views.map, name = 'map'),
        path('sightings/', views.sightings, name = 'sightings'),
        path('add/', views.add, name =  'add'),
        path('stats/', views.stats, name = 'stats'),
        ]
