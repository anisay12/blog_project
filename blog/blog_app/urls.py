from django.contrib import  admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import HomeView, PostView, PostDetailView, EventDetailView, EventView, ContactView
from django.conf.urls import include
app_name = 'blog_app'

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('home/', HomeView.as_view(), name="home"),
    path('posts/', PostView.as_view(), name="post"),
    path('post_detail/<int:pk>', PostDetailView.as_view(), name="post_detail"),
    path('events/', EventView.as_view(), name="event"),
    path('event_detail/<int:pk>', EventDetailView.as_view(), name="event_detail"),
    path('contact/', ContactView.as_view(), name="contact"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
