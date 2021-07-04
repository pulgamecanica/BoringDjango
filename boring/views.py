import boring
from django.http.response import JsonResponse
from django.core.serializers import serialize
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse, request
from django.contrib.auth.models import User
from boring_website.models import ContactBox, QuizzSubmission, Review, Question, Answer
from .models import Game, Post, BoringUser, Item
from .forms import GameForm, PostForm, LoginForm, RegisterForm, SettingsForm, QuestionForm, AnswerForm

@login_required(login_url='./login')
def profile_page_view(request, message=""):
    return render(request, 'boring/profile.html', {'message': message, 'post_form': PostForm(), 'game_form': GameForm(), 'settings_form': SettingsForm(), 'shop': Item.objects.all(), 'categories': [category[0] for category in Item.ItemType.choices]})

def login_page_view(request, message=""):
    if request.user.is_authenticated:
        return profile_page_view(request)
    return render(request, 'boring/login.html', {'login_form': LoginForm(), 'register_form': RegisterForm(), 'message': message})

def logout_page_view(request):
    logout(request)
    return login_page_view(request, "Logged out...")

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return profile_page_view(request, message=f"Welcome Back {user.username}.")
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
                return profile_page_view(request, message="Welcome!")
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
            if request.user.boringuser.buy_game():
                game = Game.objects.create(name = form.cleaned_data['name'], description = form.cleaned_data['description'], iconClass1 = form.cleaned_data['iconClass1'], iconClass2 = form.cleaned_data['iconClass2'], function = form.cleaned_data['function'], points_per_win = form.cleaned_data['points_per_win'], active = form.cleaned_data['active'], category = form.cleaned_data['category'], user = request.user.boringuser)
                game.save()
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
            if request.user.boringuser.buy_post():
                post = Post.objects.create(title=form.cleaned_data['title'], description=form.cleaned_data['description'], active=form.cleaned_data['active'], short_description=form.cleaned_data['short_description'], user=request.user.boringuser)
                post.save()
    return posts_page_view(request)

@login_required(login_url='./login')
def delete_game(request, game_id):
    Game.objects.get(pk=game_id).delete()
    return profile_page_view(request)
    
@login_required(login_url='./login')
def delete_post(request, post_id):
    Post.objects.get(pk=post_id).delete()
    return profile_page_view(request)

@login_required(login_url='./login')
def change_settings(request):
    if request.method == 'POST':
        form = SettingsForm(request.POST)
        if form.is_valid():
            user = User.objects.get(id=request.user.id)
            boring_user = BoringUser.objects.get(user=request.user)
            username = form.cleaned_data['username']
            old_password = form.cleaned_data['old_password']
            new_password = form.cleaned_data['new_password']
            password_confirmation = form.cleaned_data['password_confirmation']
            bio = form.cleaned_data['bio']
            if bio:
                boring_user.bio = bio
            if new_password:
                if authenticate(username=user.username, password=old_password) is not None:
                    if new_password == password_confirmation:
                        user.set_password(new_password)
                    else:
                        return profile_page_view(request, message="The new password must match the password confirmation!")
                else:
                    return profile_page_view(request, message="Invalid credentials!")
            if user.username != username:
                user.username = username
            user.save()
            boring_user.save()
            return profile_page_view(request, message="Updated!")
    return profile_page_view(request, message="We couldn't update the settings :( !")

@login_required(login_url='./login')
def boring_transaction(request, item_id):
    item = Item.objects.get(pk=item_id)
    if request.user.boringuser.boring_transaction(item):
        return profile_page_view(request, message=f"Item: {item.name}, bought! :D.")
    else:
        return profile_page_view(request, message="Sorry, something went wrong! :/....")

@login_required(login_url='./login')
def boring_return_transaction(request, item_id):
    item = Item.objects.get(pk=item_id)
    if request.user.boringuser.boring_return_transaction(item):
        return profile_page_view(request, message=f"Item: {item.name}, Sold!! :D.")
    else:
        return profile_page_view(request, message="Sorry, something went wrong! :/....")

@login_required(login_url='./login')
def filter_items(request, item_type):
    if item_type.capitalize() in [type[0] for type in Item.ItemType.choices]:
        response = {'items': serialize('json', Item.objects.filter(type=item_type))}
    else:
        response = {'items': serialize('json', Item.objects.all())}
    return JsonResponse(response, status=200)

@login_required(login_url='./login')
def boring_admin(request):
    if not request.user.boringuser.is_admin:
        return profile_page_view(request, "Sorry, you are not an Admin")
    return render(request, 'boring/boring_admin.html', {'contact_boxes': ContactBox.objects.all() ,'reviews': Review.objects.all(), 'questions': Question.objects.all() ,'question_form': QuestionForm(), 'answer_form': AnswerForm(), 'submissions': QuizzSubmission.objects.all()})

@login_required(login_url='./login')
def delete_contact_box(request, contact_box_id):
    if not request.user.boringuser.is_admin:
        return profile_page_view(request, "Sorry, you are not an Admin")
    ContactBox.objects.get(pk=contact_box_id).delete()
    return boring_admin(request)

@login_required(login_url='./login')
def create_question(request):
    if not request.user.boringuser.is_admin:
        return profile_page_view(request, "Sorry, you are not an Admin")
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = Question(question=form.cleaned_data['question'], points=form.cleaned_data['points'])
            question.save()
    return boring_admin(request)

@login_required(login_url='./login')
def create_answer(request, question_id):
    if not request.user.boringuser.is_admin:
        return profile_page_view(request, "Sorry, you are not an Admin")
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            question = Question.objects.get(pk=question_id)
            answer = Answer(description=form.cleaned_data['description'], is_correct=form.cleaned_data['is_correct'], question=question)
            answer.save()
    return boring_admin(request)
@login_required(login_url='./login')
def delete_question(request, question_id):
    if not request.user.boringuser.is_admin:
        return profile_page_view(request, "Sorry, you are not an Admin")
    Question.objects.get(pk=question_id).delete()
    return boring_admin(request)

@login_required(login_url='./login')
def delete_answer(request, answer_id):
    if not request.user.boringuser.is_admin:
        return profile_page_view(request, "Sorry, you are not an Admin")
    Answer.objects.get(pk=answer_id).delete()
    return boring_admin(request)
