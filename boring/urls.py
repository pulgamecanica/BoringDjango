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
    path('create_new_post', views.create_post, name="create_new_post" ),
    path('create_new_game', views.create_game, name="create_new_game" ),
    path('delete_game/<int:game_id>', views.delete_game, name="delete_game" ),
    path('delete_post/<int:post_id>', views.delete_post, name="delete_post" ),
]