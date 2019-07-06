from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader
from django.views import generic
from . models import Sermon, Event, Post

def index(request):
    template = loader.get_template('sermon/index.html')
    sermons = Sermon.objects.all()
    context ={
        'sermons' : sermons
    }
    return HttpResponse(template.render(context,request))

def event(request):
    template = loader.get_template('sermon/event.html')
    events = Event.objects.all()
    context = {
        'events':events
    }
    return HttpResponse(template.render(context,request))

def about(request):
    template = loader.get_template('sermon/about.html')
    context = {}
    return HttpResponse(template.render(context,request))

def blog(request):
    template = loader.get_template('sermon/blog.html')
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return HttpResponse(template.render(context,request))