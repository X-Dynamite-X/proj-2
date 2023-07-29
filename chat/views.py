from django.shortcuts import render ,get_object_or_404
from .models import Message
from django.contrib.auth.models import User
# Create your views here.

def msg(request):
    message=Message.objects.all()
    user = User.objects.all()
    # user_id = get_object_or_404(User,pk=user_id)
    # print(user_id.email)
    username = request.user
    uesrname_is_cheak = str(request.user)

    context={"message":message,"users":user,"username":username}
    if request.method == 'POST' :
        if 'image' in request.FILES:
            image = request.FILES['image']
        else :
            image = "/static/media/cv.png"
        text_msg = request.POST['text_msg']
        print(image)
        if len(text_msg) !=0 or image !="/static/media/cv.png":
            print(image)
            msg=Message.objects.create(
                msg=text_msg,
                image=image,
                created_by = request.user,
            )

    return render(request, 'all_screan.html',context)

def msg2(request,user_id):
    message=Message.objects.all()
    user = User.objects.all()
    # user_id = get_object_or_404(User,pk=user_id)
    # print(user_id.email)
    username = request.user


    context={"message":message,"users":user,"username":username}
    if request.method == 'POST' :
        if 'image' in request.FILES:
            image = request.FILES['image']
        else :
            image = "/static/media/cv.png"
        text_msg = request.POST['text_msg']
        print(image)
        if len(text_msg) !=0 or image !="/static/media/cv.png":
            print(image)
            msg=Message.objects.create(
                msg=text_msg,
                image=image,
                created_by = request.user,
            )
    return render(request, 'all_screan.html',context)