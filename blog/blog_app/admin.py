from django.contrib import admin
from .models import Post, Event, Contact
# Register your models here.

admin.site.register(Post)
admin.site.register(Event)
admin.site.register(Contact)