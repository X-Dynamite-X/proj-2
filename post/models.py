from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    username  = models.ForeignKey(User,on_delete=models.CASCADE)
    profile_picture_post =models.ImageField(null=True,upload_to="send_post_img/")
    post_text = models.TextField(max_length=2400,unique=False,default="")
    post_img  = models.ImageField(null=True,upload_to="post_img/")
    post_created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Post by {self.username.username}"
class Dair(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_picture_dair =models.ImageField(null=True,upload_to="send_dair_img/")
    dair_img  = models.ImageField(null=True,upload_to="dair_img/")
    dair_video = models.FileField(upload_to='dair_videos/',null=True)
    def __str__(self):
        return f"Dair by {self.username.username}"