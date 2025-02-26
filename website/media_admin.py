from django.contrib.admin import AdminSite
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.admin.models import LogEntry
from .models import ProgramDesign,TemplateForBibleQuote

class MediaAdminSite(AdminSite):
    site_header = "Media Team Admin"
    site_title = "Media Admin Portal"
    index_title = "Welcome to Media Team"

    def has_permission(self, request):
        return request.user.is_active and request.user.groups.filter(name='Media Team').exists()
    

    def index(self, request, extra_context = None):
        extra_context = extra_context or {}
        media_team_users = User.objects.filter(groups__name="Media Team")
        recent_actions = LogEntry.objects.filter(
            user__in = media_team_users
        ).order_by('-action_time')[:10]

        extra_context['recent_actions'] = recent_actions
        return super().index(request, extra_context=extra_context)

media_admin_site = MediaAdminSite(name='media_admin')


class TemplateForBibleQuoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'dates_posted')
    search_fields = ('title','dates_posted' )
    list_filter = ('title','dates_posted',)

media_admin_site.register(TemplateForBibleQuote, TemplateForBibleQuoteAdmin)