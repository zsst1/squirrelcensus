import csv
from django.core.management.base import BaseCommand
from squirrel.models import Sighting

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv.file')

    def handle(self,*args, **options):
        with open(options['csv.file'],'w') as csvfile:
            writer = csv.writer(csvfile)
            field_names = [f.name for f in Sighting._meta.fields]
            writer.writerow(field_names)
            # write your header first
            for obj in Sighting.objects.all():
                row = ""
                row = [str(getattr(obj, f))  for f in field_names]
                writer.writerow(row)
