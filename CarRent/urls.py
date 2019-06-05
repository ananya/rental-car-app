from django.conf.urls import url
from . import views
from django.urls import include
from django.conf import settings

urlpatterns = [
    url(r'^$', views.car_form, name='car_new'),
]