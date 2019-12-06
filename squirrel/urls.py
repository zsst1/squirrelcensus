
from . import views
from django.urls import path

urlpatterns = [
        path('', views.map),
        path('sightings/', views.sightings),
        path('add/', views.add),
        path('<int:squirrel_id>', views.update),
        path('stats/', views.stats),
        ]
