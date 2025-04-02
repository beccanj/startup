from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    courseone = models.CharField(max_length=100, blank=True, null=True)  # Store the course template name

    def __str__(self):
        return self.title