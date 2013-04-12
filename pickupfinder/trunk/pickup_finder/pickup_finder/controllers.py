from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext
from pickup_finder.forms import *
from pickup_finder.constants import *
from pickup_finder.models import *
from pickup_finder.components import *

class Controller():
    def __init__(self, request, mobile=False):
        self.request = request            
        self.mobile = mobile
        self.tpl_vars = {'facebook_id' : APIKeys.FACEBOOK_PROD}

class AjaxController(Controller):
    def __init__(self, request):
        Controller.__init__(self, request)
        
class PortalController(Controller):
    def __init__(self, request, current_tab, mobile=False):        
        Controller.__init__(self, request, mobile)       
        self.tpl_vars.update({'current_tab' : current_tab, 'notifications' : Notification.unseen_notifications(request.user)})
        
class MobileController(Controller):
    def __init__(self, request):
        Controller.__init__(self, request, mobile=True)        

class CreateUserController(Controller):
    '''the request for creating a new user'''
    def __init__(self, request, mobile=False):
        Controller.__init__(self, request)
        self.mobile = mobile
        
    def create_user(self):
        from django.contrib.auth import authenticate, login
        from django.contrib.auth.models import User                

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
        else:
            #if a mobile user goes to the non mobile site, redirect them to the mobile site
            if self.request.MOBILE and not self.mobile:
                return HttpResponseRedirect(reverse('pickup_finder.views.mobile_home'))
            form = UserForm()

        if self.request.user.is_authenticated():
            if self.mobile:
                return HttpResponseRedirect(reverse('pickup_finder.views.mobile_view_games'))
            else:
                return HttpResponseRedirect(reverse('pickup_finder.views.dashboard'))
            
        context = RequestContext(self.request, {'form' : form, 'facebook_id' : APIKeys.FACEBOOK_PROD, 'mobile' : self.mobile})
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
    def __init__(self, request, mobile=False):
        PortalController.__init__(self, request, 'create-game', mobile=mobile)    
        
    def create_game(self):
        from geopy.geocoders.googlev3 import GoogleV3, GQueryError
        from decimal import Decimal
        import datetime               
        
        if self.request.method == "POST":
            form = GameForm(self.request.POST)       
            google = GoogleV3()
            
            if form.is_valid():
                location = form.cleaned_data['location']
                game_type = form.cleaned_data['game_type']
                try:
                    place, (lat, lng) = list(google.geocode(location, exactly_one=False))[0] #go back and fix
                except GQueryError:
                    return HttpResponseRedirect('%s?created=False'%(reverse('pickup_finder.views.create_game')))
                    
                public = form.cleaned_data['public']
                player_cap = form.cleaned_data['player_cap'] if public else None
                start = form.cleaned_data['start']              
                player_names = form.cleaned_data['player_names']
                player_ids = form.cleaned_data['player_ids']
                
                split_names = player_names.split(',')[1:] #the names and ids start with a , so the first element is a blank el
                split_ids = player_ids.split(',')[1:]

                #create the model instances
                game = Game(creator=self.request.user, latitude=Decimal(str(lat)), longitude=Decimal(str(lng)), 
                            normalized_location=location, public=public, game_type=game_type, person_cap=player_cap, starts_at=start)
                game.save()
                for index,name in enumerate(split_names):                    
                    (player, created) = Player.objects.get_or_create(name=name, fb_id=split_ids[index])                                 
                    player_game = PlayerGame(player=player, game=game, chance_attending=ChanceAttendingConstants.NOT_RESPONDED[0])
                    player_game.save()

                #create the notification only if the game being created is public
                if game.public:                
                    notif_controller = NotificationController(game)
                    notif_controller.create_notification(NotificationTypeConstants.GAME_CREATED)
                
                if self.mobile:
                    return HttpResponseRedirect('%s?created=True&game=%s'%(reverse('pickup_finder.views.mobile_create_game'), int(game.id)))
                else:
                    return HttpResponseRedirect('%s?created=True&game=%s'%(reverse('pickup_finder.views.create_game'), int(game.id)))
                    
        else:
            self.tpl_vars['created'] = self.request.GET.get('created', None)            
            self.tpl_vars['game'] = Game.for_id(self.request.GET.get('game', None)) if self.tpl_vars['created'] == 'True' else None
            form = GameForm()
        
        self.tpl_vars['form'] = form
        self.tpl_vars['form_errors'] = form.non_field_errors()
        context = RequestContext(self.request, self.tpl_vars)
        
        tpl_file =  "mobile/create.html"  if self.mobile else "portal/create_game.html"
        return render_to_response(tpl_file, context)        

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

        self.tpl_vars['games'] = Game.public_games().all()

    def explore(self):        
        context = RequestContext(self.request, self.tpl_vars)        
        return render_to_response("portal/explore.html", context)        
        
    
class GameRsvpController(Controller):
    def __init__(self, request, game, mobile=False):
        Controller.__init__(self, request, mobile=mobile)
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
                    player_game = PlayerGame(player=player, game=self.game, chance_attending=rsvp_status)
                    player_game.save()
                else:
                    player_game = PlayerGame.objects.filter(player=player).get(game=self.game)
                    player_game.chance_attending = rsvp_status
                    player_game.save()
                    
                #create the notification
                notif_controller = NotificationController(self.game, player_game)
                notif_controller.create_notification(NotificationTypeConstants.PLAYER_JOINED)
                    
                if self.mobile:
                    return HttpResponseRedirect(reverse('pickup_finder.views.mobile_game_rsvp_thanks', args=(int(self.game.id),)))                    
                else:
                    return HttpResponseRedirect(reverse('pickup_finder.views.game_rsvp_thanks', args=(int(self.game.id),)))
                    
        else:
            form = GameRsvpForm(self.game)  
            
        self.tpl_vars.update({'game' : self.game, 'form' : form, 'mobile_or_public' : 'public/base.html' if not self.mobile else 'mobile/base.html', 'back_button' : False})
        context = RequestContext(self.request, self.tpl_vars)
        return render_to_response("public/rsvp_game.html", context)     
    
class GameRsvpThanksController(Controller):
    def __init__(self, request, game, mobile=False):
        Controller.__init__(self, request, mobile=mobile)
        self.game = game
        self.tpl_file = "mobile/rsvp_thanks.html" if self.mobile else "public/rsvp_thanks.html"
    
    def render(self):
        self.tpl_vars.update({'game' : self.game})
        context = RequestContext(self.request, self.tpl_vars)
        return render_to_response(self.tpl_file, context)
    
        
        
####MOBILE CONTROLLERS####
class MobileViewGamesController(MobileController):
    def __init__(self, request):
        MobileController.__init__(self, request)
        
        #we bucket the games by their game type
        game_dict = {}
        for game in Game.public_games().all():
            if game.verbose_game_type not in game_dict:
                game_dict[game.verbose_game_type] = [game]
            else:
                game_dict[game.verbose_game_type].append(game)

        self.tpl_vars.update({'games' : game_dict})
        
    def render(self):
        context = RequestContext(self.request, self.tpl_vars)        
        return render_to_response("mobile/view.html", context)
    
class MobileGameDetailsController(MobileController):
    def __init__(self, request, game):
        MobileController.__init__(self, request)
        self.game = game
        self.tpl_vars['game'] = self.game

    def render(self):
        context = RequestContext(self.request, self.tpl_vars)
        return render_to_response("mobile/game_details.html", context)    
    
    
    
####OTHER CONTROLLERS####
class NotificationController():
    def __init__(self, game, player_game=None):
        self.game = game
        self.player_game = player_game
        
            
    def create_notification(self, notification_type):
        notification = Notification(game=self.game, player_game=self.player_game, type=notification_type[0], seen=False)
        notification.save()
