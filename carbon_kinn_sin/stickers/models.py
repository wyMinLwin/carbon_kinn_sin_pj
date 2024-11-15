from django.db import models

class StickerType(models.Model):
    name = models.CharField(max_length=100)
   
    def __str__(self):
        return self.name

class Sticker(models.Model):
    code = models.CharField(max_length=50, unique=True)  
    sticker_type = models.ForeignKey(StickerType, related_name='stickers', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='core/media')  
    lat = models.FloatField(null=True, blank=True)  # Latitude for geographical location
    lng = models.FloatField(null=True, blank=True)  # Longitude for geographical location
    special = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.code} - {self.sticker_type.name}"
