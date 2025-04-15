from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    courseone = models.CharField(max_length=100, blank=True, null=True)  # Store the course template name

    def __str__(self):
        return self.title

from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField  # if you're using CKEditor

class Article(models.Model):
    CATEGORY_CHOICES = [
        ('Crops', 'Crops'),
        ('Livestock', 'Livestock'),
        ('Soil', 'Soil'),
        ('Pests', 'Pests'),
        ('SmartAgri', 'SmartAgri'),
    ]

    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    title_tag = models.CharField(max_length=255, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='article_images/', blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
