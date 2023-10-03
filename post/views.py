from django.shortcuts import render
from .models import Post, Dair
# Create your views here.
from django.contrib.auth.models import User
from .cut_video import get_video_duration, trim_video

from django.conf import settings


def dair(request):
    if request.method == 'POST':
        # dair_video_file = request.FILES.get('dair_video_file')
        # video_duration = get_video_duration(dair_video_file)
        # if video_duration > 120:
        #     dair_video_file = trim_video(dair_video_file, 0, 120)
        dair_img_file = request.FILES.get(
            'dair_img_file', settings.MEDIA_URL + "cv.png")

        if dair_img_file != settings.MEDIA_URL + "cv.png":
            dair = Dair.objects.create(dair_img=dair_img_file)


def post(request):
    user = request.user

    posts = Post.objects.all()
    dairs = Dair.objects.all()

    context = {"user": user, "posts": posts, "dairs": dairs}

    if request.method == 'POST':
        add_image_post = request.FILES.get(
            'add_image_post', settings.MEDIA_URL + "cv.png")
        post_text = request.POST.get('post_text', '').strip()
        dair_img_file = request.FILES.get(
            'dair_img_file', settings.MEDIA_URL + "cv.png")
        if dair_img_file != settings.MEDIA_URL + "cv.png":
            dair = Dair.objects.create(
                username=request.user,
                dair_img=dair_img_file,
                profile_picture_dair=user.userprofile.profile_picture
            )
        if post_text or add_image_post != settings.MEDIA_URL + "cv.png":
            post = Post.objects.create(
                username=request.user,
                post_text=post_text,
                post_img=add_image_post,
                profile_picture_post=user.userprofile.profile_picture
            )
    return render(request, 'post.html', context)
