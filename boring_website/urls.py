from django.urls import path

from . import views

app_name = 'boring_website'

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('games', views.games_page_view, name='games'),
    path('faq', views.faq_page_view, name='faq'),
    path('about', views.about_page_view, name='about'),
    path('posts', views.posts_page_view, name='posts'),
    path('contact_message', views.contact_message, name='contact_message'),
]