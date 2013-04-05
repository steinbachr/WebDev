import json
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from pickup_finder.constants import *
    
class Game(models.Model):
    creator = models.ForeignKey(User)
    #location info
    latitude = models.DecimalField(max_digits=10, decimal_places=6)
    longitude = models.DecimalField(max_digits=10, decimal_places=6)
    normalized_location = models.CharField(max_length=200)
    #meta info
    public = models.BooleanField()
    person_cap = models.IntegerField(blank=True, null=True)
    game_type = models.SmallIntegerField(choices=GameTypeConstants.choices_for_model())
    #datetime fields
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    starts_at = models.DateTimeField()
    
    @property
    def rsvp_link(self):
        return 'http://instapickup-steinbachr.dotcloud.com%s' % reverse('pickup_finder.views.game_rsvp', args=(self.id,))
    
    @property
    def players_count(self):
        return PlayerGame.objects.filter(game=self.id).count()
    
    @property
    def can_rsvp(self):
        return self.players_count < self.person_cap or (self.public and self.person_cap is None)
    
    @property
    def verbose_game_type(self):
        return GameTypeConstants.get_verbose(self.game_type)
    
    @classmethod
    def public_games(cls):
        return cls.objects.filter(public=True).all()
    
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
    
    
class Notification(models.Model):
    game = models.ForeignKey(Game)
    player = models.ForeignKey(Player, blank=True, null=True)
    type = models.SmallIntegerField(choices=NotificationTypeConstants.choices_for_model())
    seen = models.BooleanField()
        
    @property
    def format_notification(self):
        formatter = NotificationTypeConstants.get_verbose(self.type)
        return formatter(self.player, self.game)
        
    @classmethod
    def unseen_notifications(cls, user):        
        return cls.objects.filter(game__creator=user).filter(seen=False).all()
    
    @classmethod
    def mark_as_seen(cls, user):
        '''when the user clicks the notifications, for now we'll just assume hes seen everything
        so we use this method to mark all the notifications for a user as seen'''
        unseen = cls.unseen_notifications(user)
        for notif in unseen:
            notif.seen = True
            notif.save()                        
