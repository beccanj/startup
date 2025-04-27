from base.models import BaseModel
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from farming.models import Practice


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    courseone = models.CharField(max_length=100, blank=True, null=True)  # Store the course template name

    def __str__(self):
        return self.title


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
    slug = models.SlugField(unique=True, blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, null=True)
    practice = models.ForeignKey(Practice, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class UserProfile(BaseModel):
    '''This model will have additional information we may need from a user'''
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    phone_number = models.CharField(max_length=20, blank=True, null=True)
