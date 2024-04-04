from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import eventMedia, blogMedia, profilePicture
from .serializer import EventMedia, ProfilePic, BlogMedia
# Create your views here.
class EventMediaView(viewsets.ModelViewSet):
    queryset = eventMedia.objects.all()
    serializer_class = EventMedia
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self,serializer):
        serializer.save(event=self.request.user)
        
        
        
class BlogMediaView(viewsets.ModelViewSet):
    queryset = blogMedia.objects.all()
    serializer_class = BlogMedia
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self,serializer, request, *args, **kwargs):
        serializer.save(blog=self.request.user)
        
        
class ProfilePicView(viewsets.ModelViewSet):
    queryset = profilePicture.objects.all()
    serializer_class = ProfilePic
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self,serializer, request, *args, **kwargs):
        serializer.save(User=self.request.user)