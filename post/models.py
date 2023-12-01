from django.db import models
from django.utils import timezone

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
# class Dair(models.Model):
#     username = models.ForeignKey(User, on_delete=models.CASCADE)
#     profile_picture_dair =models.ImageField(null=True,upload_to="send_dair_img/")
#     dair_img  = models.ImageField(null=True,upload_to="dair_img/")
#     dair_video = models.FileField(upload_to='dair_videos/',null=True)
#     def __str__(self):
#         return f"Dair by {self.username.username}"
    


class Dair(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture_dair =models.ImageField(null=True,upload_to="send_dair_img/")
    def __str__(self):
        return f"Dair by {self.username.username}"
class DairPost(models.Model):
    dair = models.ForeignKey(Dair, related_name='dair_posts', on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)  # يمكنك جعله خياريًا إذا كنت ترغب في ذلك
    dair_img = models.ImageField(null=True, upload_to="dair_img/")
    dair_video = models.FileField(upload_to='dair_videos/', null=True)
    dair_created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Dair ID: {self.username.username}, DairPost ID: {self.id}"

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.dair.username
        super(DairPost, self).save(*args, **kwargs)
