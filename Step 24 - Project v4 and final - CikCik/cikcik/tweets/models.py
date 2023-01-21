from django.contrib.auth.models import User as DjangoUser
from django.db import models


class Tweet(models.Model):
    text = models.CharField(max_length=140)
    image = models.ImageField(blank=True, null=True)
    author = models.ForeignKey("User", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


class User(DjangoUser):
    follows = models.ManyToManyField("User")
    retweets = models.ManyToManyField(Tweet)
