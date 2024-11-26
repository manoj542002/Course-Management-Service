from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    video = models.FileField(upload_to='videos/', null = True, blank = True)
    def __str__(self):
        return f"{self.title} ({self.duration} days)"