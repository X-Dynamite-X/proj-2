from django.shortcuts import get_list_or_404, render, get_object_or_404, redirect
from .models import Message
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.db.models import Q

@login_required
def msg2(request, users_id):
    # الحصول على المستخدم الهدف باستخدام معرفه
    createdTo = get_object_or_404(User, pk=users_id)
    
    # استعلام لجلب الرسائل بين المنشئ والمستقبل
    messages_between_users = Message.objects.filter(
        Q(created_by=request.user, created_to=createdTo) |
        Q(created_by=createdTo, created_to=request.user)
        ).order_by('created_dt')
    

    # استعلام لجلب جميع المستخدمين باستثناء المستخدم الحالي
    users = User.objects.exclude(id=request.user.id)
    
    # الحصول على اسم المستخدم الحالي
    username = request.user
    
    # إعداد السياق لاستخدامه في القالب
    context = {
        "messages": messages_between_users,
        "users": users,
        "username": username,
        "createdTo": createdTo
    }
    
    if request.method == 'POST':
        # الحصول على الصورة المرفوعة إذا كانت موجودة، وإلا سيتم استخدام صورة افتراضية
        image = request.FILES.get('image', settings.MEDIA_URL + "cv.png")
        
        # الحصول على نص الرسالة المدخلة من المستخدم وإزالة الفراغات الزائدة
        text_msg = request.POST.get('text_msg', '').strip()
        
        # التحقق من وجود نص في الرسالة أو وجود صورة غير الصورة الافتراضية
        if text_msg.strip() or image != settings.MEDIA_URL + "cv.png":
            # إنشاء رسالة جديدة إذا تم إدخال نص أو صورة
            msg = Message.objects.create(
                msg=text_msg,
                image=image,
                created_by=request.user,
                created_to=createdTo
            )
    
    # إعادة توجيه المستخدم إلى الصفحة الرئيسية بعد الإرسال
    return render(request, 'all_screan.html', context)

@login_required
def msg(request):
    user = User.objects.exclude(id=request.user.id)
    context = {"users": user}
    return render(request, 'all_screan.html', context)
