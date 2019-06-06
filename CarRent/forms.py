from django import forms
from .models import Car

class CarForm(forms.Form):
    location = forms.CharField(label='Your Location', max_length=100)
    startdate = forms.DateField(label='enter date of journey', widget=forms.SelectDateWidget)

    