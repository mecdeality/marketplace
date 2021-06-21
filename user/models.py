from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserStatus(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    send_request = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username+", Seller:"+ str(self.is_seller)
