from django.shortcuts import render
from .models import Bike,Category
from django.http import JsonResponse
# Create your views here.
def home(request):
    return render(request,"home.html")


def clothes(request):
    return render(request,'clothes.html')

def owner(request):
    return render(request,'owner.html')
def your_trumph(request):
    return render(request,'your_trumph.html')
def discover(request):
    return render(request,'discover.html')

def access(request):
    return render(request,'access.html')

def news(request):
    return render(request,'news.html')

def brand(request):
    return render(request,'brand.html')

def inspiration(request):
    return render(request,'inspiration.html')

def racing(request):
    return render(request,'racing.html')


def motorcycles(request):
    return render(request,'motorcycles.html')

def events(request):
    return render(request,'events.html')

def epic_a(request):
    return render(request,'epic_a.html')

def RACE(request):
    return render(request,'RACE.html')

def MOTO(request):
    return render(request,'MOTO.html')

def engine(request):
    return render(request,'engine.html')
def engine(request):
    return render(request,'engine.html')
def trophy(request):
    return render(request,'trophy.html')
def testing(request):
    return render(request,'testing.html')
def calender(request):
    return render(request,'calender.html')
def PTR(request):
    return render(request,'PTR.html')
def MXGP(request):
    return render(request,'MXGP.html')
def US(request):
    return render(request,'US.html')
def team(request):
    return render(request,'team.html')
def calender1(request):
    return render(request,'calender1.html')

def brand1(request):
    return render(request,'brand1.html')
def reviews(request):
    return render(request,'reviews.html')
def dealer(request):
    return render(request,'dealer.html')
def customize(request):
    category_names = ['ADVENTURE', 'CLASSICS', 'ROADSTER', 'ROCKET3']
    adventure_cat = Category.objects.get(name='ADVENTURE')
    modern_cat = Category.objects.get(name='CLASSICS')
    road_cat = Category.objects.get(name="ROADSTER")
    rocket_cat = Category.objects.get(name="ROCKET3")

    adv_bike = Bike.objects.filter(category=adventure_cat)
    mod_bike = Bike.objects.filter(category=modern_cat)
    road_bike = Bike.objects.filter(category=road_cat)
    rocket_bike = Bike.objects.filter(category=rocket_cat)

    context = {
        "adv_bike": adv_bike,
        "mod_bike": mod_bike,
        "road_bike": road_bike,
        "rocket_bike": rocket_bike
    }

    return render(request, 'customize.html', context)
def view_bike_details(request):
    return render(request,'view_bike_details.html')