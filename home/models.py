from django.db import models

# Create your models here.


class TeleBot(models.Model):
    userid = models.CharField(max_length=100, null=True)
    username = models.CharField(max_length=100, null=True)
    first_name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.username


class Messages(models.Model):
    user = models.ForeignKey(TeleBot, on_delete=models.CASCADE)
    text = models.TextField(null=True)
