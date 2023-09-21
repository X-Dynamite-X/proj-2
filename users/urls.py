from django.contrib import admin
from django.urls import path,include
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',singin,name='singin'),
    path("singup/", singup, name="singup"),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path("password_change/",password_change,name="password_change"),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="password_reset_email.html"), name='password_reset'), 
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name="password_done_sen_maile.html"),name='password_reset_done'),
    path('reser/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"),name='password_reset_confirm'),
    path('reser/done/',auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"),name='password_reset_complete'),
    path("userprofile/",user_profile, name="user_profile"),
    path('edit_profile/',edit_profile, name='edit_profile'),
]

