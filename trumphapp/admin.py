from django.contrib import admin
from .models import Category,Bike,BikeDetails
# Register your models here.
admin.site.register(Category)
admin.site.register(Bike)
admin.site.register(BikeDetails)

