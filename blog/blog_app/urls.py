from django.contrib import  admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import HomeView, PostView, PostDetailView, EventDetailView, EventView, PostViewSet, EventViewSet, \
    ContactViewSet, login_view
from rest_framework.routers import DefaultRouter
from django.conf.urls import include
app_name = 'blog_app'


router = DefaultRouter()
router.register(r'articles', PostViewSet)
router.register(r'events', EventViewSet)
router.register(r'contacts', ContactViewSet)

urlpatterns = [
    #path('', HomeView.as_view(), name="home"),
    path('', views.login_view, name='login'),
    path('login/', views.login_view, name='login'),
    path('home/', HomeView.as_view(), name="home"),
    path('posts/', PostView.as_view(), name="post"),
    path('post_detail/<int:pk>', PostDetailView.as_view(), name="post_detail"),
    path('events/', EventView.as_view(), name="event"),
    path('event_detail/<int:pk>', EventDetailView.as_view(), name="event_detail"),
    path('contact/', views.contact, name="contact"),
    path('api/', include(router.urls)),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
