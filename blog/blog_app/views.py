from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Post, Event, Contact
from django.views.generic import ListView, DetailView

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


class ContactView(ListView):
    model = Contact
    template_name = 'contact.html'






