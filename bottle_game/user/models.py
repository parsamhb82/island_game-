from django.db import models
from django.contrib.auth.models import User
from bottle.models import Bottle

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=100)
    x = models.BigIntegerField()
    y = models.BigIntegerField()

    def __str__(self):
        return self.user.username