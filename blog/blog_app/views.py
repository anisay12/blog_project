from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Post, Event, Contact
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Create your views here.


def home(request):
    return render(request, 'home.html', {})


def post(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})


def event(request):
    return render(request, 'events.html', {})


def contact(request):
    return render(request, 'contact.html', {})
