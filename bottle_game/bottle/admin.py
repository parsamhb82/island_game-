from django.contrib.admin import register, ModelAdmin
from .models import Bottle
@register(Bottle)
class BottleAdmin(ModelAdmin):
    list_display = ['sender', 'reciever', 'message', 'date', 'status']
