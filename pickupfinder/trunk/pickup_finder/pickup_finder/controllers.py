from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext
from pickup_finder.forms import *
from pickup_finder.constants import *
from pickup_finder.models import *
from pickup_finder.components import *

class Controller():
    def __init__(self, request):
        self.request = request

class AjaxController(Controller):
    def __init__(self, request):
        Controller.__init__(self, request)
        
class PortalController(Controller):
    def __init__(self, request, current_tab):        
        Controller.__init__(self, request)        
        self.tpl_vars = {'current_tab' : current_tab, 'facebook_id' : APIKeys.FACEBOOK_PROD}

class CreateUserController(Controller):
    '''the request for creating a new user'''
    def __init__(self, request):
        Controller.__init__(self, request)
        
    def create_user(self):
        from django.contrib.auth import authenticate, login
        from django.contrib.auth.models import User        
        from pickup_finder.http import Http

        if self.request.method == 'POST':
            form = UserForm(self.request.POST)
    
            if form.is_valid():
                name = form.cleaned_data['fb_id']
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
        
        context = RequestContext(self.request, {'form' : form, 'facebook_id' : APIKeys.FACEBOOK_PROD})
        return render_to_response("index.html", context)             

###PORTAL CONTROLLERS###
class DashboardController(PortalController):
    def __init__(self, request):        
        PortalController.__init__(self, request, 'dashboard')        
        self.lineup_component = GameLineup(request)

        self.tpl_vars.update(self.lineup_component.tpl_vars())
        self.tpl_vars['games'] = self.lineup_component.games

    def dashboard(self):      
        context = RequestContext(self.request, self.tpl_vars)
        return render_to_response("portal/dashboard.html", context)
    
    
class CreateGameController(PortalController):
    def __init__(self, request):
        PortalController.__init__(self, request, 'create-game')
        
    def create_game(self):
        from geopy.geocoders.googlev3 import GoogleV3
        from decimal import Decimal
        import datetime               
        
        if self.request.method == "POST":
            form = GameForm(self.request.POST)       
            google = GoogleV3()
            
            if form.is_valid():
                location = form.cleaned_data['location']
                place, (lat, lng) = list(google.geocode(location, exactly_one=False))[0] #go back and fix
                public = form.cleaned_data['public']
                player_cap = form.cleaned_data['player_cap'] if public else None
                start = datetime.datetime.strptime("%s %s" % (form.cleaned_data['start_date'], form.cleaned_data['start_time']), 
                                                   FormattingConstants.DATE_FORMAT)                
                player_names = form.cleaned_data['player_names']
                player_ids = form.cleaned_data['player_ids']
                
                split_names = player_names.split(',')[1:] #the names and ids start with a , so the first element is a blank el
                split_ids = player_ids.split(',')[1:]

                #create the model instances
                game = Game(creator=self.request.user, latitude=Decimal(str(lat)), longitude=Decimal(str(lng)), 
                            normalized_location=location, public=public, person_cap=player_cap, starts_at=start)
                game.save()
                for index,name in enumerate(split_names):                    
                    (player, created) = Player.objects.get_or_create(name=name, fb_id=split_ids[index])                                 
                    player_game = PlayerGame(player=player, game=game, chance_attending=ChanceAttendingConstants.NOT_RESPONDED[0])
                    player_game.save()                    
                return HttpResponseRedirect('%s?created=True&game=%s'%(reverse('pickup_finder.views.create_game'), int(game.id)))
        else:
            self.tpl_vars['created'] = self.request.GET.get('created', None)
            self.tpl_vars['rsvp_link'] = Game.for_id(self.request.GET.get('game', None)).rsvp_link if self.tpl_vars['created'] else None
            form = GameForm()
        
        self.tpl_vars['form'] = form
        context = RequestContext(self.request, self.tpl_vars)
        return render_to_response("portal/create_game.html", context)        

class ViewGamesController(PortalController):
    def __init__(self, request):
        PortalController.__init__(self, request, 'view-games')
        self.lineup_component = GameLineup(request)

        self.tpl_vars.update(self.lineup_component.tpl_vars())
        self.tpl_vars['games'] = Game.games_by_creator(self.request.user)

    def view_games(self):        
        context = RequestContext(self.request, self.tpl_vars)
        return render_to_response("portal/view_games.html", context)        


class HelpController(PortalController):
    def __init__(self, request):
        PortalController.__init__(self, request, 'help')

    def help(self):
        context = RequestContext(self.request, self.tpl_vars)
        return render_to_response("portal/help.html", context)


class ExploreController(PortalController):
    def __init__(self, request):
        PortalController.__init__(self, request, 'explore')

        self.tpl_vars['games'] = Game.objects.filter(public=True).all()

    def explore(self):        
        context = RequestContext(self.request, self.tpl_vars)        
        return render_to_response("portal/explore.html", context)
    
    
class GameRsvpController(PortalController):
    def __init__(self, request, game):
        PortalController.__init__(self, request, 'rsvp')
        self.game = game

    def rsvp(self):
        if self.request.method == "POST":
            form = GameRsvpForm(self.game, self.request.POST)
            if form.is_valid():
                player = Player.for_fb_id(form.cleaned_data['player'])
                player_name = form.cleaned_data['player_name']
                rsvp_status = form.cleaned_data['rsvp_status']                
                
                #if the user is not a FB friend and its a public game, create a new player out of the given player_name
                if player_name:
                    player = Player(name=player_name)
                    player.save()
                    pg = PlayerGame(player=player, game=self.game, chance_attending=rsvp_status)
                    pg.save()
                else:
                    player_game = PlayerGame.objects.filter(player=player).get(game=self.game)
                    player_game.chance_attending = rsvp_status
                    player_game.save()
                    
                return HttpResponseRedirect(reverse('pickup_finder.views.game_rsvp_thanks', args=(int(self.game.id),)))
        else:
            form = GameRsvpForm(self.game)  
            
        self.tpl_vars.update({'game' : self.game, 'form' : form})
        context = RequestContext(self.request, self.tpl_vars)
        return render_to_response("public/rsvp_game.html", context)        
