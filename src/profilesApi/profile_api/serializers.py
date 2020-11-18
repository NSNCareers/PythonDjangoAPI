from rest_framework import serializers
from . import models

class HelloSerializer(serializers.Serializer):
    """Serialises a name field for testing our view"""

    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our profile objects"""

    class Meta:
        model = models.UserProfile
        fields = ('id','email','firstName','lastName','password')
        extra_kwargs = {'password':{'write_only':True}}

    def create(self, validated_data):
        """Create and return a new user"""

        user = models.UserProfile(
            email = validated_data['email'],
            firstName = validated_data['firstName'],
            lastName = validated_data['lastName'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

class ProfilefeeditemSerializer(serializers.ModelSerializer):
    """A serializer for profile feed iteems"""

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id','user_profile','status_text','create_on')
        extra_kwargs = {'user_profile':{'read_only':True}}