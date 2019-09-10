from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Room(models.Model):
    room_id = models.AutoField(primary_key= True)
    room_name = models.CharField(max_length= 40)
    room_description = models.CharField(max_length= 200)
   # room_type=models.CharField(max_length=40)
   # room_design=models.CharField(max_length=100)
    user = models.ForeignKey(Profile, on_delete= models.CASCADE)