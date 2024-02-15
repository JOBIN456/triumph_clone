from django.urls import path
from .import views

urlpatterns = [
     path('',views.home,name="home"),
     
     path('clothes/',views.clothes,name="clothes"),
     path('owner/',views.owner,name="owner"),
     path('your_trumph/',views.your_trumph,name="your_trumph"),
     path('discover/',views.discover,name="discover"),
   
     path('news/',views.news,name="news"),
     path('brand/',views.brand,name="brand"),
     path('inspiration/',views.inspiration,name="inspiration"),
      path('racing/',views.racing,name="racing"),
     path('motorcycles/',views.motorcycles,name="motorcycles"),
     path('events/',views.events,name="events"),
     path('epic_a/',views.epic_a,name="epic_a"),
     path('RACE/',views.RACE,name="RACE"),
     path('MOTO/',views.MOTO,name="MOTO"),
     path('engine/',views.engine,name="engine"),
      path('trophy/',views.trophy,name="trophy"),
      path('testing/',views.testing,name="testing"),
     path('calender/',views.calender,name="calender"),
     path('PTR/',views.PTR,name="PTR"),
     path('MXGP/',views.MXGP,name="MXGP"),
     path('US/',views.US,name="US"),  
     path('team/',views.team,name="team"),
     path('calender1/',views.calender1,name="calender1"),
     path('brand1/',views.brand1,name="brand1"),
     path('reviews/',views.reviews,name="reviews"),
     path('dealer/',views.dealer,name="dealer"),
     path('customize/',views.customize,name="customize"),
     path('bike_details/<str:bike_name>/',views.view_bike_details, name='view_bike_details'), 
     path('model/<str:bike_name>/',views.model,name="model"),
     path('specification/<str:bike_name>/',views.specification,name="specification"),
     path('reason/<str:bike_name>/',views.reason,name="reason"),
     path('access/<str:bike_name>/',views.access,name="access"),










]
