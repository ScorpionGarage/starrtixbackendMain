from rest_framework import viewsets, permissions, status
from .models import Event, ticket, Booking
from .serializer import EventSerializer, ticketSerializer, BookingSerializer
from rest_framework.response import Response
import qrcode
from uuid import UUID
from django.shortcuts import get_object_or_404
from io import BytesIO
from django.core.files import File
from rest_framework.decorators import action

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
# Assuming you're passing the event ID in the request data
        event_id = self.request.data.get('event')  
        event = Event.objects.get(id=event_id)
        serializer.save(event=event)      
    def create(self, request, *args, **kwargs):
         # Check if any ticket exists for the event
        event_id = request.data.get('event')
        existing_tickets = ticket.objects.filter(event_id=event_id)
        
        if existing_tickets.exists():
            return Response({"error": "Tickets already exist for this event"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"message": "Ticket successfully created", "statusCode":status.HTTP_200_OK}, status=status.HTTP_200_OK, headers=headers)  
        
class BookingViewset(viewsets.ModelViewSet):
    queryset=Booking.objects.all()
    serializer_class= BookingSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        event_id=serializer.validated_data['event'].id
        event=Event.objects.get(id=event_id)
        num_tickets_requested= serializer.validated_data.get('number_of_tickets', 1)
  
        try:
            tickets = ticket.objects.get(event=event)
            if tickets.ticketleft >= num_tickets_requested:
                self.perform_create(serializer)
                tickets.ticketsold += num_tickets_requested
                tickets.save()
                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
            else:
                return Response({'error': 'Not enough tickets available'}, status=status.HTTP_400_BAD_REQUEST)
        except tickets.DoesNotExist:
            return Response({'error': 'No ticket available for this event'}, status=status.HTTP_400_BAD_REQUEST)
    @action(detail=False, methods=['get'], url_path='by-unique-id/(?P<unique_id>[^/.]+)')
    def get_by_unique_id(self, request, unique_id=None):
        """
        Retrieve a booking by its unique ID.
        """
        try:
            # Validate that the unique_id is a valid UUID
            uuid_obj = UUID(unique_id, version=4)
        except ValueError:
            return Response({"error": "Invalid UUID format"}, status=status.HTTP_400_BAD_REQUEST)

        booking = get_object_or_404(Booking, unique_id=uuid_obj)
        serializer = self.get_serializer(booking)
        return Response(serializer.data)
