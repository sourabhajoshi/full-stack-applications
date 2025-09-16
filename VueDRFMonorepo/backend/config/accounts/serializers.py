from rest_framework import serializers
from .models import User, Profile, Role


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'first_name', 'last_name', 'phone_number', 'avatar_url', 'bio']  # Convert all model fields to JSON


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=False)  # Nested serializer: allows creating User + Profile together.

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'profile']
        extra_kwargs = {
            'password': {'write_only': True}}  # write_only=True → password cannot be read via API, only written.

    def create(self, validated_data):
        profile_data = validated_data.pop('profile', None)
        user = User.objects.create_user(**validated_data)
        if profile_data:
            Profile.objects.create(user=user, **profile_data)
        return user
