from django.contrib.auth import get_user_model
from django.db import models
from stickers.models import Sticker

User = get_user_model()
class StickerCollection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sticker = models.ForeignKey(Sticker, on_delete=models.CASCADE)
    collected_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'sticker')

    def __str__(self):
        return f"{self.user.email} collected {self.sticker.code}"

class Reward(models.Model):
    TIER_CHOICES = [
        (1, 'Tier 1: Respective sticker pack (3 stickers)'),
        (2, 'Tier 2: Pouch (6 stickers)'),
        (3, 'Tier 3: Purple upcycled things (9 stickers)'),
        (4, 'Tier 3: Tote bag (12 stickers)'),
        (5, 'Tier 3: Water bottle (15 stickers)'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    threshold = models.PositiveIntegerField()  
    tier = models.PositiveSmallIntegerField(choices=TIER_CHOICES, unique=True)
    required_stickers = models.ManyToManyField(Sticker, related_name='rewards', blank=True)

    def __str__(self):
        return self.name
    
    def get_required_stickers(self):
        return ", ".join([sticker.code for sticker in self.required_stickers.all()])
    
class RewardUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reward = models.ForeignKey(Reward, on_delete=models.CASCADE)
    awarded_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'reward') 

    def __str__(self):
        return f"{self.user.email} received {self.reward.name} on {self.awarded_at}"