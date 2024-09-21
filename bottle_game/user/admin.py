from django.contrib.admin import register, ModelAdmin
from .models import Player

@register(Player)
class PlayerAdmin(ModelAdmin):
    list_display = ['user', 'score', 'x', 'y']


