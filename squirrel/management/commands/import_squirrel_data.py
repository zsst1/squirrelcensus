import csv
from django.core.management.base import BaseCommand
from squirrel.models import Sighting

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv.file')

    def handle(self,*args, **options):
        with open (options['csv.file']) as fp:
            reader = csv.DictReader(fp)
            data = list(reader)
        
        for item in data:
            s = Sighting(
                    latitude = item['X'],
                    longitude = item['Y'],
                    unique_squirrel_id = item['Unique Squirrel ID'],
                    shift = item['Shift'],
                    date = item['Date'],
                    age = item['Age'],
                    primary_fur_color = item['Primary Fur Color'],
                    location = item['Location'],
                    specific_location = item['Specific Location'],
                    running = bool(item['Running'].capitalize()),
                    chasing = bool(item['Chasing'].capitalize()),
                    climbing = bool(item['Climbing'].capitalize()),
                    eating = bool(item['Eating'].capitalize()),
                    foraging = bool(item['Foraging'].capitalize()),
                    other_activities = item['Other Activities'],
                    kuks = bool(item['Kuks'].capitalize()),
                    quaas = bool(item['Quaas'].capitalize()),
                    moans = bool(item['Moans'].capitalize()),
                    tail_flags = bool(item['Tail flags'].capitalize()),
                    tail_twitches = bool(item['Tail twitches'].capitalize()),
                    approaches = bool(item['Approaches'].capitalize()),
                    indifferent = bool(item['Indifferent'].capitalize()),
                    runs_from = bool(item['Runs from'].capitalize()),
                    )
            s.save()
