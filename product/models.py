from django.db import models
from django.contrib.auth.models import User
from user.models import UserStatus


class Game(models.Model):
    name = models.CharField(max_length=100)
    picture_url = models.ImageField(null=True, blank=True, default='games/default.jpg', upload_to='games')

    def __str__(self):
        return self.name


class Item(models.Model):
    description = models.CharField(max_length=200)
    detailed_description = models.TextField(default='')
    # seller = models.CharField(max_length=100)
    price = models.IntegerField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    sold = models.BooleanField(default=False)
    owner = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, default=None, blank=True)
    item_login = models.CharField(max_length=100, default='account_login')
    item_password = models.CharField(max_length=100, default='password123')
    seller = models.ForeignKey(UserStatus, null=True, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.game.name+", Sold:"+ str(self.sold)


class Comment(models.Model):
    seller = models.ForeignKey(UserStatus, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.seller.user.username
