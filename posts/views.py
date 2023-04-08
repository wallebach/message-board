from django.views.generic import ListView
from django.shortcuts import render
from .models import Post


# Create your views here.
class HomePageView(ListView):
    template_name = "home.html"
    model = Post
