from django.db import models
from django.contrib.auth.models import User

class Announcement(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to = 'uploads/media/', blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Creating a model for Media team upload
class ProgramDesign(models.Model):
    CATEGORY_CHOICES = [
        ('sunday_service','Sunday Service'),
        ('bible_study','Bible Study'),
        ('prayer_meeting','Prayer Meeting'),
        ('special_program','Special Program'),
        ('other','Other'),
    ]

    title = models.CharField(max_length = 255, help_text="Enter the title of the upload(e.g, 'Sunday Service Banner')")
    description = models.TextField(blank=True, null=True, help_text="Optional description of the media")
    image = models.ImageField(upload_to = 'uploads/media/', help_text="Upload an image, video or document")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other'),
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, help_text="User who uploaded the file")

    class Meta:
        ordering =['-uploaded_at']
        verbose_name = "Media Upload"
        verbose_name_plural = "Media Uploads"

    def __str__(self):
        return f"{self.title} - {self.category}"