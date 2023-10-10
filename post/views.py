from django.shortcuts import render ,redirect
from .models import Post, Dair
# Create your views here.
from django.contrib.auth.models import User
from .cut_video import get_video_duration, trim_video ,get_media_type

from django.conf import settings

def dair(request, dair_img_and_video_file_input):
    user = request.user
    # احتسب نوع الملف
    media_type = get_media_type(dair_img_and_video_file_input)

    if media_type == 'video':
        # إنشاء سجل Dair للفيديو
        dair = Dair.objects.create(
            username=request.user,
            dair_video=dair_img_and_video_file_input,
            profile_picture_dair=user.userprofile.profile_picture
        )
    elif media_type == 'image':
        # إنشاء سجل Dair للصورة
        dair = Dair.objects.create(
            username=request.user,
            dair_img=dair_img_and_video_file_input,
            profile_picture_dair=user.userprofile.profile_picture
        )

    return redirect("post")
    # return "done"
def post(request):
    user = request.user
    posts = Post.objects.all()
    dairs = Dair.objects.all()
    if request.method == 'POST':
        add_image_post = request.FILES.get(
            'add_image_post', settings.MEDIA_URL + "cv.png")
        post_text = request.POST.get('post_text', '').strip()
        dair_img_and_video_file_input = request.FILES.get(
            'dair_img_and_video_file_input', settings.MEDIA_URL + "cv.png")
        dair(request,dair_img_and_video_file_input)
        
        if post_text or add_image_post != settings.MEDIA_URL + "cv.png":
            post = Post.objects.create(
                username=request.user,
                post_text=post_text,
                post_img=add_image_post,
                profile_picture_post=user.userprofile.profile_picture
            )
            
        # بمجرد أن تنجح عملية الإرسال، قم بتوجيه المستخدم إلى صفحة أخرى (POST-Redirect-GET)
        return redirect('post')

    context = {"user": user, "posts": posts, "dairs": dairs}
    return render(request, 'post.html', context)
