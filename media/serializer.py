from rest_framework import serializers
from .models import blogMedia, eventMedia, profilePicture

class BlogMedia(serializers.ModelSerializer):
    class Meta:
        model = blogMedia
        fields ='__all__'
        read_only_fields = ('blog',)
        
        
class EventMedia(serializers.ModelSerializer):
    class Meta:
        model = eventMedia
        fields ='__all__'
        read_only_fields = ('event',)
        
        
class ProfilePic(serializers.ModelSerializer):
    class Meta:
        model = profilePicture
        fields ='__all__'
        read_only_fields = ('User',)
