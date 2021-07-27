from django.db import models

# Create your models here.


class TeleBot(models.Model):
    userid = models.CharField(max_length=100, null=True)
    username = models.CharField(max_length=100, null=True)
    first_name = models.CharField(max_length=100, null=True)
    fat_btn = models.IntegerField(default=0)
    dumb_btn = models.IntegerField(default=0)
    stupid_btn = models.IntegerField(default=0)
