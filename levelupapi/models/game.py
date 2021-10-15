from django.db import models
from django.contrib.auth.models import User
from .gametype import Gametype


class Game(models.Model):

    title = models.CharField(max_length=50)
    maker = models.CharField(max_length=50)
    gamer = models.ForeignKey(User, on_delete=models.CASCADE)
    game_type = models.ForeignKey(Gametype, on_delete=models.CASCADE)
    number_of_players = models.IntegerField()
    skill_level = models.IntegerField()
