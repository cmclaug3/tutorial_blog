from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils.text import slugify


'''

ALL MODELS NOTES

Blog
 title, slug, body, pictures, date_created, date_updated, Comment
 
Comment
 username, body, date_created
 
---------------

Lesson
 title, slug, Topic, body, pictures, video?, user_grade (1-10), date_created, date_updated, Comment
 
Topic
 name, Category, slug
 
Category
 name, slug

'''

class Blog(models.Model):
 title = models.CharField(max_length=70)
 slug = models.SlugField(blank=True, null=True)
 body = models.TextField()
 date_created = models.DateTimeField(auto_now_add=True)

 def __str__(self):
  return self.title

 # Automatically create slug when saving new Blog object
 def save(self, *args, **kwargs):
  self.slug = slugify(self.title)
  super(Blog, self).save(*args, **kwargs)



class Comment(models.Model):
 username = models.ForeignKey(User, on_delete=models.CASCADE)
 blog = models.ForeignKey(Blog, on_delete=models.CASCADE, default='')
 body = models.TextField()
 date_created = models.DateTimeField(auto_now_add=True)

 def __str__(self):
  return self.blog.title
