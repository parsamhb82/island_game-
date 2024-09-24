from django.shortcuts import render
from user.models import *
from .models import Bottle
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serilizers import *
from rest_framework.generics import CreateAPIView, ListAPIView
import random
from rest_framework import status
from django.utils.timezone import now

class SendBottleView(APIView):
    queryset = Bottle.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = SendBottleSerilizer
    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            sender = request.user.player
            bottle_type = serializer.validated_data['bottle_type']
            message = serializer.validated_data['message']
            bottles = Bottle.objects.filter(sender=sender, bought_bottle=bottle_type, is_sent=False)
            if not bottles.exists():
                return Response({'message': 'You don\'t have a bottle of this type'}, status=status.HTTP_400_BAD_REQUEST)
            bottle = bottles[0]
            if bottle.bought_bottle.max_lenght < len(message):
                return Response({'message': f'message should be less than{bottle.bought_bottle.max_lenght} characters for this specific bottle '}, status=status.HTTP_400_BAD_REQUEST)
            radius = bottle.bought_bottle.radius
            price = bottle.bought_bottle.price
            users = Player.objects.exclude(id=sender.id)
            eligble_users = []
            for user in users:
                if ((sender.x - user.x)**2 + (sender.y - user.y)**2)**0.5 <= radius :
                    eligble_users.append(user)
            if not eligble_users:
                    return Response({'message': 'No eligible users found within the radius'}, status=status.HTTP_400_BAD_REQUEST)
            user = eligble_users[random.randint(0, len(eligble_users)-1)]
            bottle.reciever = user
            bottle.message = message
            bottle.status = 1
            bottle.is_sent = True
            bottle.sent_date = now()
            bottle.save()
            return Response({'message': 'bottle sent successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReadSentBottles(APIView):
    queryset = Bottle.objects.all()
    permission_classes = [IsAuthenticated]
    def get(self, request):
        reciever = self.request.user.player
        if reciever.read_bottles >= reciever.daily_heighest_bottles:
            return Response({'message': 'You have reached your daily limit of reading bottles'}, status=status.HTTP_400_BAD_REQUEST)
        reciever.read_bottles += 1
        bottles = Bottle.objects.filter(reciever=reciever, status=1)
        serilizer = BottleSerilizer(bottles, many=True)
        for bottle in bottles:
            if bottle.status == 1:
                bottle.status = 2
                reciever.score += bottle.bought_bottle.price
                reciever.total_read_bottle += 1
                bottle.save()
        reciever.save()
        return Response(serilizer.data, status= status.HTTP_200_OK)
    
class ViewAvailabeBottlesToBuy(ListAPIView):
    serializer_class = ToBuyBottleSerilizer
    queryset = ToBuyBottle.objects.all()
    permission_classes = [IsAuthenticated]

class BuyBottleView(CreateAPIView):
    queryset = Bottle.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = BuyBottleSerilizer

    def perform_create(self, serializer):
        bought_bottle = self.request.data.get('bought_bottle')
        if not bought_bottle:
            raise serializers.ValidationError({'error': 'bought_bottle is required'})

        sender = self.request.user.player
        bottle_instance = ToBuyBottle.objects.get(id=bought_bottle)
        
        if sender.score < bottle_instance.price:
            raise serializers.ValidationError({'message': 'You don’t have enough score to buy this bottle'})

        sender.score -= bottle_instance.price
        sender.save()
        serializer.save(sender=self.request.user.player, bought_bottle=bottle_instance)

class ViewOwnedBottles(ListAPIView):

    queryset = Bottle.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = OwnedBottlesSerilizer

    def get_queryset(self):
        return Bottle.objects.filter(sender=self.request.user.player, is_sent=False)
    

class ViewAbilitiesTobuy(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        player = request.user.player
        reply = player.reply_bottles
        response = []
        reply_dict = {}
        if not reply:
            reply_dict['ability to reply'] = False
            reply_dict['reply_price'] = 100
            response.append(reply_dict)
        daily = player.daily_heighest_bottles
        response.append({'add daily_highest bottles to ' : daily + 1, 
                         'price': 10})
        return Response(response, status=status.HTTP_200_OK)

class BuyAbilityToReply(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        player = request.user.player
        if player.reply_bottles == True:
            return Response({'message': 'You already have this ability'}, status=status.HTTP_400_BAD_REQUEST)
        if player.score < 100:
            return Response({'message': 'You don\'t have enough score to buy this ability'}, status=status.HTTP_400_BAD_REQUEST)
        player.score -= 100
        player.reply_bottles = True
        player.save()
        return Response({'message': 'You have successfully bought the ability to reply'}, status=status.HTTP_200_OK)
class BuyAbilityToReadMore(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        player = request.user.player
        if player.score < 10:
            return Response({'message': 'You don\'t have enough score to buy this ability'}, status=status.HTTP_400_BAD_REQUEST)
        player.score -= 10
        player.daily_heighest_bottles += 1
        player.save()
        return Response({'message': 'You have successfully bought the ability to read more bottles'}, status=status.HTTP_200_OK)

class ReplyToBottle(APIView):
    serializer_class = ReplySerializer
    queryset = Bottle.objects.all()
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            bottle = serializer.validated_data['bottle']
            message = serializer.validated_data['message']
            if bottle.status != 2:
                return Response({'message': 'You can only reply to bottles that have been read'}, status=status.HTTP_400_BAD_REQUEST)
            sender = request.user.player
            if bottle.reciever != sender :
                return Response({'message': 'You can only reply to bottles that you have received'}, status=status.HTTP_400_BAD_REQUEST)
            if sender.score < 10 :
                return Response({'message': 'You don\'t have enough score to reply to this bottle'}, status=status.HTTP_400_BAD_REQUEST)
            sender.score -= 10
            sender.save()
            Bottle.objects.create(sender=sender, reciever=bottle.sender, message=message, status=1, is_sent=True)
            return Response({'message': 'You have successfully replied to the bottle'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

            
    




