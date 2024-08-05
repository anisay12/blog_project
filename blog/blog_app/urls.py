from django.contrib import  admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
app_name = 'blog_app'

urlpatterns = [
    path('', views.home, name="home"),
    path('home/', views.home, name="home"),
    path('posts/', views.post, name="post"),
    path('events/', views.event, name="event"),
    path('contact/', views.contact, name="contact"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)