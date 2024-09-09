from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# Create your views here.
class BlogListView(ListView): #Creamos los posts tipo lista que más tarde se podrán editar
    model = Post
    template_name = "home.html"