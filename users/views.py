# استيراد المكتبات والنماذج الضرورية
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import UserProfile  # استيراد نموذج UserProfile إذا كنت تستخدمه
from django.contrib.auth.decorators import login_required

# دالة تسجيل الدخول
def singin(request):
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # تسجيل المستخدم إذا تم التحقق من بيانات تسجيل الدخول بنجاح
            login(request, user)
            messages.success(request, 'تم تسجيل الدخول بنجاح.')
            return redirect('user_profile')  # إعادة توجيه المستخدم إلى صفحة أخرى بعد تسجيل الدخول
        else:
            # إذا كانت بيانات تسجيل الدخول غير صحيحة
            messages.error(request, 'اسم المستخدم أو كلمة المرور غير صحيحة.')

    return render(request, 'singin.html')  # عرض صفحة تسجيل الدخول

# دالة تسجيل مستخدم جديد 
def singup(request):
    if request.method == "POST":
        username = request.POST.get('username', '').lower()
        email = request.POST.get('email', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        phone_number = request.POST.get('phone_number', '')
        # التحقق من عدم استخدام البريد الإلكتروني أو رقم الهاتف مسبقًا
        if User.objects.filter(email=email).exists():
            messages.error(request, 'البريد الإلكتروني مستخدم بالفعل.')
            return redirect("singup")
        if UserProfile.objects.filter(phone_number=phone_number).exists():
            messages.error(request, 'رقم الهاتف مستخدم بالفعل.')
            return redirect("singup")
        # التحقق من صحة كلمة المرور
        if password1 == password2:
            myuser = User.objects.create_user(username, email, password1)
            if myuser is not None:
                first_name = request.POST.get('first_name', '').title()
                myuser.first_name = first_name
                last_name = request.POST.get('last_name', '').lower()
                myuser.last_name = last_name
                myuser.save()
                # إنشاء ملف تعريف المستخدم إذا لم يتم إنشاؤه بالفعل
                user_profile, created = UserProfile.objects.get_or_create(user=myuser)
                # حفظ رقم الهاتف في موديل المستخدم
                user_profile.phone_number = phone_number
                user_profile.save()
                return redirect("singin")
            else:
                messages.error(request, 'حدثت مشكلة أثناء إنشاء حساب المستخدم.')
        else:
            messages.error(request, 'كلمة المرور غير متطابقة.')
            return redirect("singup")
    return render(request, 'singup.html')

# دالة تغيير كلمة المرور
@login_required
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
                return redirect("logout")  # إعادة توجيه المستخدم إلى تسجيل الخروج بعد تغيير كلمة المرور بنجاح
            else:
                messages.error(request, 'كلمة المرور الجديدة غير متطابقة.')

    return render(request, 'password_change.html')  # عرض صفحة تغيير كلمة المرور

# دالة عرض ملف تعريف المستخدم (تحتاج إلى تسجيل الدخول للوصول)
@login_required
def user_profile(request):
    # user = request.user
    context ={ 
        # 'user': user,
        
            }
    # print(user.first_name)

    return render(request, 'user_profile.html',context)  # عرض صفحة ملف تعريف المستخدم
@login_required
def edit_profile(request):
    if request.method == 'POST':
        user = request.user
        new_first_name = request.POST.get('first_name', '').title()
        new_last_name = request.POST.get('last_name', '').lower()
        new_email = request.POST.get('email', '')
        new_phone_number = request.POST.get('phone_number', '')

        user.first_name = new_first_name
        user.last_name = new_last_name
        user.email = new_email

        # تحديث الصورة الشخصية إذا تم تحميلها
        user_profile = user.userprofile
        if 'profile_picture' in request.FILES:
            user_profile.profile_picture = request.FILES['profile_picture']
        if 'profile_picture_background' in request.FILES:
            user_profile.profile_picture_background = request.FILES['profile_picture_background']
        user_profile.save()
        user.save()

        # إذا كنت تستخدم نموذج UserProfile مرتبطًا بنموذج المستخدم User، يمكنك تحديث رقم الهاتف هكذا:
        try:
            user_profile = user.userprofile
            user_profile.phone_number = new_phone_number
            user_profile.save()
        except UserProfile.DoesNotExist:
            messages.error(request, 'المستخدم ليس لديه ملف تعريف بعد.')

        messages.success(request, 'تم تحديث ملف التعريف بنجاح.')
        return redirect('user_profile')  # توجيه المستخدم إلى صفحة ملف تعريف المستخدم بعد التحديث

    return render(request, 'edit_profile.html')