# Generated by Django 5.1.1 on 2024-09-24 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bottle', '0006_bottle_sent_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='tobuybottle',
            name='max_lenght',
            field=models.IntegerField(default=300),
        ),
    ]
