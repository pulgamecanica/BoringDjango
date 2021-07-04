from django.urls import path

from . import views

app_name = 'boring_website'

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('games', views.games_page_view, name='games'),
    path('faq', views.faq_page_view, name='faq'),
    path('quizz', views.quizz_page_view, name='quizz'),
    path('posts', views.posts_page_view, name='posts'),
    path('contact_message', views.contact_message, name='contact_message'),
    path('quizz_submission', views.quizz_submission, name='quizz_submission'),
    path('review', views.review, name='review'),
    path('send_review', views.send_review, name='send_review'),
    path('delete_review/<int:review_id>', views.delete_review, name='delete_review'),
    path('quizz_result/<int:quizz_submission_id>', views.quizz_result, name='quizz_result'),
]