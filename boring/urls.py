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
    path('login_user', views.login_user, name="login_user"),
    path('register_user', views.register_user, name="register_user"),
    path('change_settings', views.change_settings, name="change_settings"),
    path('boring_transaction/<int:item_id>', views.boring_transaction, name="boring_transaction"),
    path('boring_return_transaction/<int:item_id>', views.boring_return_transaction, name="boring_return_transaction"),
    path('filter_items/<slug:item_type>', views.filter_items, name="filter_items"),
    path('boring_admin', views.boring_admin, name="boring_admin"),
    path('delete_contact_box/<int:contact_box_id>', views.delete_contact_box, name="delete_contact_box" ),
    path('create_question', views.create_question, name="create_question"),
    path('create_answer/<int:question_id>', views.create_answer, name="create_answer"),
    path('delete_question/<int:question_id>', views.delete_question, name="delete_question" ),
    path('delete_answer/<int:answer_id>', views.delete_answer, name="delete_answer" ),

]