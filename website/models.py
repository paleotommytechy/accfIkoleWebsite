from django.db import models
from django.utils import timezone
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
    

class BibleQuote(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    dates_posted = models.DateField(help_text="Date when this quote should be displayed")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['dates_posted']

    def __str__(self):
        return f"{self.title} - {self.dates_posted}"


class TemplateForBibleQuote(models.Model):
    title = models.CharField(max_length=255)
    template_file = models.ImageField(upload_to='media_templates/')
    dates_posted = models.DateField(help_text="Date when this template should be displayed")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['dates_posted']

    def __str__(self):
        return f"{self.title} - {self.dates_posted}"

class DisplayBibleQuotes(models.Model):
    title = models.CharField(max_length=255)
    bible_quote = models.ForeignKey(BibleQuote, on_delete=models.SET_NULL, null=True, blank=True)
    media_template = models.ForeignKey(TemplateForBibleQuote, on_delete=models.SET_NULL,null=True, blank=True)
    dates_posted = models.DateField(help_text="Date when this annoucement should be displayed")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['dates_posted']

    def __str__(self):
        return f"Bible quote for {self.dates_posted}"

    @staticmethod
    def get_today_quote():
        today = timezone.now().date()
        return DisplayBibleQuotes.objects.filter(dates_posted=today)