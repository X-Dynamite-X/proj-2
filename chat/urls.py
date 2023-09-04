from django.contrib import admin
from django.urls import path,include
from .views import *
from django.contrib.auth.models import User
urlpatterns = [
    path("msg/", msg, name="msg"),
    path("msg/<users_id>/", msg2, name="msg_id"),
]