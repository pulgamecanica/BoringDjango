from django import forms
from django.forms.widgets import PasswordInput
from .models import *
from boring_website.models import Question, Answer

class GameForm(forms.Form):
    name = forms.CharField(required=False, label='Game name', max_length=30)
    description = forms.CharField(widget=forms.Textarea, required=False, label='Game Description', max_length=150)
    iconClass1 = forms.CharField(required=False, label='Icon Class 1', max_length=5)
    iconClass2 = forms.CharField(required=False, label='Icon Class 2', max_length=15)
    function = forms.CharField(label='Function', widget=forms.Select(choices=FUNCTIONS), required=False)
    points_per_win = forms.IntegerField(required=False, label="Point per Win")
    active = forms.BooleanField(required=False)
    category = forms.ChoiceField(label="Category", choices=Game.GameCategory.choices, required=False)
    
class PostForm(forms.Form):
    title = forms.CharField(required=False, label='Post title', max_length=30)
    description = forms.CharField(widget=forms.Textarea, required=False, label='Post Description', max_length=150)
    short_description = forms.CharField(required=False, label='Post Short Description', max_length=15)
    active = forms.BooleanField(required=False)

class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    
class RegisterForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    password_confirmation = forms.CharField(widget=forms.PasswordInput, label="Password Confirmation")
    bio = forms.CharField(widget=forms.Textarea, label="Bio", min_length=20)

class SettingsForm(forms.Form):
    username = forms.CharField(required=False, label="Username")
    old_password = forms.CharField(required=False, widget=forms.PasswordInput, label="Old Password")
    new_password = forms.CharField(required=False, widget=forms.PasswordInput, label="New Password")
    password_confirmation = forms.CharField(required=False, widget=forms.PasswordInput, label="New Password Confirmation")
    bio = forms.CharField(required=False, widget=forms.Textarea, label="Bio", min_length=20)

class QuestionForm(forms.Form):
    question = forms.CharField(label="Question")
    points = forms.IntegerField(label="Points")

class AnswerForm(forms.Form):
    description = forms.CharField(label="Description")
    is_correct = forms.BooleanField(required=False)