# Generated by Django 5.1.1 on 2025-02-18 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_announcement_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='announcement',
            name='file',
        ),
        migrations.RemoveField(
            model_name='programdesign',
            name='file',
        ),
        migrations.AddField(
            model_name='announcement',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/media/'),
        ),
        migrations.AddField(
            model_name='programdesign',
            name='image',
            field=models.ImageField(default='', help_text='Upload an image, video or document', upload_to='uploads/media/'),
            preserve_default=False,
        ),
    ]
