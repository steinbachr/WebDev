'''Components are things that are used on multiple pages and do essentially the same thing so we want to be DRY'''
from pickup_finder.models import *
from django.core import serializers
from itertools import chain

class GameLineup():
    def __init__(self, request):
        self.games = list(chain(Game.games_by_creator(request.user),Game.public_games()))
        
    def tpl_vars(self):
        tpl_vars = {}
        
        tpl_vars['google_key'] = APIKeys.GOOGLE        
        tpl_vars['games_json'] = serializers.serialize("json", self.games) 
        tpl_vars['games'] = self.games
        
        return tpl_vars
