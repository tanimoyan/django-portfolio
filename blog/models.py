from django.conf import settings
from django.db import models
from django.utils import timezone


class Image(models.Model):
    picture = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200)
     
    def __str__(self):
        return self.title
        
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    topimage = models.ImageField(upload_to='images/', verbose_name='トップ画像', null=True, blank=True)
    image = models.ImageField(upload_to='images/', verbose_name='イメージ画像', null=True, blank=True)
    skill = models.CharField('skill', max_length=200, null=True, blank=True)
    github = models.CharField('github', max_length=200, null=True, blank=True)
    colaboratory = models.CharField('colaboratory', max_length=200, null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title