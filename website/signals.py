from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ProgramDesign, Announcement, DisplayBibleQuotes,BibleQuote,TemplateForBibleQuote

@receiver(post_save, sender=ProgramDesign)
def create_announcement(sender, instance, created, **kwargs):
    if created:
        announcement_context = f"Check the new design for {instance.title}: {instance.description}"

        if instance.image:
            Announcement.objects.create(
            title = f"New Program Design: {instance.title}",
            content=announcement_context,
            image=instance.image
        )
        
        else:
            Announcement.objects.create(
            title = f"New Program Design: {instance.title}",
            content=announcement_context
        )


# Linking media post and bible study post together to display daily bible quote
def link_or_create_announcement(instance, related_field, is_bible_quote = False):
    date = instance.dates_posted
    announcement, created = DisplayBibleQuotes.objects.get_or_create(dates_posted=date)

    setattr(announcement, related_field, instance)

    if is_bible_quote:
        announcement.title = instance.title
    announcement.save()

@receiver(post_save, sender=BibleQuote)
def create_announcement_for_bible_quote(sender, instance, created, **kwargs):
    link_or_create_announcement(instance, 'bible_quote', is_bible_quote=True)
@receiver(post_save, sender=TemplateForBibleQuote)
def create_announcement_for_media_template(sender, instance, created, **kwargs):
    link_or_create_announcement(instance, 'media_template')
