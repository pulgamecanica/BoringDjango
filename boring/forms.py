from django import forms
from .models import *
class GameForm(forms.Form):
    name = forms.CharField(required=False, label='Game name', max_length=30)
    description = forms.CharField(widget=forms.Textarea, required=False, label='Game Description', max_length=150)
    iconClass1 = forms.CharField(required=False, label='Icon Class 1', max_length=5)
    iconClass2 = forms.CharField(required=False, label='Icon Class 2', max_length=15)
    function = forms.CharField(required=False, label='Function', max_length=100)
    points_per_win = forms.IntegerField(required=False, label="Point per Win")
    active = forms.BooleanField(required=False)
    category = forms.ChoiceField(label="Category", choices=Game.GameCategory.choices, required=False)
class PostForm(forms.Form):
    title = forms.CharField(required=False, label='Post title', max_length=30)
    description = forms.CharField(widget=forms.Textarea, required=False, label='Post Description', max_length=150)
    short_description = forms.CharField(required=False, label='Post Short Description', max_length=15)
    active = forms.BooleanField(required=False)
