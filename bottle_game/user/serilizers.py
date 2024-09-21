from rest_framework import serializers
from django.contrib.auth.models import User
from user.models import Player
import random

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        x = random.randint(1, 1000000)
        y = random.randint(1, 1000000)
        
        Player.objects.create(user=user, x = x, y = y)
        return user
    def validate(self, data):
        password = data.get('password')
        if len(password) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")
        username = data.get('username')
        if len(username) < 3:
            raise serializers.ValidationError("Username must be at least 3 characters long.")
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError("Username already exists.")
        return data