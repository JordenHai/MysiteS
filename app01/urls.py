"""Mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import re_path
from app01 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login),
    path('index/', views.index),
    path('user_info/', views.userInfo),
    path('group_info/', views.groupInfo),
    re_path('userdetail-(?P<nid>\d+)/', views.userDetail),
    re_path('userdel-(?P<nid>\d+)/', views.userDel),
    re_path('useredit-(?P<nid>\d+)/', views.userEdit),

    path('orm/',views.orm)
]

#url的分发系统