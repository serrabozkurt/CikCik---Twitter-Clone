from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    category = models.SmallIntegerField(choices=(
        (1, "Python"),
        (2, "Django"),
        (3, "PyCharm")
    ))
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
