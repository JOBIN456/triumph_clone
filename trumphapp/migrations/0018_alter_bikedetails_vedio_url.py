# Generated by Django 4.2 on 2024-02-14 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trumphapp', '0017_bikedetails_big_image_bikedetails_card_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bikedetails',
            name='vedio_url',
            field=models.URLField(blank=True, max_length=600),
        ),
    ]
