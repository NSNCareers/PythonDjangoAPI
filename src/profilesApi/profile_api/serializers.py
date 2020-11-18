from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serialises a name field for testing our view"""

    name = serializers.CharField(max_length=10)