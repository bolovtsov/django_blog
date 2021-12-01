from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# def home(request):
#     return render(request, "home.html", {})

class HomeView(ListView):
    model = Post
    template_name = "home.html"
    ordering = ["-time"]

class PostDetailView(DetailView):
    model = Post
    template_name = "post.html"
