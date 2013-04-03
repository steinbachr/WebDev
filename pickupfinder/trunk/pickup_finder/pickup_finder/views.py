from django.shortcuts import render_to_response
from django.template import RequestContext
from pickup_finder.controllers import *


def home(request):
    controller = CreateUserController(request)    
    return controller.create_user() #because a redirect is required, we break the normal pattern here

##PORTALS
def dashboard(request):
    controller = DashboardController(request)    
    return controller.dashboard()

def create_game(request):
    controller = CreateGameController(request)  
    return controller.create_game()        

def view_games(request):
    controller = ViewGamesController(request)
    return controller.view_games()    

def help(request):
    controller = HelpController(request)    
    return controller.help()

def explore(request):
    controller = ExploreController(request)    
    return controller.explore()

def game_rsvp(request, game=None):
    controller = GameRsvpController(request, Game.for_id(game))
    return controller.rsvp()

def game_rsvp_thanks(request, game=None):
    controller = GameRsvpThanksController(request, Game.for_id(game))
    return controller.render()

##MOBILE
def mobile_view_games(request):
    controller = MobileViewGamesController(request)
    return controller.render()

def mobile_create_game(request):
    controller = CreateGameController(request, tpl_file='mobile/create.html')
    return controller.create_game()

def mobile_game_details(request, game=None):
    controller = MobileGameDetailsController(request, Game.for_id(game))
    return controller.render()

def mobile_game_rsvp(request, game=None):
    controller = GameRsvpController(request, Game.for_id(game), base_tpl='mobile/base.html')
    return controller.rsvp()

def mobile_game_rsvp_thanks(request, game=None):
    controller = GameRsvpThanksController(request, Game.for_id(game), base_tpl='mobile/base.html')
    return controller.render()
    



    
