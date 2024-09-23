from django.contrib.admin import register, ModelAdmin
from .models import Bottle, ToBuyBottle
@register(Bottle)
class BottleAdmin(ModelAdmin):
    list_display = ['sender', 'reciever', 'message', 'date', 'status']

@register(ToBuyBottle)
class ToBuyBottleAdmin(ModelAdmin):
    list_display = ['price', 'radius']
