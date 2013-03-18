import json
from django.db import models
from django.contrib.auth.models import User
from pickup_finder.constants import ChanceAttendingConstants
    
class Game(models.Model):
    creator = models.ForeignKey(User)
    #location info
    latitude = models.DecimalField(max_digits=10, decimal_places=6)
    longitude = models.DecimalField(max_digits=10, decimal_places=6)
    normalized_location = models.CharField(max_length=200)
    #meta info
    public = models.BooleanField()
    person_cap = models.IntegerField(blank=True, null=True)
    #datetime fields
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    starts_at = models.DateTimeField() 
    
class Player(models.Model):
    fb_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)

class PlayerGame(models.Model):
    player = models.ForeignKey(Player)
    game = models.ForeignKey(Game)
    chance_attending = models.SmallIntegerField(choices=ChanceAttendingConstants.choices_for_model())
