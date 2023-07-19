# configuring models for video service app
from django.db import models
from django.contrib.postgres.fields import ArrayField

from videoservice.settings import AUTH_USER_MODEL


class VSUser(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    black_list = ArrayField(models.CharField(max_length=128), blank=True, default=list)
    ignore_list = ArrayField(models.CharField(max_length=128), blank=True, default=list)
    subscribes = ArrayField(models.CharField(max_length=128), blank=True, default=list)

    def __str__(self):
        return self.user.username


class VSVideo(models.Model):
    name = models.CharField(max_length=128)
    author = models.ForeignKey('VSUser', on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True)
    likes = ArrayField(models.CharField(max_length=128), blank=True, default=list)
    description = models.TextField(blank=False, default='My new video')
    comments = models.ManyToManyField('VSComment', through='CommentVideo')
    upload = models.FileField()

    def __str__(self):
        return self.name


class VSComment(models.Model):
    author = models.ForeignKey('VSUser', on_delete=models.CASCADE)
    text = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    likes = ArrayField(models.CharField(max_length=128), blank=True, default=list)
    ignored = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.author.username}/ {self.text}'


class CommentVideo(models.Model):
    video = models.ForeignKey('VSVideo', on_delete=models.CASCADE)
    comment = models.ForeignKey('VSComment', on_delete=models.CASCADE)
