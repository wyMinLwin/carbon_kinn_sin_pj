# Generated by Django 5.1.2 on 2024-11-02 13:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stickers', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('threshold', models.PositiveIntegerField()),
                ('tier', models.PositiveSmallIntegerField(choices=[(1, 'Tier 1: Completion of 1 Theme'), (2, 'Tier 2: Completion of 3 Themes'), (3, 'Tier 3: Completion of All Themes')], unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='StickerCollection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collected_at', models.DateTimeField(auto_now_add=True)),
                ('sticker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stickers.sticker')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'sticker')},
            },
        ),
    ]
