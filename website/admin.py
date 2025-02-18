from django.contrib import admin
from .models import Announcement, ProgramDesign

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted')
    search_fields = ('title', 'content')
    list_filter = ('date_posted',)

class ProgramDesignAdmin(admin.ModelAdmin):
    list_display = ['title','category','uploaded_by','uploaded_at']
    list_filter = ['uploaded_at']
    list_fields = ['title', 'uploaded_by__username']

admin.site.register(ProgramDesign, ProgramDesignAdmin)