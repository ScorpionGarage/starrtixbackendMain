# public_events/serializers.py

from rest_framework import serializers
from Event.models import Event, ticket  # Adjust the import path as needed
from User.serializer import RegisterSerializer  # Assuming this exists

class PublicTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = ticket
        fields = '__all__'

class PublicEventSerializer(serializers.ModelSerializer):
    organizer = RegisterSerializer(read_only=True)
    tickets = PublicTicketSerializer(source='ticket_set', many=True, read_only=True)
    
    class Meta:
        model = Event
        fields = '__all__'



