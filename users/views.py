from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import UserProfile  # استيراد نموذج UserProfile إذا كنت تستخدمه

def singin(request):
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'تم تسجيل الدخول بنجاح.')
            return redirect('msg')
        else:
            messages.error(request, 'اسم المستخدم أو كلمة المرور غير صحيحة.')

    return render(request, 'singin.html')

def singup(request):
    if request.method == "POST":
        username = request.POST.get('username', '').lower()
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        # التحقق من وجود المستخدم أولاً
        if User.objects.filter(username=username).exists():
            # المستخدم موجود بالفعل
            messages.error(request, 'اسم المستخدم موجود بالفعل.')
            return redirect("singup")

        myuser = User.objects.create_user(username, email, password)

        if myuser is not None:
            first_name = request.POST.get('first_name', '').title()
            myuser.first_name = first_name
            last_name = request.POST.get('last_name', '').lower()
            myuser.last_name = last_name
            myuser.save()
            # إنشاء ملف تعريف المستخدم إذا لم يتم إنشاؤه بالفعل
            user_profile, created = UserProfile.objects.get_or_create(user=myuser)
            # يوجد خطاء في هاذه ال if 
            if "profile_picture" in request.FILES and request.FILES["profile_picture"]:
                print("image")
                user_profile.profile_picture = request.FILES["profile_picture"]
                user_profile.save()
                print(request.FILES["profile_picture"])
            return redirect("singin")

        else:
            messages.error(request, 'حدثت مشكلة أثناء إنشاء حساب المستخدم.')

    return render(request, 'singup.html')

def password_change(request):
    user = request.user
    if request.method == 'POST':
        old_password = request.POST["old_password"]
        if user.check_password(old_password):
            new_password1 = request.POST["new_password1"]
            new_password2 = request.POST["new_password2"]
            if new_password1 == new_password2:
                user.set_password(new_password2)
                user.save()
                return redirect("logout")
            else:
                messages.error(request, 'كلمة المرور الجديدة غير متطابقة.')
    return render(request, 'password_change.html')
