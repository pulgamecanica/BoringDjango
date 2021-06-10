from django.db import models

# Create your models here.
class Game(models.Model):
    class GameCategory(models.TextChoices):    # Category
        USELESS = 0
        CREATIVE = 1
        BORING = 2
        FRUSTRATION = 3
    name = models.CharField(max_length = 30)
    description = models.CharField(max_length = 150)
    points_per_win = models.IntegerField(default = False)
    likes = models.IntegerField(default = 0)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.IntegerField(choices=GameCategory.choices, default=False)
    #a
    #gameObj.GameCategory.choices
    #[('1', 'Useless'), ('2', 'Creative'), ('3', 'Boring'), ('4', 'Frustration')] 
    # User 
    # Hint
    # Guide
    # Icon
    # Short Description
    # Function name
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
    short_description = models.CharField(max_length = 15)
    # USER REFERENCE
    def __str__(self):
        return f"{self.title} - Description: {self.description[:15]}... - Active: {self.active} ."