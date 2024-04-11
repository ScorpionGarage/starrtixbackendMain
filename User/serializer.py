from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('id','username', 'email', 'password', 'first_name', 'last_name', 'phonenumber', 'date_of_birth')
        
    def create(self, validated_data):
        
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phonenumber=validated_data['phonenumber'],
            date_of_birth=validated_data['date_of_birth']
        )
        return user
        def update(self, instance, validated_data):
             instance.email = validated_data.get('email', instance.email)
             instance.first_name = validated_data.get('first_name', instance.first_name)
             instance.last_name = validated_data.get('last_name', instance.last_name)
        # Handle password update with care
             if validated_data.get('password'):
                 instance.set_password(validated_data['password'])
             instance.save()
             return instance
