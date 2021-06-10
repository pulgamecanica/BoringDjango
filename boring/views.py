from django.shortcuts import render
from django.http import HttpResponse
from .models import Game, Post

# Create your views here.
def home_page_view(request):
    recent_posts = [post for index, post in enumerate(Post.objects.all().filter(active=True)) if index < 2]
    context = {'game': Game.objects.all()[0], 'posts': recent_posts, 'uselessGames': Game.objects.all().filter(category=0)[:2], 'creativeGames': Game.objects.all().filter(category=1)[:2], 'boringGames': Game.objects.all().filter(category=2)[:2], 'frustrationGames': Game.objects.all().filter(category=3)[:2]}
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