from django.contrib.auth.models import User
from rest_framework import serializers


class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User(username=validated_data["username"], email=validated_data["email"])
        user.set_password(validated_data["password"])
        user.save()
        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField(required=False, allow_blank=True)
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        username = data.get('username')
        password = data.get('password')
        
        if not email and not username:
            raise serializers.ValidationError("Must include either 'username' or 'email'.")
        
        if not password:
            raise serializers.ValidationError("Must include password.")
        
        return data