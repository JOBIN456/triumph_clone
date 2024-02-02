from django.urls import path
from .import views

urlpatterns = [
     path('',views.home,name="home"),
     path('clothes/',views.clothes,name="clothes"),
     path('owner/',views.owner,name="owner"),
     path('your_trumph/',views.your_trumph,name="your_trumph"),
     path('discover/',views.discover,name="discover"),
     path('access/',views.access,name="access"),
     path('news/',views.news,name="news"),
     path('brand/',views.brand,name="brand"),
     path('inspiration/',views.inspiration,name="inspiration"),
      path('racing/',views.racing,name="racing"),
     path('motorcycles/',views.motorcycles,name="motorcycles"),
     path('events/',views.events,name="events"),
     path('epic_a/',views.epic_a,name="epic_a"),
     path('RACE/',views.RACE,name="RACE"),
     path('MOTO/',views.MOTO,name="MOTO"),








]
