from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from .models import Blog
# Create your views here.

class BlogListView(ListView):
	model = Blog
	template_name = 'blog/blog.html'
