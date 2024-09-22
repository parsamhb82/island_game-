from rest_framework import serializers
from .models import Bottle

class CreateBottleSerilizer(serializers.ModelSerializer):

    class Meta:
        model = Bottle
        fields = ['message']
    
        