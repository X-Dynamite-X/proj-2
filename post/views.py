from django.shortcuts import render ,redirect ,get_object_or_404
from .models import Post, Dair ,DairPost
# Create your views here.
from django.contrib.auth.models import User
from .cut_video import get_video_duration, trim_video ,get_media_type

from django.conf import settings
from django.contrib.auth.decorators import login_required

# def dair(request, dair_img_and_video_file_input):
#     user = request.user
#     # احتسب نوع الملف
#     media_type = get_media_type(dair_img_and_video_file_input)

#     if media_type == 'video':
#         # إنشاء سجل Dair للفيديو
#         dair = Dair.objects.create(
#             username=request.user,
#             dair_video=dair_img_and_video_file_input,
#             profile_picture_dair=user.userprofile.profile_picture
#         )
#     elif media_type == 'image':
#         # إنشاء سجل Dair للصورة
#         dair = Dair.objects.create(
#             username=request.user,
#             dair_img=dair_img_and_video_file_input,
#             profile_picture_dair=user.userprofile.profile_picture
#         )

#     return redirect("post")
#     # return "done"


@login_required
def add_dair(request):
    user = request.user
    try:
        # يحاول البحث عن دار مرتبطة بالمستخدم
        dair = Dair.objects.get(username=user)
    except Dair.DoesNotExist:
        # إذا لم تكن هناك دار مرتبطة بالمستخدم، سيتم إنشاء واحدة
        dair = Dair.objects.create(username=user, profile_picture_dair=user.userprofile.profile_picture)

    if request.method == 'POST':
        dair_img_and_video_file_input = request.FILES.get('dair_img_and_video_file_input', settings.MEDIA_URL + "cv.png")
        media_type = get_media_type(dair_img_and_video_file_input)

        if media_type == 'video':
            # إنشاء سجل DairPost للفيديو
            DairPost.objects.create(
                dair=dair,
                dair_video=dair_img_and_video_file_input
            )
        elif media_type == 'image':
            # إنشاء سجل DairPost للصورة
            DairPost.objects.create(
                dair=dair,
                dair_img=dair_img_and_video_file_input
            )

        return redirect("post")

    return render(request,"add_dair.html")
@login_required
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
        # dair(request,dair_img_and_video_file_input)
        
        if post_text or add_image_post != settings.MEDIA_URL + "cv.png":
            post = Post.objects.create(
                username=request.user,
                post_text=post_text,
                post_img=add_image_post,
                profile_picture_post=user.userprofile.profile_picture
            )
            
        # بمجرد أن تنجح عملية الإرسال، قم بتوجيه المستخدم إلى صفحة أخرى (POST-Redirect-GET)
        return redirect('post')

    context = {"user": user,'dairs':dairs, "posts": posts}
    return render(request, 'post.html', context)

@login_required
def dair_views1(request, username, dair_post_id):
    user = get_object_or_404(User, username=username)
    users = User.objects.all()
    current_user = get_object_or_404(User, username=username)
    dair_posts = DairPost.objects.filter(dair__username=current_user).order_by('dair_created_date')
    current_dair = get_object_or_404(DairPost, id=dair_post_id, dair__username=user)
    previous_post = None
    next_post = None

    # البحث عن العناصر السابقة والتالية
    for i, post in enumerate(dair_posts):
        if post == current_dair:
            if i > 0:
                previous_post = dair_posts[i - 1]
            if i < len(dair_posts) - 1:
                next_post = dair_posts[i + 1]
            break

    previous_user = None
    next_user = None

    for i, user in enumerate(users):
        if user == current_user:
            if i > 0:
                previous_user = users[i - 1]
            if i < len(users) - 1:
                next_user = users[i + 1]
            break

    # تحديث current_user بناءً على العملية المطلوبة
# قبل التحديث
    print("Before Update - current_user:", current_user )

    # تحديث current_user
    if previous_user:
        current_user = previous_user
    elif next_user:
        current_user = next_user
    print(previous_user)
    print(next_user)

    # بعد التحديث
    print("After Update - current_user:", current_user )
        
    # بعد الحلقة، يمكنك البحث عن first_post إذا كان المستخدم الحالي غير فارغ
    first_post = None
    if current_user:
        first_post = DairPost.objects.filter(dair__username=current_user).order_by('dair_created_date').first()

    context = {
        'dair_posts': dair_posts,
        'current_dair': current_dair,
        'previous_post': previous_post,
        'next_post': next_post,
        'dair_po': first_post,
        'user': user,
        'previous_user': previous_user,
        'next_user': next_user,
        'current_user': current_user,
    }

    return render(request, "dair_views.html", context)


from django.shortcuts import render, get_object_or_404
from .models import Dair, DairPost, User
@login_required

def dair_views(request, username, dair_post_id):
    users = get_object_or_404(User, username=username)
    current_post = get_object_or_404(DairPost, username=users, id=dair_post_id)
    dair_posts = DairPost.objects.filter(dair__username=users).order_by('dair_created_date')
    current_dair = get_object_or_404(DairPost, id=dair_post_id, dair__username=users)
    # ابحث عن المستخدم السابق والمستخدم التالي والمنشور الأول الخاص بهما
    previous_user = Dair.objects.filter(id__lt=users.dair.id).order_by('-id').first()
    next_user = Dair.objects.filter(id__gt=users.dair.id).order_by('id').first()
    first_post_of_previous_user = DairPost.objects.filter(username=previous_user.username).first() if previous_user else None
    first_post_of_next_user = DairPost.objects.filter(username=next_user.username).first() if next_user else None
    previous_post = None
    next_post = None
    counts=dair_posts.count()


    # البحث عن العناصر السابقة والتالية
    for i, post in enumerate(dair_posts):
        if post == current_dair:
            if i > 0:
                previous_post = dair_posts[i - 1]
            if i < len(dair_posts) - 1:
                next_post = dair_posts[i + 1]
            break
    context = {
        'current_post': current_post,
        'first_post_of_previous_user': first_post_of_previous_user,
        'first_post_of_next_user': first_post_of_next_user,
        'dair_posts': dair_posts,
        'current_dair': current_dair,
        'previous_post': previous_post,
        'next_post': next_post,
        'users': users,
        'previous_user': previous_user,
        'next_user': next_user,
        'counts':counts
    }

    return render(request, 'dair_views.html', context)
