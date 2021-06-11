from django.shortcuts import render
from django.http import HttpResponse
from .models import Game, Post

# Create your views here.
def profile_page_view(request):
    return render(request, 'boring/profile.html')
def games_page_view(request):
    return render(request, 'boring/games.html')
def posts_page_view(request):
    context = {'posts': Post.objects.all().filter(active=True)}
    return render(request, 'boring/posts.html', context)