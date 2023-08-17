from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Message(models.Model):
    msg = models.TextField(max_length=2400,unique=False,default="")
    created_by = models.ForeignKey(User,related_name="user",on_delete=models.CASCADE)
    created_dt = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default="pgb.png",upload_to="images/")


