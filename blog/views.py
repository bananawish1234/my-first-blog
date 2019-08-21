from django.shortcuts import render
<<<<<<< HEAD
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
=======

def post_list(request):
    return render(request, 'blog/post_list.html', {})
>>>>>>> parent of 2f4b06d... Modified templates to display posts from database.
