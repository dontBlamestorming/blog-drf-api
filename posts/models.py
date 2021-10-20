from django.conf import settings
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128)


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=128)
    sub_title = models.CharField(max_length=128, default="")
    content = models.TextField()
    thumbnail_url = models.CharField(max_length=128)
    post_date = models.DateField(auto_now_add=True)

