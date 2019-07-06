from django.urls import path

from . import views

app_name = 'sermon'

urlpatterns = [
    path('',views.index,name='index'),
    path('event/',views.event, name = 'event'),
    path('about/',views.about, name = 'about'),
    path('blog/',views.blog, name = 'blog'),
]