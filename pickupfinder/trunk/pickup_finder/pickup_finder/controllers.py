from pickup_finder.forms import *
from pickup_finder.constants import *
from pickup_finder.models import *
from django.core import serializers
from django.db import IntegrityError

class Controller():
    def __init__(self, request):
        self.request = request

class AjaxController(Controller):
    def __init__(self, request):
        Controller.__init__(self, request)
        
class PortalController(Controller):
    def __init__(self, request, current_tab):        
        Controller.__init__(self, request)        
        self.tpl_vars = {'current_tab' : current_tab}

class CreateUserController(Controller):
    '''the request for creating a new user'''
    def __init__(self, request):
        Controller.__init__(self, request)
        
    def create_user(self):
        from django.contrib.auth import authenticate, login
        from django.contrib.auth.models import User        
        from django.shortcuts import render_to_response
        from django.template import RequestContext
        from pickup_finder.http import Http

        if self.request.method == 'POST':
            form = UserForm(self.request.POST)
    
            if form.is_valid():
                name = '%s:%s' % (form.cleaned_data['name'], form.cleaned_data['fb_id'])
                password = form.cleaned_data['name']
                
                #if the user already exists, log them in, o/w create them         
                user = authenticate(username=name, password=password)
                if user is not None:
                    login(self.request, user)
                else:        
                    user = User.objects.create_user(name, '', password)
                    user.save()
                    user = authenticate(username=name, password=password)
                    login(self.request, user)
                    
                return Http.redirect('pickup_finder.views.dashboard')
        else:
            form = UserForm()
        
        context = RequestContext(self.request, {'form' : form, 'facebook_id' : APIKeys.FACEBOOK_DEV})
        return render_to_response("index.html", context)             

###PORTAL CONTROLLERS###
class DashboardController(PortalController):
    def __init__(self, request):        
        PortalController.__init__(self, request, 'dashboard')    
        self.games = Game.objects.filter(creator=self.request.user)        
        self.player_games = PlayerGame.objects.filter(game__in=self.games)
        self.players = [pg.player for pg in self.player_games]

    def dashboard(self):      
        self.tpl_vars['google_key'] = APIKeys.GOOGLE    
        self.tpl_vars['games_json'] = serializers.serialize("json", self.games, fields=('latitude','longitude'))
        self.tpl_vars['player_game_json'] = serializers.serialize("json", self.player_games)
        self.tpl_vars['players_json'] = serializers.serialize("json", self.players)
        return self.tpl_vars
    
class CreateGameController(PortalController):
    def __init__(self, request):
        PortalController.__init__(self, request, 'create-game')
        
    def create_game(self):
        from geopy.geocoders.googlev3 import GoogleV3
        import datetime
        
        if self.request.method == "POST":
            form = GameForm(self.request.POST)       
            google = GoogleV3()
            
            if form.is_valid():
                location = form.cleaned_data['location']
                place, (lat, lng) = google.geocode(location)
                public = form.cleaned_data['public']
                player_cap = form.cleaned_data['player_cap'] if public else None
                start = form.cleaned_data['start']
                player_names = form.cleaned_data['player_names']
                player_ids = form.cleaned_data['player_ids']
                
                split_names = player_names.split(',')[1:] #the names and ids start with a , so the first element is a blank el
                split_ids = player_ids.split(',')[1:]

                #create the model instances
                game = Game(creator=self.request.user, latitude=lat, longitude=lng, normalized_location=location, public=public,
                            person_cap=player_cap, starts_at=datetime.datetime.now())
                game.save()
                for index,name in enumerate(split_names):                    
                    (player, created) = Player.objects.get_or_create(name=name, fb_id=split_ids[index])                                 
                    player_game = PlayerGame(player=player, game=game, chance_attending=ChanceAttendingConstants.NOT_RESPONDED[0])
                    player_game.save()                    
        else:
            form = GameForm()
            
        self.tpl_vars['form'] = form
        self.tpl_vars['facebook_id'] = APIKeys.FACEBOOK_DEV
        return self.tpl_vars

class ViewGamesController(PortalController):
    def __init__(self, request):
        PortalController.__init__(self, request, 'view-games')

    def view_games(self):
        return self.tpl_vars


class HelpController(PortalController):
    def __init__(self, request):
        PortalController.__init__(self, request, 'help')

    def help(self):        
        return self.tpl_vars
