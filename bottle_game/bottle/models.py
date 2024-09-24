from django.db import models
from django.contrib.auth.models import User

class ToBuyBottle(models.Model):
    price = models.IntegerField()
    radius = models.IntegerField()
    max_lenght = models.IntegerField(default=300)
    def __str__(self) -> str:
        return f"{self.price} - {self.radius}"
class Bottle(models.Model):
    bought_bottle = models.ForeignKey(ToBuyBottle, on_delete=models.PROTECT, related_name= "bought", blank=True, null=True)
    sender = models.ForeignKey('user.Player', on_delete=models.CASCADE, related_name="sender_player")
    reciever = models.ForeignKey('user.Player', on_delete=models.CASCADE, related_name="reciever_player", blank=True, null=True)
    is_sent = models.BooleanField(default=False)
    message = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    sent_date = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(default=0)
    def __str__(self):
        return self.sender.user.username

    

