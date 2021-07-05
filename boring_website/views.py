from boring.views import boring_admin
from django.core.serializers import serialize
from django.http.response import JsonResponse
from django.shortcuts import redirect, render

# Create your views here.
from django.http import HttpResponse
from boring.models import *
from .models import *
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

def quizz_page_view(request):
    return render(request, 'boring_website/quizz.html', {'questions': Question.objects.all()})

def posts_page_view(request):
    context = {'posts': Post.objects.all().filter(active=True)}
    return render(request, 'boring_website/posts.html', context)

def contact_message(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact = ContactBox(name=contact_form.cleaned_data['name'], sur_name=contact_form.cleaned_data['sur_name'], email=contact_form.cleaned_data['email'], description=contact_form.cleaned_data['message'], phone_number=contact_form.cleaned_data['phone_number'])
            contact.save()
            contact.date_of_birth = contact_form.cleaned_data['date_of_birth']
            contact.save()
    return home_page_view(request)

def quizz_submission(request):
    if request.method == "POST":
        submission = QuizzSubmission()
        submission.save()
        score = 0.0
        for question in Question.objects.all():
            question_submission = QuestionSubmission(submission=submission, question=question)
            question_submission.save()
            if question.type() == "open_answer":
                answer_submission = AnswerSubmission(input = request.POST[str(question.pk)], question_submission = question_submission)
                answer_submission.save()
            elif question.type() == "one_choice":
                input_answer = request.POST[str(question.pk)]
                for answer in question.answers.all():
                    if f'{question.pk}_{answer.pk}' in input_answer:
                        answer_submission = AnswerSubmission(input = answer.description, question_submission = question_submission, answer = answer)
                        if answer.is_correct:
                            score += answer.answer_points()
                        answer_submission.save()
            elif question.type() == "multiple_choice":
                input_answer = request.POST.getlist(str(question.pk))
                for answer in question.answers.all():
                    if f'{question.pk}_{answer.pk}' in input_answer:
                        answer_submission = AnswerSubmission(input = answer.description, question_submission = question_submission, answer = answer)
                        if answer.is_correct:
                            score += answer.answer_points()
                        else:
                            score -= answer.answer_points()
                        answer_submission.save()
        score = (score*100)/sum(question.points for question in Question.objects.all()) if score >= 0 else 0
        submission.final_score = score
        submission.save()
        question_submission.save()
    return render(request, 'boring_website/quizz_result.html', {'quizz_submission': submission})
def review(request):
    # return render(request, 'boring_website/review.html', {})
    r = Review()
    r.save()
    for option in ReviewElement.ReviewElementOptions:
        re = ReviewElement(element=option, review=r, grade=0)
        re.save()
    response = {'elements': serialize('json', r.elements.all()), 'options': {option[0]:option[1] for option in ReviewElement.ReviewElementOptions.choices}}
    return JsonResponse(response, status=200)
def send_review(request):
    if request.method == "POST":
        dict = request.POST.dict()
        dict.pop('csrfmiddlewaretoken')
        for key, value in dict.items():
            review = ReviewElement.objects.get(pk=int(key.split("_")[0]))
            review.grade = value
            review.save()
    return home_page_view(request)

def delete_review(request, review_id):
    Review.objects.get(pk=review_id).delete()
    return boring_admin(request)

def quizz_result(request, quizz_submission_id):
    return render(request, 'boring_website/quizz_result.html', {'quizz_submission': QuizzSubmission.objects.get(pk=quizz_submission_id)})