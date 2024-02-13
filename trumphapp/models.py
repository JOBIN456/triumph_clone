from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self):
        return self.name
class Bike(models.Model):
    image = models.ImageField(upload_to='bike_images/')
    name = models.CharField(max_length=200)
    price = models.IntegerField(blank=True, null=True)
    description1 = models.TextField(blank=True)
    description2 = models.TextField(blank=True)
    description3 = models.TextField(blank=True)
    cc_engine=models.IntegerField(blank=True, null=True)
    ps_peak_power=models.IntegerField(blank=True, null=True)
    torque=models.IntegerField(blank=True, null=True)
    year=models.IntegerField(blank=True, null=True)
    accesories=models.IntegerField(blank=True, null=True)
    mile_service=models.IntegerField(blank=True, null=True)
    cylinders=models.IntegerField(blank=True, null=True)
    rpm=models.IntegerField(blank=True, null=True)
    kg_wet =models.IntegerField(blank=True, null=True)
    kg_lighter = models.IntegerField(blank=True, null=True)
    nm = models.IntegerField(blank=True, null=True)
    engine = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    
	
    def __str__(self):
        return self.name