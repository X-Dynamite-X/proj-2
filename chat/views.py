from django.shortcuts import render ,get_object_or_404
from .models import Message
from django.contrib.auth.models import User
# Create your views here.
from django.contrib.auth.decorators import login_required
@login_required
def msg(request):
    user = User.objects.all()
    context={"users":user,}
    return render(request, 'all_screan.html',context)
@login_required
def msg2(request,users_id):
    message=Message.objects.all()
    user = User.objects.all()
    user_id = get_object_or_404(User,pk=users_id)
    username = request.user
    createdTo= User.objects.get(id=users_id)
    print(createdTo)
    context={"message":message,"users":user,"username":username,"createdTo":createdTo}
    if request.method == 'POST' :
        if 'image' in request.FILES:
            
            image = request.FILES['image']
            print(image)
        else :
            image = "/static/media/cv.png"
        text_msg = request.POST['text_msg']
        # print(image)
        if len(text_msg) !=0 or image !="/static/media/cv.png":
            # print(image)
            msg=Message.objects.create(
                msg=text_msg,
                image=image,
                created_by = request.user,
                created_to= User.objects.get(id=users_id)
            )
    return render(request, 'all_screan.html',context)
