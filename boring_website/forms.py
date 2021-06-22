from django import forms
from .models import *

class ContactForm(forms.Form):
    name = forms.CharField(required=True, label='Name', max_length=100)
    email = forms.CharField(required=True, label='Email', max_length=100)
    message = forms.CharField(required=True, widget=forms.Textarea, label='Message', max_length=300, min_length=10)
