from django.db import models
from django.contrib.auth.models import User
from bottle.models import Bottle

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=100)
    x = models.BigIntegerField()
    y = models.BigIntegerField()
    daily_heighest_bottles = models.IntegerField(default=3)
    read_bottles = models.IntegerField(default=0)
    reply_bottles = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username