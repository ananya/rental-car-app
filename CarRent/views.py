from django.shortcuts import render, redirect
from .models import TransmissionType, CarType, FuelType, Car
from .forms import CarForm

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