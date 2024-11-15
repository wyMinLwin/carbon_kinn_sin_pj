# Generated by Django 5.1.2 on 2024-11-02 12:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StickerType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='core/media')),
            ],
        ),
        migrations.CreateModel(
            name='Sticker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True)),
                ('lat', models.FloatField(null=True, blank=True)),
                ('lng', models.FloatField(null=True, blank=True)),
                ('sticker_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stickers', to='stickers.stickertype')),
            ],
        ),
    ]
