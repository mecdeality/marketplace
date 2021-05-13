from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    name = models.CharField(max_length=100)
    picture_url = models.CharField(default='https://pixy.org/src/78/788566.jpg', max_length=255)

    def __str__(self):
        return self.name


class Item(models.Model):
    description = models.CharField(max_length=200)
    detailed_description = models.TextField(default='')
    seller = models.CharField(max_length=100)
    price = models.IntegerField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    sold = models.BooleanField(default=False)
    owner = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, default=None, blank=True)
    item_login = models.CharField(max_length=100, default='account_login')
    item_password = models.CharField(max_length=100, default='password123')

    def __str__(self):
        return self.game.name
