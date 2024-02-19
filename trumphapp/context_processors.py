

from .models import Bike, Category

def navbar_data(request):
    adventure_category = Category.objects.get(name='ADVENTURE')
    adventure_bikes = Bike.objects.filter(category=adventure_category)

    classics_category = Category.objects.get(name='CLASSICS')
    classics_bikes = Bike.objects.filter(category=classics_category)

    roadster_category = Category.objects.get(name='ROADSTER')
    roadster_bikes = Bike.objects.filter(category=roadster_category)

    rocket3_category = Category.objects.get(name='ROCKET3')
    rocket3_bikes = Bike.objects.filter(category=rocket3_category)
    stealth_category = Category.objects.get(name='STEALTH_EDITION')
    stealth_bikes = Bike.objects.filter(category=stealth_category)
    sport_category = Category.objects.get(name='SPORT')
    sport_bikes = Bike.objects.filter(category=sport_category)
    chrome_category = Category.objects.get(name='CHROME COLLECTION')
    chrome_bikes = Bike.objects.filter(category= chrome_category)


    return {
        "adventure_bikes": adventure_bikes,
        "classics_bikes": classics_bikes,
        "roadster_bikes": roadster_bikes,
        "rocket3_bikes": rocket3_bikes,
        "stealth_bikes":stealth_bikes,
        "sport_bikes":sport_bikes,
        "chrome_bikes":chrome_bikes,
    }

