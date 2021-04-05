from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

class Address (forms.Form):
    address = forms.CharField()
    country = CountryField(blank_label = 'select country').formfield(widget = CountrySelectWidget)