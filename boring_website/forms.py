from django import forms
from django.forms import widgets
from .models import *

class ContactForm(forms.Form):
    name = forms.CharField(required=True, label='Name', max_length=100)
    sur_name = forms.CharField(required=True, label='Sur Name', max_length=100)
    email = forms.CharField(required=True, label='Email', max_length=100)
    phone_number = forms.IntegerField(label="Phone Number")
    date_of_birth = forms.DateTimeField(input_formats=['%d/%m/%Y'],widget=forms.DateTimeInput(attrs={'class': 'datetimepicker-input','data-target': '#datetimepicker1'}))
    message = forms.CharField(required=True, widget=forms.Textarea, label='Message', max_length=300, min_length=10)