from django.contrib.admin import AdminSite
from django.contrib import admin
from .models import BibleQuote

class BibleStudyAdminSite(AdminSite):
    site_header = "Bible Study Admin"
    site_title = "Bible Study Admin Portal"
    index_title = "Welcome to Bible Study Unit"

    def has_permission(self, request):
        return request.user.is_active and request.user.groups.filter(name='Bible Study Unit').exists()

bible_study_admin_site = BibleStudyAdminSite(name='bible_study_unit')

class BibleQuoteAdmin(admin.ModelAdmin):
    list_display = ['title','dates_posted']
    list_filter = ['dates_posted']
    list_fields = ['title', 'created_at']

bible_study_admin_site.register(BibleQuote,BibleQuoteAdmin)