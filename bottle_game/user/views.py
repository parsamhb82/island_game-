from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView
from .serilizers import UserRegisterSerializer, PlayerScoreSheetSerializer
from rest_framework.generics import ListAPIView
from .models import Player
from django.db.models import F


class Login(TokenObtainPairView):
    pass

class Refresh(TokenRefreshView):
    pass 

class RegisterPlayerView(CreateAPIView):
    serializer_class = UserRegisterSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        serializer.save()

    def create(self, request, *args, **kwargs):
        serilizer = self.get_serializer(data = request.data)
        if serilizer.is_valid():
            self.perform_create(serilizer)
            return Response(serilizer.data, status=status.HTTP_201_CREATED)
        return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PlayersScoresSheet(ListAPIView):

    serializer_class = PlayerScoreSheetSerializer
    queryset = Player.objects.all().order_by(F('total_read_bottles').desc(nulls_last=True))
    permission_classes = [IsAuthenticated]

import uuid
class FillTheMap(APIView):
    #permission_classes = [IsAuthenticated]#need to be implemented
    def get(self, request):
        x = 1
        y = 0
        while x < 10000 and y < 10000:
            username = str(uuid.uuid4())[:16]
            password = str(uuid.uuid4())[:16]
            email = f"{str(uuid.uuid4())[:8]}@example.com"
            user = User.objects.create_user(username=username, password=password, email=email)
            player = Player.objects.create(user=user, x=x, y=y)
            x += 10
            y += 10
        return Response({'message': 'Map filled successfully'}, status=status.HTTP_200_OK)

        
        