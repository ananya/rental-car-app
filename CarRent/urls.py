from django.conf.urls import url
from . import views
from django.urls import include
from django.conf import settings

urlpatterns = [
    url(r'^$', views.car_form, name='car_new'),
    url(r'^car/list/$', views.car_list, name='car_list'),
    url(r'^update$', views.update_cars, name='update_cars'),
]