from pickup_finder.forms import *

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
        
        context = RequestContext(self.request, {'form' : form})
        return render_to_response("index.html", context)             

###PORTAL CONTROLLERS###
class DashboardController(PortalController):
    def __init__(self, request):        
        PortalController.__init__(self, request, 'dashboard')

    def dashboard(self):         
        return self.tpl_vars
    
class CreateGameController(PortalController):
    def __init__(self, request):
        PortalController.__init__(self, request, 'create-game')
        
    def create_game(self):
        if self.request.method == "POST":
            form = GameForm(self.request.POST)
        else:
            form = GameForm()
            
        self.tpl_vars['form'] = form
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
