from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE);
    phone = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=255, blank=True)
    dob = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=20, blank=True)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png')
    gender = models.CharField(max_length=10, choices=(('Male','Male'),('Female','Female')), default='Male')

    def __str__(self):
        return self.user.username

# Automatically create Profile for new users
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        # Ensure profile exists for existing users
        Profile.objects.get_or_create(user=instance);