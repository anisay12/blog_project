from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Post, Event, Contact
from django.views.generic import ListView, DetailView
from .serializers import PostSerializer, EventSerializer, ContactSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


# Views related to displaying posts and events

# HomeView displays a list of Post objects in 'home.html'
class HomeView(ListView):
    model = Post
    template_name = 'home.html'


# PostView displays a list of Post objects in 'posts.html'
class PostView(ListView):
    model = Post
    template_name = 'posts.html'


# PostDetailView displays a single Post object in 'post_detail.html'
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


# EventView displays a list of Event objects in 'events.html'
class EventView(ListView):
    model = Event
    template_name = 'events.html'


# EventDetailView displays a single Event object in 'event_detail.html'
class EventDetailView(DetailView):
    model = Event
    template_name = 'event_detail.html'

# API endpoints using Django REST framework


# PostViewSet allows CRUD operations on Post objects through an API
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


# EventViewSet allows CRUD operations on Event objects through an API
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]


# ContactViewSet allows CRUD operations on Contact objects through an API
class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]

# User authentication views


# login_view handles user login functionality
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home/')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')


# logout_view handles user logout functionality
def logout_view(request):
    logout(request)
    return redirect('login')

# contact handles contact form submission
def contact(request):
    if request.method == 'POST':
        email = request.POST['message-email']
        option = request.POST.get('option')
        message = request.POST['message']
        new_contact = Contact(email=email, request_type=option, message=message)
        new_contact.save()
        return render(request, 'contact.html', {'email': email})

    else:
        return render(request, 'contact.html', {})






