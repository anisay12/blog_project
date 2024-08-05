from django.contrib import  admin
from django.urls import path
from . import views
from django.conf.urls import include
app_name = 'blog_app'

urlpatterns = [
    path('', views.home, name="home"),
    path('posts.html/', views.contact),
    path('events.html/', views.contact),
    path('contact.html/', views.contact),

]