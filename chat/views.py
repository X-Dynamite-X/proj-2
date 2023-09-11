
from django.shortcuts import render, get_object_or_404, redirect
from .models import Message
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.conf import settings
from users.models import UserProfile
@login_required
def msg(request):
    user = User.objects.exclude(id=request.user.id)
    context = {"users": user}
    return render(request, 'all_screan.html', context)

@login_required
def msg2(request, users_id):
    message = Message.objects.all()
    user = User.objects.exclude(id=request.user.id)

    # user_id = get_object_or_404(User, pk=users_id)
    username = request.user
    createdTo = get_object_or_404(User, pk=users_id)
    context = {
            "message": message, 
            "users": user,
            "username": username, 
            "createdTo": createdTo
                }
    
    
    if request.method == 'POST':
        image = request.FILES.get('image', settings.MEDIA_URL + "cv.png")
        text_msg = request.POST.get('text_msg', '').strip()
        
        if text_msg or image != settings.MEDIA_URL + "cv.png":
            msg = Message.objects.create(
                msg=text_msg,
                image=image,
                created_by=request.user,
                created_to=createdTo
            )
    
    return render(request, 'all_screan.html', context)

