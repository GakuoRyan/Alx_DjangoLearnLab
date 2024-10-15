from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'bio', 'profile_picture')  # Customize as needed

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(), get_user_model().objects.create_user

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'bio', 'profile_picture')  # Include fields as necessary

    def create(self, validated_data):
        # Create a user using the create_user method
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],  # Password should be hashed
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture', None)
        )
        # Create a token for the newly created user
        Token.objects.create(user=user)
        return user
