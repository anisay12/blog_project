from django.shortcuts import render, redirect
from .models import Post, Event, Contact
from django.views.generic import ListView, DetailView
from .serializers import PostSerializer, EventSerializer, ContactSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class HomeView(ListView):
    model = Post
    model = Event
    template_name = 'home.html'


class PostView(ListView):
    model = Post
    template_name = 'posts.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class EventView(ListView):
    model = Event
    template_name = 'events.html'


class EventDetailView(DetailView):
    model = Event
    template_name = 'event_detail.html'


#class ContactView(ListView):
 #   model = Contact
  #  template_name = 'contact.html'


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]


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






