from rest_framework import viewsets, permissions
from .models import Event, ticket
from .serializer import EventSerializer, ticketSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)


class ticketViewSet(viewsets.ModelViewSet):
    queryset=ticket.objects.all()
    serializer_class=ticketSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(event=self.request.user)
        