from django.contrib import admin
from .models import Announcement, DisplayBibleQuotes,BibleQuote, TemplateForBibleQuote

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted')
    search_fields = ('title', 'content')
    list_filter = ('date_posted',)

class DisplayBibleQuotesAdmin(admin.ModelAdmin):
    list_display = ['title','bible_quote','dates_posted']
    list_filter = ['dates_posted']
    list_fields = ['title','bible_quote','created_at']

admin.site.register(DisplayBibleQuotes,DisplayBibleQuotesAdmin)

class BibleQuoteAdmin(admin.ModelAdmin):
    list_display = ['title','dates_posted']
    list_filter = ['dates_posted']
    list_fields = ['title', 'created_at']

admin.site.register(BibleQuote,BibleQuoteAdmin)

class TemplateForBibleQuoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'dates_posted')
    search_fields = ('title','dates_posted' )
    list_filter = ('dates_posted',)

admin.site.register(TemplateForBibleQuote, TemplateForBibleQuoteAdmin)
