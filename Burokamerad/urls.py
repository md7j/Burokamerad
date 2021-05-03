"""Burokamerad URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import include, path
from . import views
from bot.views import ChatterBotAppView, ChatterBotApiView


urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('login', views.login.as_view(), name='login'),
    path('faq', views.faq.as_view(), name='faq'),
    path('register', views.register.as_view(), name='register'),
    path('api/bot/', include('bot.urls'), name='bot'),
    path('admin/', admin.site.urls),
]