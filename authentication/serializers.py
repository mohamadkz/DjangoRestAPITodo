from rest_framework import serializers
from authentication.models import User
from django.core.validators import MinLengthValidator


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        max_length=128, validators=[MinLengthValidator(6)], write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        max_length=128, validators=[MinLengthValidator(6)], write_only=True)

    class Meta:
        model = User
        fields = ('email','username' ,'password', 'token')

        read_only_fields = ['token']