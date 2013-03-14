from pickup_finder.forms import UserForm

class Controller():
    def __init__(self, request, tpl_vars={}):
        self.request = request
        self.tpl_vars = tpl_vars

class AjaxController(Controller):
    def __init__(self, request):
        Controller.__init__(self, request)
        
class PortalController(Controller):
    def __init(self, request, content=None):
        Controller.__init__(self, request)
        self.content = content
        

class CreateUserController(Controller):
    '''the request for creating a new user'''
    def __init__(self, request):
        Controller.__init__(self, request)
        
    def create_user(self):
        from django.contrib.auth import authenticate, login
        from django.contrib.auth.models import User                
        
        form = UserForm(self.request.POST)

        if form.is_valid():
            #if the user already exists, log them in, o/w create them         
            user = authenticate(username='%s:%s' % (form.cleaned_data['name'], form.cleaned_data['fb_id']), password=form.cleaned_data['name'])
            if user is not None:
                login(self.request, user)
            else:        
                user = User.objects.create_user('%s:%s' % (form.cleaned_data['name'], form.cleaned_data['fb_id']), '', form.cleaned_data['name'])
                user.save()
                login(self.request, user)
