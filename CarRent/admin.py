from django.contrib import admin
from .models import Car

# class TransmissionTypeAdmin(admin.ModelAdmin):
#     list_display = ['name', 'slug']
#     prepopulated_fields = {'slug':('name',)}

# admin.site.register(TransmissionType, TransmissionTypeAdmin)


# class CarTypeAdmin(admin.ModelAdmin):
#     list_display = ['name', 'slug']
#     prepopulated_fields = {'slug':('name',)}

# admin.site.register(CarType, CarTypeAdmin)


# class FuelTypeAdmin(admin.ModelAdmin):
#     list_display = ['name', 'slug']
#     prepopulated_fields = {'slug':('name',)}

# admin.site.register(FuelType, FuelTypeAdmin)


class CarAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'photo', 'location', 'available', 'seats']
    list_filter = ['available']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Car, CarAdmin)
