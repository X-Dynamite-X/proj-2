from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
# Create your models here.
class Message(models.Model):
    msg = models.TextField(max_length=2400,unique=False,default="")
    created_by = models.ForeignKey(User,related_name="user",on_delete=models.CASCADE)
    created_dt = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default="pgb.png",null=True,upload_to="images/")
    # video = models.FileField(upload_to='video/', null=True, validators=[FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
