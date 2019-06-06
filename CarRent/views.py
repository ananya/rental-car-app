from django.shortcuts import render, redirect
from .models import Car
from .forms import CarForm
from django.db.models import Q
import requests
import json
from django.core.paginator import Paginator
from django.shortcuts import render

def get_cars():
    url = "https://api.sheety.co/311576ae-321a-43e3-9a5b-61b3ac373d85"
    response = requests.get(url)
    cars = json.loads(response.content.decode('utf-8'))
    return cars

def update_cars(requests):
    cars = get_cars()
    print(cars)
    obj_name = ""
    obj_photo = ""
    obj_price = ""
    obj_location = ""
    obj_seats = ""
    obj_fuel_type = ""
    obj_transmission = ""
    obj_car_type = ""

    for child in cars:
        # print(child)
        obj_name = child["name"]
        # print(obj_name)
        obj_photo = child["photo"]
        obj_location = child["location"]
        obj_price = child["price"]
        obj_seats = child["seats"]
        obj_fuel_type = child["fuel_Type"]
        obj_transmission = child["transmission"]
        obj_car_type = child["car_Type"]
        
        if not Car.objects.filter(name=obj_name).exists():
            Car.objects.get_or_create(
                name=obj_name, 
                photo=obj_photo, 
                price=obj_price, 
                location=obj_location, 
                seats=obj_seats, 
                fuel_Type=obj_fuel_type, 
                transmission=obj_transmission, 
                car_Type=obj_car_type,
                )

    return redirect('car_list')

def car_form(request):
    if request.method == "POST":
        form = CarForm(request.POST)
        if form.is_valid():
            return redirect('update_cars')
    else:
        form = CarForm()
    return render(request, 'car/car_form.html', {'form': form})


def car_list(request):
    queryset = Car.objects.all()
    
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(name__icontains=query) |
            Q(location__icontains=query) |
            Q(seats__icontains=query) |
            Q(fuel_Type__icontains=query) |
            Q(transmission__icontains=query) |
            Q(car_Type__icontains=query) |
            Q(price__icontains=query)

            )


    paginator = Paginator(queryset, 6)
    page = request.GET.get('page')
    cars = paginator.get_page(page)

    
    context = {
        'cars': cars
    }
    return render(request, 'car/car_list.html', context)


