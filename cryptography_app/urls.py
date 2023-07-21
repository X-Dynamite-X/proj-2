from django.urls import path
from .views import *


urlpatterns = [
    path('cryptography/',cryptography,name='cryptography'),
    # path('cryptography/done/',outt,name='outt'),

]

