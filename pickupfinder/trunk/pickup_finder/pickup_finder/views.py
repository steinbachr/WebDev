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
    context = RequestContext(request, {'game' : Game.for_id(game)})
    return render_to_response("public/rsvp_thanks.html", context)



    
