from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from django.contrib.auth import views as auth_views
from django.views.static import serve
from django.conf import settings
from django.urls import re_path
urlpatterns=[
    path('',views.index,name='index'),
    path('details',views.details,name='details'),
    path('update',views.update_resume,name='update_resume'),
]