from django.shortcuts import render
from . models import Blog, Comment




def home(request):
    return render(request, 'home.html')


def blog_home(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'blog/blog_home.html', context)


def single_blog(request, slug):
    blog = Blog.objects.get(slug=slug)
    context = {
        'blog': blog
    }
    return render(request, 'blog/single_blog.html', context)
