from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='posts/', null=False)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    image = models.ImageField(upload_to='events/', null=False)

    def get_absolute_url(self):
        return reverse("event_detail", kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Contact(models.Model):
    email = models.EmailField()
    request_type = models.CharField(max_length=50, choices=[('contact.html', 'Contact'), ('bug', 'Remontée de bug')])
    message = models.TextField()

    def __str__(self):
        return self.email

