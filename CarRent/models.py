from django.db import models


# class TransmissionType(models.Model):
#     name = models.CharField(max_length=100, db_index=True)
#     slug = models.SlugField(max_length=100, unique=True, db_index=True)

#     class Meta:
#         ordering = ('name',)
#         verbose_name = 'transmissiontype'
#         verbose_name_plural = 'transmissiontype'

#     def __str__(self):
#         return self.name


# class CarType(models.Model):
#     name = models.CharField(max_length=100, db_index=True)
#     slug = models.SlugField(max_length=100, unique=True, db_index=True)

#     class Meta:
#         ordering = ('name',)
#         verbose_name = 'cartype'
#         verbose_name_plural = 'cartype'

#     def __str__(self):
#         return self.name


# class FuelType(models.Model):
#     name = models.CharField(max_length=100, db_index=True)
#     slug = models.SlugField(max_length=100, unique=True, db_index=True)

#     class Meta:
#         ordering = ('name',)
#         verbose_name = 'fueltype'
#         verbose_name_plural = 'fueltype'

#     def __str__(self):
#         return self.name


class Car(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    photo = models.CharField(max_length=100 blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    location = models.CharField(max_length=100, blank=True)
    available = models.BooleanField(default=True)
    seats = models.DecimalField(max_digits=10, decimal_places=0)

    DIESEL = 'Diesel'
    PETROL  = 'Petrol'

    FUEL_OPTIONS = (
        (DIESEL, DIESEL),
        (PETROL, PETROL),
    )
    
    fuel_Type = models.CharField(max_length=10, choices=FUEL_OPTIONS)
    
    AUTOMATIC = 'Automatic'
    MANUAL  = 'Manual'

    TRANSMISSION_OPTIONS = (
        (AUTOMATIC, AUTOMATIC),
        (MANUAL, MANUAL),
    )
    
    transmission = models.CharField(max_length=10, choices=TRANSMISSION_OPTIONS)
    
    HATCHBACK = 'Hatchback'
    SEDAN  = 'Sedan'
    SUV = 'SUV'
    MINISUV = 'Mini SUV'

    CAR_OPTIONS = (
        (HATCHBACK, HATCHBACK),
        (SEDAN, SEDAN),
        (SUV, SUV),
        (MINISUV, MINISUV),
    )
    
    car_Type = models.CharField(max_length=10, choices=CAR_OPTIONS)
    
    class Meta:
        ordering = ('price','name', )
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name