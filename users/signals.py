from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile
from django.contrib.auth import get_user_model
User = get_user_model()

# The user model sends a signal everytime a user is created


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(seller=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
