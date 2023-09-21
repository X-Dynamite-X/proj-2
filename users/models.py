from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(default="profile_picture/default.png",null=True,upload_to="profile_picture/")
    profile_picture_background =models.ImageField(default="profile_picture_background/default.png",null=True,upload_to="profile_picture_background/")
    phone_number = PhoneNumberField(max_length=15)