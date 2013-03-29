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
    
    @classmethod
    def games_by_creator(cls, creator):
        return cls.objects.filter(creator=creator)
    
    @classmethod
    def for_id(cls, id):
        return cls.objects.get(pk=id)        
    
class Player(models.Model):
    fb_id = models.CharField(max_length=50, unique=True, blank=True, null=True)
    name = models.CharField(max_length=100)
    
    @classmethod
    def for_fb_id(cls, fb_id):
        return cls.objects.get(fb_id=fb_id)

class PlayerGame(models.Model):
    player = models.ForeignKey(Player)
    game = models.ForeignKey(Game)
    chance_attending = models.SmallIntegerField(choices=ChanceAttendingConstants.choices_for_model())
    
    @property
    def verbose_status(self):
        return ChanceAttendingConstants.get_verbose(self.chance_attending)

    @classmethod
    def players_in_games(cls, games):
        return cls.objects.filter(game__in=games)
    
    @classmethod
    def all_players_for_game(cls, game):
        return [pg.player for pg in cls.objects.filter(game=game).all()]
        
