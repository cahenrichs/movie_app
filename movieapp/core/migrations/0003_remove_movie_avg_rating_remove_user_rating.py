# Generated by Django 4.2.4 on 2023-08-05 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_director_date_of_death'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='avg_rating',
        ),
        migrations.RemoveField(
            model_name='user',
            name='rating',
        ),
    ]
