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
    price = models.IntegerField()
    description1 = models.TextField()
    description2 = models.TextField()
    description3 = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name