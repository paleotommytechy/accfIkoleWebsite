from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ProgramDesign, Announcement

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