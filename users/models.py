from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(default="profile_picture/default.png",null=True,upload_to="profile_picture/")
    profile_picture_background =models.ImageField(default="profile_picture_background/default.png",null=True,upload_to="profile_picture_background/")