from django.shortcuts import render, redirect, get_object_or_404
from .models import Person, Car, Rent
from .forms import FormContact
from django.db.models import Q
from .forms import FormContact, CarForm, LoginForm, SignUpForm
from django.http import HttpResponse
from IPython import embed
from django.conf import settings
import os
from django.contrib.auth import authenticate, login, logout
from django.views.generic import UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
# Create your views here


def serve_base(request):
    return render(request=request, template_name='base.html', context={})

def serve_cars(request):
    cars = list(Car.objects.all())
    cars_manu = {car.manufacturer for car in cars}
    orderby = request.GET.get('orderby', False)
    find_by_manufacturer = request.GET.get("find_by_manufacturer", False)
    if orderby or find_by_manufacturer:
        try:
            if orderby:
                cars = list(Car.objects.all().order_by(orderby))
            elif find_by_manufacturer:
                cars = list(Car.objects.filter(manufacturer__iexact = find_by_manufacturer))
        except Exception as e:
            return render(request=request, template_name='showcarsprac.html', context={'cars':cars, "error":e, "cars_manu":cars_manu})
        
    else:
        cars = list(Car.objects.all())
    return render(request=request, template_name='showcarsprac.html', context={'cars':cars, "cars_manu": cars_manu})

def serve_car_id(request):
    carid = request.GET.get('carid', False)
    if carid:
        try:
            car = Car.objects.get(plate_id = carid)
            return render(request=request, template_name='car_id.html', context={"car":car})
        except Exception as e:

            return render(request=request, template_name='car_id.html', context={'error_message' : e})
        
    else:
        return render(request=request, template_name='car_id.html', context={})

def serve_search_bar(request):
    search = request.GET.get('search', False)
    minsearch, maxsearch = (request.GET.get("min", False), request.GET.get("max", False))
    print(minsearch)
   
    if search and minsearch and maxsearch:
        cars = Car.objects.filter(manufacturer__icontains = search).filter(Q(cost__gt = int(minsearch)-1) & Q(cost__lt = int(maxsearch)+1))
    elif search:
        cars = Car.objects.filter(manufacturer__icontains = search)
    elif minsearch and maxsearch:
        cars = Car.objects.filter(Q(cost__gt = int(minsearch)-1) & Q(cost__lt = int(maxsearch)+1))
    else:
        cars = False
    return render(request=request, template_name='search.html', context={"cars": cars})

def serve_contact(request):  
    if request.method == 'GET':
        return render(request=request, template_name='contact.html', context={'form': FormContact})
    elif request.method == 'POST' :
        form = FormContact(request.POST, request.FILES)
        if form.is_valid():
            img = form.cleaned_data['img']
            imgnumber = len(os.listdir(str(settings.BASE_DIR) + r'\my_app\assets')) + 1
            path = str(settings.BASE_DIR) + r'\my_app\assets\img' + f"{imgnumber}.jpg"
            with open(path, "wb") as fh:
                for chunk in img.chunks():
                    fh.write(chunk)

        return render(request=request, template_name='contact.html', context={'form': form})


@login_required
def add_car(request):
    user = request.user
    person = Person.objects.get(id=user.id)
    form = CarForm()
    form.fields['owner'].choices = [(user, user.username)]  

    if request.method == 'POST':
        form = CarForm(request.POST)
        form.fields['owner'].choices = (user, user.username)
        form.initial['owner'] = person
        if form.is_valid():
            form.save()
            return redirect('base')

    return render(request=request, template_name='form.html', context={'form': form})



def update_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    user = request.user
    if car.owner != user:
        return render(request=request, template_name='nicetry.html', context={})
    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        form.fields['owner'].disabled = True
        form.initial['owner'] = car.owner
        if form.is_valid():
            form.save()
            return redirect('base')
    else:
        form = CarForm(instance=car)
        form.fields['owner'].disabled = True
        form.initial['owner'] = car.owner
    return render(request, template_name='form.html', context={'form': form})
      
@login_required
def owner_cars(request):
    user = request.user
    cars = Car.objects.filter(owner__id = user.id)
    return render(request=request, template_name='owner_cars.html', context={'cars': cars})


def test_update(request, car_id):
    car = get_object_or_404(Car, id=car_id)

    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        form.fields['owner'].disabled = True
        form.initial['owner'] = car.owner
        if form.is_valid():
            form.save()
            return redirect('base')
    else:
        form = CarForm(instance=car)
        form.fields['owner'].disabled = True
        form.initial['owner'] = car.owner
        

    return render(request=request, template_name='form.html', context={'form': form})

@unauthenticated_user
def signup(request):
    if request.method == 'POST':
        user = SignUpForm(request.POST)
        if not user.is_valid():
            return render(request=request, template_name='form.html', context={'form' : user})
        elif user.is_valid():
            user.save()
            username = user.cleaned_data.get('username')
            password = user.cleaned_data.get('password1')
            user_authenticate = authenticate(request, username=username, password=password)
            login(request, user_authenticate)
            return redirect('base')

    return render(request=request, template_name='form.html', context={'form': SignUpForm})
@unauthenticated_user    
def serve_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('base')  
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, template_name='form.html', context={'form': form})


def testing(request):
    return render(request, template_name='test.html', context={})


def site_logout(request):
    if request.method == 'GET':
        logout(request)
        return redirect('base')