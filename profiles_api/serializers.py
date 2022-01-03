# serializer allows us to easily convert data input into python objects, vice versa (this is required for put/post requests)
from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing out APIView"""
    name = serializers.CharField(max_length=10)