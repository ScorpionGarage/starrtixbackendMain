# public_events/views.py

from rest_framework import viewsets, permissions
from Event.models import Event  # Adjust the import path as needed
from .serializer import PublicEventSerializer

class PublicEventViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing events and their tickets publicly.
    """
    queryset = Event.objects.all()
    serializer_class = PublicEventSerializer
    permission_classes = [permissions.AllowAny]  # No authentication required
