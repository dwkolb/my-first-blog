#M04 django tutorial 
#SDEV 220 intro to SDEV with python
#11/17/2023
#https://tutorial.djangogirls.org/en/django_admin/

from django.contrib import admin
from .models import Post

admin.site.register(Post)