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
    published = models.DataTime(default = timezone.now)
    created = models.DataTime(auto_now_add = True)
    updated = models.DataTime(auto_now = True)
    status = models.CharField(max_length = 60, choices = STATUS_CHOICES, default = 'draft')
    