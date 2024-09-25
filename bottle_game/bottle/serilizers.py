from rest_framework import serializers
from .models import Bottle, ToBuyBottle

class CreateBottleSerilizer(serializers.ModelSerializer):

    class Meta:
        model = Bottle
        fields = ['message']

class BottleSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Bottle
        fields = ['id', 'message']

class ToBuyBottleSerilizer(serializers.ModelSerializer):
    class Meta:
        model = ToBuyBottle
        fields = '__all__'

class BuyBottleSerilizer(serializers.ModelSerializer):
    bought_bottle = serializers.PrimaryKeyRelatedField(queryset =Bottle.objects.all(), required=True)
    class Meta:
        model = Bottle
        fields = ['bought_bottle']

class OwnedBottlesSerilizer(serializers.ModelSerializer):
    price = serializers.IntegerField(source='bought_bottle.price')
    radius = serializers.FloatField(source='bought_bottle.radius')

    class Meta:
        model = Bottle
        fields = ['price', 'radius']

class SendBottleSerilizer(serializers.Serializer):
    bottle_type = serializers.IntegerField(required=True)
    message = serializers.CharField(required=True)

class ReplySerializer(serializers.Serializer):
    bottle = serializers.PrimaryKeyRelatedField(queryset=Bottle.objects.all(), required=True)
    message = serializers.CharField(required=True)

    
        