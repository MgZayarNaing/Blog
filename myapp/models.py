from django.db import models
import uuid
# from ckeditor.fields import RichTextField
from datetime import datetime
from django.contrib.auth.models import User


class HomeModel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    img = models.ImageField(default=None)
    title = models.CharField(max_length=255, null=True, blank=True)
    contact = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title


# Create your models here.
class BlogModel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    img = models.ImageField(default=None)
    title = models.CharField(max_length=255, null=True, blank=True)
    contact = models.TextField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

class AboutModle(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    img = models.ImageField(default=None)
    title = models.CharField(max_length=255, null=True, blank=True)
    contact = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title