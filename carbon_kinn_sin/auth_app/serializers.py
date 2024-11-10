from rest_framework import serializers
from .models import User
from core.serializers import StickerCollectionSerializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True},  # Password is write-only
            'email': {'required': True}  
        }

    def create(self, validated_data):
        """Create and return a new user instance, using hashed password."""
        user = User(**validated_data)
        user.set_password(validated_data['password'])  # Hash the password
        user.save()
        return user

class UserSerializer(serializers.ModelSerializer):
    """Serializer for User Profile, including collected stickers."""
    collected_stickers = StickerCollectionSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'ph_num', 'collected_stickers']
