from django.contrib import admin
from . models import Sermon, Event, Post
# Register your models here.

admin.site.register(Sermon)
admin.site.register(Event)
admin.site.register(Post)