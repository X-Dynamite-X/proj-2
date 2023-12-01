from django.urls import path
from .views import *

urlpatterns = [
    path('post/', post, name='post'),
    path("post/add_dair", add_dair, name="dair"),
    path('post/dair/<str:username>/<int:dair_post_id>/', dair_views, name='dair_views'),
]

