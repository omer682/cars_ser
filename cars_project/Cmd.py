import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cars_project.settings")

import django
django.setup()
from django.db.models import Q, Min, Max, Sum, Avg
from my_app.models import Car, Person, Rent
# x = Person.objects.Cars(cost__gt = 400)
# print(x.username)

# with open('cars.csv', "r") as fh:
#     for line in fh.readlines()[1:]:
#         print(line)
#         car = line.strip().split(",")
#         Car.objects.create(plate_id=car[0], manufacturer=car[1], model=car[3], year=car[2], km=car[5], cost=car[6], gearbox= "Manual", owner_id="2")

# cars = Car.objects.filter(cost__gt = 400)

# s = Car.objects.get(plate_id = 123125)

from django.db.transaction import atomic


#1
# car = Car.objects.all().order_by("-cost")
# print(car[0].cost)
#2
# avgcar = Car.objects.aggregate(Avg('cost'))
# print(avgcar)
#3
# cheapest = Car.objects.all().order_by('cost')[0]
# print(cheapest.owner)
#4
# cars = Car.objects.filter(Q(cost__gt = 500) | Q(cost=500)).order_by('-cost')
# print(cars[len(cars)-1].cost)
#5
# car = Car.objects.all().order_by('-cost')
# car = car[0]
# owner = car.owner
# owner.first_name = 'sarit'
# owner.save()
#6
# cars = Car.objects.filter(owner__first_name__startswith = 'o')
# print(cars.count()
#7
# cars = Car.objects.filter(manufacturer__icontains = 'y')
# print(cars.count())
#8
# cars = Car.objects.filter(Q(year__gt = 2018) | Q(cost__gt = 400))
# print(cars.count())
#9
# cars = Car.objects.filter(Q(year__gt = 2018) | Q(cost__gt = 400)).aggregate(Avg('cost'))
# print(cars)
# cars = Car.objects.all()
# cars = {car.manufacturer for car in cars}
# print(cars)

# cars = Car.objects.filter(manufacturer__icontains = "a").filter(Q(cost__gt = int(99)) & Q(cost__lt = int(101)))
# print(cars[0].cost)


# import re
# s = "12121332"
# pattern = r"^\d{7,9}$"

# ans = re.findall(pattern, s)
# print(ans)
# objects = os.listdir(r"C:\Users\omer6\OneDrive\שולחן העבודה\study folders\MyDjangoCarbnb\cars_project\my_app\assets")
# num = len(objects) + 1
# print(num)
# from django.conf import settings
# imgnumber = len(os.listdir(str(settings.BASE_DIR) + r'\my_app\assets')) + 1
# print(imgnumber)

# car = Car.objects.first()
with open('cars.csv', "r") as fh:
    for line in fh.readlines()[1:]:
        print(line)
        car = line.strip().split(",")
        Car.objects.create(plate_id=car[0], manufacturer=car[1], model=car[3], year=car[2], km=car[5], cost=car[6], gearbox= "Manual", owner_id="2")