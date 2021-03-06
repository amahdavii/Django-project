from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length = 60)
    slug = models.SlugField(max_length = 100)
    body = models.TextField()
    published = models.DateTimeField(default = timezone.now)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    status = models.CharField(max_length = 60, choices = STATUS_CHOICES, default = 'draft')


    def __str__(self):
        return "Post object (id = {} & title = {})".format(self.id, self.title)