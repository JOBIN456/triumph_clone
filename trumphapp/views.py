from django.shortcuts import render

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

