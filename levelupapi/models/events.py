from django.db import models
from .game import Game
from .gamer import Gamer


class Event(models.Model):

    organizer = models.ForeignKey('Gamer', on_delete=models.CASCADE)
    description = models.TextField(max_length=200)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    attendees = models.ManyToManyField(
        "Gamer", related_name="events"
    )

    @property
    def joined(self):
        return self.__joined

    @joined.setter
    def joined(self, value):
        self.__joined = value
