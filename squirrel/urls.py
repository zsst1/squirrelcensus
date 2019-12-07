
from . import views
from django.urls import path

urlpatterns = [
        path('', views.map),
        path('sightings/', views.sightings),
        path('add/', views.add),
        path('sightings/<int:squirrel_id>/', views.details),
        path('<int:squirrel_id>/', views.update),
        path('stats/', views.stats),
        ]
