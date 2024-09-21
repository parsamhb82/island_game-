from django.db import models
from django.contrib.auth.models import User
from user.models import Player

class Bottle(models.Model):
    sender = models.ForeignKey(Player, on_delete=models.CASCADE)
    reciever = models.ForeignKey(Player, on_delete=models.CASCADE)
    message = models.CharField(max_length=100) 
    date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=0)
    def __str__(self):
        return self.message
    

