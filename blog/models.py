from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


class Category(models.Model):
    name = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default="Post")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=255, default='coding')

    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return self.title
