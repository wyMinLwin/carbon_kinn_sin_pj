# Generated by Django 5.1.2 on 2024-11-10 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stickers', '0002_remove_stickertype_image_sticker_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='sticker',
            name='special',
            field=models.BooleanField(default=False),
        ),
    ]
