'''Components are things that are used on multiple pages and do essentially the same thing so we want to be DRY'''
from pickup_finder.models import *
from pickup_finder.constants import *
from django.core import serializers

class GameLineup():
    def __init__(self, request):
        self.games = Game.games_by_creator(request.user)
        self.player_games = PlayerGame.players_in_games(self.games)
        self.players = [pg.player for pg in self.player_games]
        
    def tpl_vars(self):
        tpl_vars = {}
        
        tpl_vars['google_key'] = APIKeys.GOOGLE
        tpl_vars['player_games'] = self.player_games
        tpl_vars['games_json'] = serializers.serialize("json", self.games)
        
        return tpl_vars
        
