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
    date_of_birth = models.DateTimeField(auto_now_add=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.name}, {self.email}, description: {self.description}, {self.date_of_birth.strftime("%d/%m/%Y")}.'

class Question(models.Model):
    qustion = models.CharField(max_length=400)
    points = models.IntegerField(default=10)
    def __str__(self):
        return f'Question: {self.question}, {self.points}pts.'

class Answer(models.Model):
    description = models.CharField(max_length=300)
    is_correct = models.BooleanField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    def __str__(self):
        return f'Answer: {self.description}, {self.is_correct}.'

class Review(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
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
    comments = models.CharField(max_length=300, blank=True)
    review = models.ForeignKey(Review, on_delete=CASCADE)
    def __str__(self):
        return f'{self.element}, {self.grade}.0%.'