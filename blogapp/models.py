from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=50)
    dateCreated = models.DateField(editable=False, default=now)
    lastModifiedDate = models.DateField(null=True, blank=True)
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='blog')
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    text = models.TextField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(
        User, related_name='comments', on_delete=models.CASCADE, null=True, blank=True)
    blog = models.ForeignKey(
        Blog, related_name='comments', on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
    datePublished = models.DateTimeField(default=now)
