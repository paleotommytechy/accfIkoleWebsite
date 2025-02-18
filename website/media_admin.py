from django.contrib.admin import AdminSite
from django.contrib import admin
from django.contrib.auth.mixins import UserPassesTestMixin
from .models import ProgramDesign

class MediaAdminSite(AdminSite):
    site_header = "Media Team Admin"
    site_title = "Media Admin Portal"
    index_title = "Welcome to Media Team"

    def has_permission(self, request):
        return request.user.is_active and request.user.groups.filter(name='Media Team').exists()

media_admin_site = MediaAdminSite(name='media_admin')

class ProgramDesignAdmin(admin.ModelAdmin):
    list_display = ['title','category','uploaded_by','uploaded_at']
    list_filter = ['uploaded_at']
    list_fields = ['title', 'uploaded_by__username']

media_admin_site.register(ProgramDesign,ProgramDesignAdmin)