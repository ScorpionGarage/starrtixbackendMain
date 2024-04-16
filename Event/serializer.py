from rest_framework import serializers
from .models import Event, ticket,Booking,invitation

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        read_only_fields = ('organizer',)


class ticketSerializer(serializers.ModelSerializer):
    class Meta:
        model = ticket 
        fields = '__all__'
        read_only_fields = ('event',)


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Booking
        fields='__all__'
        read_only_fields=['booked_on','unique_id', 'qrcode' ]
        
        def validate_number_of_tickets(self, value):
            if value<=0:
                raise serializers.ValidationError("Number of tickets should be a positive")
            return value
class InvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model=invitation
        fields='__all__'
        read_only_fields=['unique_id', 'qrcode' ]
        
    