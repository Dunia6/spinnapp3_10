from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user


class ProfileSerialiser(serializers.ModelSerializer):
    """ Serializer de la classe Profile """
    user = serializers.PrimaryKeyRelatedField(read_only = True)
    
    class Meta:
        model = Profile
        fields = ['first_name', 'name', 'last_name', 'birth', 'created_time', 'updated_time', 'user']
        read_only_fields = ('created_time', 'updated_time', 'user')
    
    def create(self, validated_data):
        return Profile.objects.create(**validated_data)