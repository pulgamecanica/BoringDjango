from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponse
from .models import Game, Post, BoringUser

# Create your views here.
@login_required(login_url='./login')
def profile_page_view(request):
    return render(request, 'boring/profile.html')
@login_required(login_url='./login')
def games_page_view(request):
    context = {'games': Game.objects.all().filter(user = request.user.boringuser)}
    return render(request, 'boring/games.html', context)
@login_required(login_url='./login')
def posts_page_view(request):
    context = {'posts': Post.objects.all().filter(user = request.user.boringuser)}
    return render(request, 'boring/posts.html', context)
def login_page_view(request):
    return render(request, 'boring/login.html')
def logout_page_view(request):
    logout(request)
    return render(request, 'boring_website/home.html')
def game_page_view(request, game_id):
    context = {'game': Game.objects.get(pk=game_id)}
    return render(request, 'boring/game.html', context)
def post_page_view(request, post_id):
    context = {'post': Post.objects.get(pk=post_id)}
    return render(request, 'boring/post.html', context)
