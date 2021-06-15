from typing import Optional
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ManyToManyField
# Create your models here.
class BoringUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    boring_coins = models.IntegerField(default=100)
    boring_diamonds = models.IntegerField(default=10)
    bio = models.TextField(blank=True)
    level = models.IntegerField(default=0)
    def __str__(self):
        return f"Name: {self.user.username}, Coins: {self.boring_coins} | {self.boring_diamonds}"
class Game(models.Model):
    class GameCategory(models.TextChoices):    # Category
        USELESS = 0
        CREATIVE = 1
        BORING = 2
        FRUSTRATION = 3
    name = models.CharField(max_length = 30)
    description = models.CharField(max_length = 150)
    iconClass1 = models.CharField(max_length = 5, blank=True, default='')
    iconClass2 = models.CharField(max_length = 15, blank=True, default='')
    function = models.CharField(max_length = 100, default='')
    points_per_win = models.IntegerField(default = False)
    likes = models.IntegerField(default = 0)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.IntegerField(choices=GameCategory.choices, default=False)
    user = models.ForeignKey(BoringUser, on_delete=models.CASCADE, related_name="games")
    #a
    #gameObj.GameCategory.choices
    #[('1', 'Useless'), ('2', 'Creative'), ('3', 'Boring'), ('4', 'Frustration')] 
    # Guide
    def getCat(self):
        return self.GameCategory.choices[self.category]
    def __str__(self):
        return f"{self.name} - Description: {self.description[:15]}... - Active: {self.active} ."
class Post(models.Model):
    title = models.CharField(max_length = 30)
    description = models.TextField(max_length = 150)
    views = models.IntegerField(default = 0)
    likes = models.IntegerField(default = 0)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    short_description = models.CharField(max_length = 15, default='Details')
    user = models.ForeignKey(BoringUser, on_delete=models.CASCADE, related_name="posts")
    def __str__(self):
        return f"{self.title} - Description: {self.description[:15]}... - Active: {self.active} ."
class Comment(models.Model):
    user = models.ForeignKey(BoringUser, on_delete=models.CASCADE, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length = 250)
    likes = models.IntegerField(default=0)
class Item(models.Model):
    user = ManyToManyField(BoringUser)
    price_coins = models.IntegerField(blank=True)
    price_diamonds = models.IntegerField(blank=True)
    description = models.TextField(max_length = 150)