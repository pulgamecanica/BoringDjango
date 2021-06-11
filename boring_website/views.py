from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from boring.models import *

# Create your views here.
def home_page_view(request):
    recent_posts = [post for index, post in enumerate(Post.objects.all().filter(active=True)) if index < 2]
    game = None if len(Game.objects.all()) == 0 else Game.objects.all().order_by('likes')[0]
    post = None if len(Post.objects.all()) == 0 else Post.objects.all().order_by('likes')[0]
    context = {'post': post, 'game': game, 'posts': recent_posts, 'uselessGames': Game.objects.all().filter(category=0)[:2], 'creativeGames': Game.objects.all().filter(category=1)[:2], 'boringGames': Game.objects.all().filter(category=2)[:2], 'frustrationGames': Game.objects.all().filter(category=3)[:2]}
    return render(request, 'boring_website/home.html', context)
def games_page_view(request):
    active_games = {'games': Game.objects.all().filter(active=True), 'games_by_cat': enumerate([(category[0], category[1], Game.objects.all().filter(category=category[0]).filter(active=True)) for category in Game.GameCategory.choices])}
    return render(request, 'boring_website/games.html', active_games)
def faq_page_view(request):
    return render(request, 'boring_website/faq.html')
def about_page_view(request):
    return render(request, 'boring_website/about.html')
def posts_page_view(request):
    context = {'posts': Post.objects.all().filter(active=True)}
    return render(request, 'boring_website/posts.html', context)