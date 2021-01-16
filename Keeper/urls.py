"""Keeper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls import url
from Noting import views


from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls), #opens admin interface for superuser
    path('', views.temp),
    path('accounts/', include('django.contrib.auth.urls')), #using auth to maintain user accounts
    path('noting/', views.main), #use main view for /noting
    path('addNote/', views.addNote), #use addNote view for /addNote
    path('deleteNote/<int:Note_id>/', views.deleteNote) #use deleteNote for /deleteNote
]
