# Generated by Django 4.2 on 2024-02-14 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trumphapp', '0019_bikedetails_vedio_url1_bikedetails_vedio_url2'),
    ]

    operations = [
        migrations.AddField(
            model_name='bikedetails',
            name='Bore',
            field=models.CharField(blank=True, max_length=800),
        ),
        migrations.AddField(
            model_name='bikedetails',
            name='CO2_Figures',
            field=models.CharField(blank=True, max_length=4000),
        ),
        migrations.AddField(
            model_name='bikedetails',
            name='Capacity',
            field=models.CharField(blank=True, max_length=800),
        ),
        migrations.AddField(
            model_name='bikedetails',
            name='Clutch',
            field=models.CharField(blank=True, max_length=800),
        ),
        migrations.AddField(
            model_name='bikedetails',
            name='Compression',
            field=models.CharField(blank=True, max_length=800),
        ),
        migrations.AddField(
            model_name='bikedetails',
            name='Exhauste',
            field=models.CharField(blank=True, max_length=800),
        ),
        migrations.AddField(
            model_name='bikedetails',
            name='Final_Drive',
            field=models.CharField(blank=True, max_length=800),
        ),
        migrations.AddField(
            model_name='bikedetails',
            name='Frame',
            field=models.CharField(blank=True, max_length=800),
        ),
        migrations.AddField(
            model_name='bikedetails',
            name='Front_Brakes',
            field=models.CharField(blank=True, max_length=800),
        ),
        migrations.AddField(
            model_name='bikedetails',
            name='Front_Suspension',
            field=models.CharField(blank=True, max_length=800),
        ),
        migrations.AddField(
            model_name='bikedetails',
            name='Front_Tyre',
            field=models.CharField(blank=True, max_length=800),
        ),
        migrations.AddField(
            model_name='bikedetails',
            name='Front_Wheel',
            field=models.CharField(blank=True, max_length=800),
        ),
        migrations.AddField(
            model_name='bikedetails',
            name='Fuel_Consumption',
            field=models.CharField(blank=True, max_length=800),
        ),
        migrations.AddField(
            model_name='bikedetails',
            name='Handlebars',
            field=models.CharField(blank=True, max_length=800),
        ),
        migrations.AddField(
            model_name='bikedetails',
            name='Height',
            field=models.CharField(blank=True, max_length=800),
        ),
        migrations.AddField(
            model_name='bikedetails',
            name='Instrument',
            field=models.CharField(blank=True, max_length=800),
        ),
        migrations.AddField(
            model_name='bikedetails',
            name='Max_Power_EC',
            field=models.CharField(blank=True, max_length=800),
        ),
        migrations.AddField(
            model_name='bikedetails',
            name='Max_Torque_EC',
            field=models.CharField(blank=True, max_length=800),
        ),
        migrations.AddField(
            model_name='bikedetails',
            name='Rake',
            field=models.CharField(blank=True, max_length=800),
        ),
        migrations.AddField(
            model_name='bikedetails',
            name='Rear_Brakes',
            field=models.CharField(blank=True, max_length=800),
        ),
        migrations.AddField(
            model_name='bikedetails',
            name='Rear_Suspension',
            field=models.CharField(blank=True, max_length=800),
        ),
        migrations.AddField(
            model_name='bikedetails',
            name='Rear_Tyre',
            field=models.CharField(blank=True, max_length=800),
        ),
        migrations.AddField(
            model_name='bikedetails',
            name='Rear_Wheel',
            field=models.CharField(blank=True, max_length=800),
        ),
        migrations.AddField(
            model_name='bikedetails',
            name='Seat_Height',
            field=models.CharField(blank=True, max_length=800),
        ),
        migrations.AddField(
            model_name='bikedetails',
            name='Service_Interval',
            field=models.CharField(blank=True, max_length=800),
        ),
        migrations.AddField(
            model_name='bikedetails',
            name='Swingarm',
            field=models.CharField(blank=True, max_length=800),
        ),
        migrations.AddField(
            model_name='bikedetails',
            name='System',
            field=models.CharField(blank=True, max_length=800),
        ),
        migrations.AddField(
            model_name='bikedetails',
            name='Tank',
            field=models.CharField(blank=True, max_length=800),
        ),
        migrations.AddField(
            model_name='bikedetails',
            name='Trail',
            field=models.CharField(blank=True, max_length=800),
        ),
        migrations.AddField(
            model_name='bikedetails',
            name='Wet_Weight',
            field=models.CharField(blank=True, max_length=800),
        ),
        migrations.AddField(
            model_name='bikedetails',
            name='Wheelbase',
            field=models.CharField(blank=True, max_length=800),
        ),
        migrations.AddField(
            model_name='bikedetails',
            name='type',
            field=models.CharField(blank=True, max_length=800),
        ),
    ]