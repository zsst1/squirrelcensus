from django.db import models

class Sighting(models.Model):
    latitude = models.DecimalField('Latitude', max_digits =  10, decimal_places = 8)
    longitude = models.DecimalField('Longitude', max_digits = 10, decimal_places = 8) 
    unique_squirrel_id = models.CharField('Unique Squirrel ID', max_length = 200)
    shift = models.CharField('Shift', max_length = 200)
    date =  models.CharField('Date', max_length = 200)
    age = models.CharField('Age', max_length = 200)
    primary_fur_color = models.CharField('Primary Fur Color', max_length = 200)
    location = models.CharField('Location', max_length = 200)
    specific_location = models.CharField('Specific Location', max_length = 200)
    running = models.BooleanField('Running', )
    chasing = models.BooleanField('Chasing', )
    climbing = models.BooleanField('Climbing', )
    eating = models.BooleanField('Eating', )
    foraging = models.BooleanField('Foraging', )
    other_activities = models.CharField('Other Activities', max_length = 200)
    kuks = models.BooleanField('Kuks', )
    quaas = models.BooleanField('Quaas', )
    moans = models.BooleanField('Moans', )
    tail_flags = models.BooleanField('Tail flags', )
    tail_twitches = models.BooleanField('Tail twitches', )
    approaches = models.BooleanField('Approaches', )
    indifferent = models.BooleanField('Indifferent', )
    runs_from = models.BooleanField('Runs from', )
