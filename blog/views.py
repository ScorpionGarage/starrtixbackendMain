from rest_framework import viewsets, permissions
from .models import blog
from .serializer import blogSerializer

class blogViewSet(viewsets.ModelViewSet):
    queryset=blog.objects.all()
    serializer_class = blogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    
    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)