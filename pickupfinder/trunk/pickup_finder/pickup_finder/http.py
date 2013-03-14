from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

class Http():
    @classmethod
    def redirect(cls, view_func):
        return HttpResponseRedirect(reverse(view_func))
