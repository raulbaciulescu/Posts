from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse


class Post(models.Model):
    image = models.ImageField()
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE) #when i delete an user, all posts are deleted
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('posts:detail', kwargs={'pk': self.id})

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # when i delete an user, all posts are deleted
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
