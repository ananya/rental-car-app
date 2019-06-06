from django.shortcuts import render, redirect
from .models import Car
from .forms import CarForm
import requests
import json

def get_cars():
    url = "https://api.sheety.co/311576ae-321a-43e3-9a5b-61b3ac373d85"
    response = requests.get(url)
    cars = json.loads(response.content.decode('utf-8'))
    return cars

def update_cars(requests):
    cars = get_cars()

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
            return redirect('car_list')
    else:
        form = CarForm()
    return render(request, 'car/car_form.html', {'form': form})


def car_list(request):
    cars = Car.objects.filter(available=True)

    context = {
        'cars': cars
    }
    return render(request, 'car/car_list.html', context)