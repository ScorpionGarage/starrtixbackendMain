from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import eventMedia, blogMedia, profilePicture
from .serializer import EventMedia, ProfilePic, BlogMedia
# Create your views here.

        
        
class ProfilePicView(viewsets.ModelViewSet):
    queryset = profilePicture.objects.all()
    serializer_class = ProfilePic
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def create(self, request, *args, **kwargs):

     # Check if the current user already has a profile picture
        if ProfilePicture.objects.filter(User=request.user).exists():
            return Response({
                'message': 'Profile picture already exists. You can update or delete your existing profile picture.'
            }, status=status.HTTP_400_BAD_REQUEST)

        # Proceed with the normal creation process if no existing profile picture is found
        return super(ProfilePicView, self).create(request, *args, **kwargs)
    def perform_create(self,serializer):
        serializer.save(User=self.request.user)
        
        
        
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