from django.shortcuts import render
from user.models import *
from .models import Bottle
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serilizers import *
from rest_framework.generics import CreateAPIView
import random


class CreateBottleView(CreateAPIView):
    serializer_class = CreateBottleSerilizer
    queryset = Bottle.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        sender = self.request.user.player
        users = Player.objects.all()
        eligble_users = []
        for user in users:
            if ((sender.x - user.x)**2 + (sender.y - user.y)**2)**0.5 <= sender.score and ((sender.x - user.x)**2 + (sender.y - user.y)**2)**0.5 != 0 :
                eligble_users.append(user)

        if len(eligble_users) == 0:
            return Response({'message': 'no one is eligble to receive the bottle'})
        n = random.randint(0, len(eligble_users) - 1)
        Bottle.objects.create(sender=sender, reciever=eligble_users[n], message=serializer.validated_data['message'])
        sender.score -= 1
        eligble_users[n].score += 1
        sender.save()
        eligble_users[n].save()

