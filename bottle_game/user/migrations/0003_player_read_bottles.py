# Generated by Django 5.1.1 on 2024-09-23 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_player_daily_heighest_bottles_player_reply_bottles'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='read_bottles',
            field=models.IntegerField(default=0),
        ),
    ]
