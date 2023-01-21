from django.db import models


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
    created = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)

    objects = models.Manager()
    yayinlanmis = PublishedPost()

    class Meta:
        default_manager_name = "yayinlanmis"
