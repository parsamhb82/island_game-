from django.db import models
from django.contrib.auth.models import User


class Bottle(models.Model):
    sender = models.ForeignKey('user.Player', on_delete=models.CASCADE, related_name="sender_player")
    reciever = models.ForeignKey('user.Player', on_delete=models.CASCADE, related_name="reciever_player", blank=True, null=True)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=0)
    def __str__(self):
        return self.message
    

