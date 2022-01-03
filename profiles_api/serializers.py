# serializer allows us to easily convert data input into python objects, vice versa (this is required for put/post requests)
from rest_framework import serializers
from profiles_api import models


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing out APIView"""
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile project"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        # I only want to display password field as write-only
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

# override django normal use of create function to use our own create user function
    def create(self, validated_data):
        """Create and return a new user"""
        # create user function is in the userprofilemanager class
        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password']
        )
        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
 
        return super().update(instance, validated_data)