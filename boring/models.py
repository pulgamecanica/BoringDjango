from typing import Optional
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ManyToManyField

FUNCTIONS = [
    ('loveTheLogo', 'Love The Logo'),
    ('colorGame', 'colorGame'),
    ('seconds_game', 'Seconds Game'),
    ('no_you_cant_win', 'No you cant win.'),
    ('boring_switch', 'Boring Switch'),
    ('rgba_game', 'RGBA Game'),
    ('ninja', 'Ninja'),
    ('mysterious_messages', 'Mysterious Messages'),
    ('logo_click', 'Logo Click'),
    ('mysterious_emoji', 'Mysterious Emoji'),
    ('boring_rain', 'Boring Rain'),
    ('game_loading', 'Game Loading')
]

class BoringUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    boring_coins = models.IntegerField(default=100)
    boring_diamonds = models.IntegerField(default=10)
    bio = models.TextField(blank=True)
    level = models.IntegerField(default=0)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    def buy_game(self):
        if self.boringUser_wallet_check(1000, 10):
            self.boring_coins -= 1000
            self.boring_diamonds -= 10
            self.save()
            return True
        else:
            return False

    def buy_post(self):
        if self.boringUser_wallet_check(500, 0):
            self.boring_coins -= 500
            self.save()
            return True
        else:
            return False

    def boringUser_wallet_check(self, coins, diamons):
        if self.boring_coins < coins:
            return False
        if self.boring_diamonds < diamons:
            return False
        return True
    def boring_transaction(self, item):
        if self.boringUser_wallet_check(item.price_coins, item.price_diamonds) and item not in self.item_set.all():
            self.boring_coins -= item.price_coins
            self.boring_diamonds -= item.price_diamonds
            self.item_set.add(item)
            self.save()
            return True
        return False
    def boring_return_transaction(self, item):
        if item in self.item_set.all():
            self.item_set.remove(item)
            if item not in self.item_set.all():
                self.boring_coins += item.price_coins
                self.boring_diamonds += item.price_diamonds
                self.save()
                return True
        return False
    def __str__(self):
        return f"Name: {self.user.username}, Coins: {self.boring_coins} | {self.boring_diamonds}"

class Game(models.Model):
    class GameCategory(models.IntegerChoices):
        USELESS = 0
        CREATIVE = 1
        BORING = 2
        FRUSTRATION = 3
    name = models.CharField(max_length = 30)
    description = models.CharField(max_length = 150)
    iconClass1 = models.CharField(max_length = 5, blank=True, default='')
    iconClass2 = models.CharField(max_length = 15, blank=True, default='')
    function = models.CharField(max_length = 50, choices=FUNCTIONS)
    hint_text = models.CharField(max_length = 200, blank=True, default='')
    points_per_win = models.IntegerField(default = 10)
    likes = models.IntegerField(default = 0)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.IntegerField(choices=GameCategory.choices, default=False)
    user = models.ForeignKey(BoringUser, on_delete=models.CASCADE, related_name="games")
    times_played = models.IntegerField(default = 0)
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
    def __str__(self):
        return f'{self.user.user.username}, Description: {self.description}.'

class Item(models.Model):
    class ItemType(models.TextChoices):
        COMMON = 'Common'
        RARE = 'Rare'
        BORING = 'Boring'
        LEGENDARY = "Legendary"
        COMIC_ITEM = "Comic"
    user = ManyToManyField(BoringUser, blank=True)
    price_coins = models.IntegerField()
    price_diamonds = models.IntegerField(blank=True, default=0)
    name = models.CharField(max_length=50, default="Boring Item")
    description = models.TextField(max_length = 150)
    type = models.CharField(max_length=9,choices=ItemType.choices, default=ItemType.COMMON)
    def __str__(self):
        return f'{self.name}, Description: {self.description}, price: {self.price_coins} coins | {self.price_diamonds} diamonds.'
    