from django.db import models
from django.utils import timezone
# Create your models here.

class Category(models.Model):
    id = models.CharField(max_length=150)

    def __str__(self):
        return self.id


class News(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'DRAFT'
        Published = 'PB', 'Published'

    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300)
    body = models.TextField()
    image = models.ImageField(upload_to='news/images')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    publish_time = models.DateTimeField(default=timezone.now)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)

    # class Meta:
    #     ordering = ["-publish_time"]

    def __str__(self):
        return self.title