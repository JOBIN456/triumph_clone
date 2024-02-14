# Generated by Django 4.2 on 2024-02-14 05:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trumphapp', '0016_bikedetails_bike_alter_bikedetails_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='bikedetails',
            name='big_image',
            field=models.ImageField(null=True, upload_to='bike_images/'),
        ),
        migrations.AddField(
            model_name='bikedetails',
            name='card_image',
            field=models.ImageField(null=True, upload_to='bike_images/'),
        ),
        migrations.AddField(
            model_name='bikedetails',
            name='carousel_image3',
            field=models.ImageField(null=True, upload_to='bike_images/'),
        ),
        migrations.AddField(
            model_name='bikedetails',
            name='carousel_title1',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='bikedetails',
            name='carousel_title2',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='bikedetails',
            name='carousel_title3',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='bikedetails',
            name='cc_engine',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bikedetails',
            name='miles',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bikedetails',
            name='paragraph',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='bikedetails',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bikedetails',
            name='ps_peak_power',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bikedetails',
            name='small_image',
            field=models.ImageField(null=True, upload_to='bike_images/'),
        ),
        migrations.AddField(
            model_name='bikedetails',
            name='torque',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bikedetails',
            name='vedio_url',
            field=models.URLField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='bikedetails',
            name='video',
            field=models.FileField(null=True, upload_to='videos_uploaded', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])]),
        ),
        migrations.AlterField(
            model_name='bikedetails',
            name='carousel_image',
            field=models.ImageField(null=True, upload_to='bike_images/'),
        ),
        migrations.AlterField(
            model_name='bikedetails',
            name='carousel_image2',
            field=models.ImageField(null=True, upload_to='bike_images/'),
        ),
    ]
