from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from boring.models import *
from .models import ContactBox
from .forms import ContactForm

# Create your views here.
def home_page_view(request):
    contact_form = ContactForm()
    recent_posts = [post for post in Post.objects.all().filter(active=True).order_by('created_at')[:2] ]
    recent_games_by_cat = { choice[1]: Game.objects.filter(category=choice[0]).filter(active=True).order_by('created_at')[:2] for choice in Game.GameCategory.choices }
    game = None if len(Game.objects.all()) == 0 else Game.objects.all().order_by('likes')[0]
    post = None if len(Post.objects.all()) == 0 else Post.objects.all().order_by('likes')[0]
    comments = Comment.objects.order_by('created_at')
    context = {'contact_form': contact_form, 'post': post, 'game': game, 'posts': recent_posts, 'games_by_cat': recent_games_by_cat, 'comments': comments}
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

def contact_message(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact = ContactBox(name=contact_form.cleaned_data['name'], sur_name=contact_form.cleaned_data['sur_name'], email=contact_form.cleaned_data['email'], description=contact_form.cleaned_data['message'], phone_number=contact_form.cleaned_data['phone_number'], date_of_birth=contact_form.cleaned_data['date_of_birth'])
            contact.save()
    return home_page_view(request)