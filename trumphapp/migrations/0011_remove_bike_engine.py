# Generated by Django 4.2 on 2024-02-13 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trumphapp', '0010_bike_engine'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bike',
            name='engine',
        ),
    ]
