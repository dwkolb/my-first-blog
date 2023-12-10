#SDEV 220 M05 Tutorial - Django Deploy and Views
#SDEV 220 M05 TUtorial - Django Forms, Data, and Security
#https://tutorial.djangogirls.org/en/django_urls/

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]