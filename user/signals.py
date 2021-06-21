from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserStatus


@receiver(post_save, sender=User)
def create_status(sender, instance, created, **kwargs):
    if created:
        st = UserStatus.objects.create(user=instance)
        st.save()

