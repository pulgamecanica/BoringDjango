from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
# Create your models here.
class ContactBox(models.Model):
    name = models.CharField(max_length = 50)
    sur_name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    description = models.TextField(max_length = 300)
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.name} <{self.email}>, Description: {self.description} [{self.date_of_birth.strftime("%d/%m/%Y")}].'
        
class Question(models.Model):
    question = models.CharField(max_length=400)
    points = models.IntegerField(default=10)
    def type(self):
        if len(self.answers.all()) == 0:
            return "open_answer"
        true_options = 0
        for answer in self.answers.all():
            if answer.is_correct:
                true_options += 1
        if true_options == 1:
            return "one_choice"
        else:
            return "multiple_choice"
    def __str__(self):
        return f'{self.question}, {self.points}pts.'

class Answer(models.Model):
    description = models.CharField(max_length=300)
    is_correct = models.BooleanField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    def answer_points(self):
        return self.question.points/len(self.question.answers.filter(is_correct=True))
    def __str__(self):
        return f'{self.description}, {self.is_correct}.'

class QuizzSubmission(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    final_score = models.DecimalField(decimal_places=2, max_digits=5, default=0.0)
    def __str__(self):
        return str(self.final_score)

class QuestionSubmission(models.Model):
    submission = models.ForeignKey(QuizzSubmission, on_delete=models.CASCADE, related_name='questions_submissions')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question_submissions', blank=True, null=True)
    def __str__(self):
        return str(self.question)

class AnswerSubmission(models.Model):
    input = models.CharField(max_length=300)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='answer_submissions', blank=True, null=True)
    question_submission = models.ForeignKey(QuestionSubmission, on_delete=models.CASCADE, related_name='answer_submissions', blank=True, null=True)
    def __str__(self):
        return str(self.input)
        
class Review(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Review - {self.created_at}'
        
class ReviewElement(models.Model):
    class ReviewElementOptions(models.TextChoices):
        CLARITY = 'CL' 
        ACCURACY = 'AC'
        PRECISION = 'PR'
        COMPLEXITY = 'CM'
        AMPLITUDE = 'AM'
        LOGIC = 'LO'
        MEANINGFULLNESS = "MF"
        ORIGINALITY = "OG"
    element = models.CharField(max_length=2, choices=ReviewElementOptions.choices, default=ReviewElementOptions.ORIGINALITY)
    grade = models.IntegerField()
    comment = models.CharField(max_length=300, blank=True) #THis one has been forgotten
    review = models.ForeignKey(Review, on_delete=CASCADE, related_name='elements')
    def __str__(self):
        element_name = ""
        for choice in ReviewElement.ReviewElementOptions.choices:
            if(self.element.lower() == choice[0].lower()):
                element_name = choice[1]
        if self.comment != "":
            return f'{element_name}, {self.grade}.0%, [{self.comment}].'
        else:
            return f'{element_name}, {self.grade}.0%.'