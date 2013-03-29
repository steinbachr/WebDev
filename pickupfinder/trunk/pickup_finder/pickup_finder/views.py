from django.shortcuts import render_to_response
from django.template import RequestContext
from pickup_finder.controllers import *


def home(request):
    controller = CreateUserController(request)    
    return controller.create_user() #because a redirect is required, we break the normal pattern here

##PORTALS
def dashboard(request):
    controller = DashboardController(request)    
    context = RequestContext(request, controller.dashboard())
    return render_to_response("portal/dashboard.html", context)

def create_game(request):
    controller = CreateGameController(request)    
    context = RequestContext(request, controller.create_game())
    return render_to_response("portal/create_game.html", context)

def view_games(request):
    controller = ViewGamesController(request)
    context = RequestContext(request, controller.view_games())
    return render_to_response("portal/view_games.html", context)

def help(request):
    controller = HelpController(request)
    context = RequestContext(request, controller.help())
    return render_to_response("portal/help.html", context)

def game_rsvp(request, game=None):
    controller = GameRsvpController(request, Game.for_id(game))
    context = RequestContext(request, controller.rsvp())
    return render_to_response("portal/game.html", context)
    
    



    
