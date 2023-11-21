#SDEV 220 M05 Tutorial - Django Deploy and Views
#https://tutorial.djangogirls.org/en/django_urls/

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]