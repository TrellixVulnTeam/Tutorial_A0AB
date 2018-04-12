from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Game(models.Model):
    first_player  = models.ForeignKey(User,related_name='game_first_name',on_delete=models.CASCADE)
    second_player = models.ForeignKey(User,related_name='game_second-player')
    start_time    = models.DateTimeField(auto_now_add=True)
    last_active   = models.DateTimeField(auto_now=True)

class Move(models.Model):
    x               = models.IntegerField()
    y               = models.IntegerField()
    comment         = models.CharField(max_length=300 , blank=True)
    by_first_player = models.BooleanField()
    game            = models.ForeignKey(Game,on_delete=models.CASCADE)

