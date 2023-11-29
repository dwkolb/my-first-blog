'''
Kolb, Derek W. 
Nov 2023
SDEV 220 DJango Tutorials
https://tutorial.djangogirls.org/en/dynamic_data_in_templates/
'''

from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
  posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
  return render(request, 'blog/post_list.html', {'posts': posts})
