from django.urls import path

from . views import blog_home, single_blog

urlpatterns = [
    path('', blog_home, name='blog_home'),
    path('<slug:slug>', single_blog, name='single_blog')
]
