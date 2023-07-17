from django.shortcuts import render ,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
def singin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            print("done")
            return redirect('msg')
        else:
            print('Invalid username or password.')
            messages.error(request, 'Invalid username or password.')
    return render(request,'singin.html')

def singup(request):
    if request.method =="POST":
        username=request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        myuser = User.objects.create_user(username,email,password)
        first_name= request.POST['first_name']
        myuser.first_name=first_name
        last_name = request.POST['last_name']
        myuser.last_name=last_name
        myuser.save()
        return redirect("singin")
    return render(request, 'singup.html')

def password_change(request):
    user = request.user
    if request.method == 'POST':
        old_password = request.POST["old_password"]
        if user.check_password(old_password):
            new_password1 = request.POST["new_password1"]
            new_password2 = request.POST["new_password2"]
            if new_password1 ==new_password2:
                user.set_password(new_password2)
                user.save()
                return redirect("logout")
            else:
                print("new_password1 != new_password2")
