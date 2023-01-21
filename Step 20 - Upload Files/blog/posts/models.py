from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=25)


class PublishedPost(models.Manager):
    def get_queryset(self):
        return super(PublishedPost, self).get_queryset()\
            .filter(published=True)\
            .order_by("-created")


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    cover_photo = models.ImageField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)

    objects = models.Manager()
    yayinlanmis = PublishedPost()

    class Meta:
        default_manager_name = "objects"
