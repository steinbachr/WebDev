from django.shortcuts import render_to_response
from django.template import RequestContext
from pickup_finder.controllers import *
from pickup_finder.http import Http
from pickup_finder.forms import UserForm

def home(request):
    context = RequestContext(request, {'form' : UserForm()})
    #if its a post, we know that the user has clicked the signup button
    if request.method == 'POST':
        controller = CreateUserController(request)
        controller.create_user()
        return Http.redirect('pickup_finder.views.dashboard')
    
    return render_to_response("index.html", context)

def dashboard(request):
    context = RequestContext(request, {})
    return render_to_response("portal/base.html", context)
    
    



    
