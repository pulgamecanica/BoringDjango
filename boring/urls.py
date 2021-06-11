from django.urls import path

from . import views

app_name = 'boring'

urlpatterns = [
    path('', views.profile_page_view, name='profile'),
    path('games', views.games_page_view, name='games'),
    path('posts', views.posts_page_view, name='posts'),
]