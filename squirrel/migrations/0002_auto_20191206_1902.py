# Generated by Django 3.0 on 2019-12-06 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squirrel', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sighting',
            old_name='tail_twithces',
            new_name='tail_twitches',
        ),
    ]
