from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *

# Create your views here.
def index(request):
    return render(
        request,
        'post/index.html'
    )
    
class PostList(ListView):
    model = Post
    template_name='post/index.html'

class PostDetail(DetailView):
    model = Post