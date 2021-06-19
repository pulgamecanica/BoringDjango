import boring
from django.db.models.query_utils import Q
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse, request
from django.contrib.auth.models import User
from .models import Game, Post, BoringUser
from .forms import GameForm, PostForm, LoginForm, RegisterForm

@login_required(login_url='./login')
def profile_page_view(request):
    return render(request, 'boring/profile.html', {'post_form': PostForm(), 'game_form': GameForm()})

def login_page_view(request, message=""):
    if request.user.is_authenticated:
        return profile_page_view(request)
    return render(request, 'boring/login.html', {'login_form': LoginForm(), 'register_form': RegisterForm(), 'message': message})

def logout_page_view(request):
    logout(request)
    return render(request, 'boring_website/home.html')

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return profile_page_view(request)
            else:
                return login_page_view(request, message = "Invalid Credentials")
    return login_page_view(request, message= "Something went wrong!")

def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] != form.cleaned_data['password_confirmation']:
                return login_page_view(request, message="Password did not match the Password Confirmation!")
            user = User.objects.create_user(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            BoringUser.objects.create(user=user, bio=form.cleaned_data['bio'])
            if user is not None:
                login(request, user)
                return profile_page_view(request)
    return login_page_view(request, message= "Something went wrong!")

@login_required(login_url='./login')
def games_page_view(request):
    context = {'games': Game.objects.all().filter(user = request.user.boringuser)}
    return render(request, 'boring/games.html', context)

@login_required(login_url='./login')
def game_page_view(request, game_id):
    game = Game.objects.get(pk=game_id)
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            gameUpdate = Game.objects.filter(pk=game_id)
            name = form.cleaned_data['name']
            if name:
                gameUpdate.update(name = name)
            description = form.cleaned_data['description']
            if description:
                gameUpdate.update(description = description)
            iconClass1 = form.cleaned_data['iconClass1']
            if iconClass1:
                gameUpdate.update(iconClass1 = iconClass1)
            iconClass2 = form.cleaned_data['iconClass2']
            if iconClass2 :
                gameUpdate.update(iconClass2 = iconClass2)
            function = form.cleaned_data['function']
            if function:
                gameUpdate.update(function = function)
            points_per_win = form.cleaned_data['points_per_win']
            if points_per_win:
                gameUpdate.update(points_per_win = points_per_win)
            gameUpdate.update(active = form.cleaned_data['active'])
            gameUpdate.update(category = form.cleaned_data['category'])
            return games_page_view(request)
    else:
        form = GameForm()
    game.save
    return render(request, 'boring/game.html', {'game': game, 'form': form})

@login_required(login_url='./login')
def create_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            game = Game.objects.create(name = form.cleaned_data['name'], description = form.cleaned_data['description'], iconClass1 = form.cleaned_data['iconClass1'], iconClass2 = form.cleaned_data['iconClass2'], function = form.cleaned_data['function'], points_per_win = form.cleaned_data['points_per_win'], active = form.cleaned_data['active'], category = form.cleaned_data['category'], user = request.user.boringuser)
            if game.save:
                print("GAME CREATED!!!!!!!!\n"*10)
    return games_page_view(request)

@login_required(login_url='./login')
def posts_page_view(request):
    context = {'posts': Post.objects.all().filter(user = request.user.boringuser)}
    return render(request, 'boring/posts.html', context)

@login_required(login_url='./login')
def post_page_view(request, post_id):
    context = {'post': Post.objects.get(pk=post_id)}
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            postUpdate = Post.objects.filter(pk=post_id)
            title = form.cleaned_data['title']
            if title:
                postUpdate.update(title = title)
            description = form.cleaned_data['description']
            if description:
                postUpdate.update(description = description)
            short_description = form.cleaned_data['short_description']
            if short_description:
                postUpdate.update(short_description = short_description)
            postUpdate.update(active = form.cleaned_data['active'])
            context['form'] = form
        return posts_page_view(request)
    else:
        context['form'] = PostForm()
    return render(request, 'boring/post.html', context)

@login_required(login_url='./login')
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # game = Game.objects.create(name = form.cleaned_data['name'], description = form.cleaned_data['description'], iconClass1 = form.cleaned_data['iconClass1'], iconClass2 = form.cleaned_data['iconClass2'], function = form.cleaned_data['function'], points_per_win = form.cleaned_data['points_per_win'], active = form.cleaned_data['active'], category = form.cleaned_data['category'], user = request.user.id)
            post = Post.objects.create(title=form.cleaned_data['title'], description=form.cleaned_data['description'], active=form.cleaned_data['active'], short_description=form.cleaned_data['short_description'], user=request.user.boringuser)
            if post.save:
                print("POST CREATED!!!!!!!!\n"*10)
    return posts_page_view(request)

@login_required(login_url='./login')
def delete_game(request, game_id):
    Game.objects.get(pk=game_id).delete()
    return profile_page_view(request)
    
@login_required(login_url='./login')
def delete_post(request, post_id):
    Post.objects.get(pk=post_id).delete()
    return profile_page_view(request)