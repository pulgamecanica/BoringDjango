from django.shortcuts import render
from django.http import HttpResponse
from .models import Game, Post

# Create your views here.
def home_page_view(request):
    context = {'game': Game.objects.all()[0]}
    return render(request, 'boring/home.html', context)
def games_page_view(request):
    return render(request, 'boring/games.html')
def faq_page_view(request):
    return render(request, 'boring/faq.html')
def about_page_view(request):
    return render(request, 'boring/about.html')
def posts_page_view(request):
    context = {'posts': Post.objects.all().filter(active=True)}
    return render(request, 'boring/posts.html', context)