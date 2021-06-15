from django.urls import path

from . import views

app_name = 'boring'

urlpatterns = [
    path('', views.profile_page_view, name='profile'),
    path('games', views.games_page_view, name='games'),
    path('posts', views.posts_page_view, name='posts'),
    path('login', views.login_page_view, name='login'),
    path('logout', views.logout_page_view, name='logout'),
    path('game/<int:game_id>', views.game_page_view, name="game"),
    path('post/<int:post_id>', views.post_page_view, name="post"),
]