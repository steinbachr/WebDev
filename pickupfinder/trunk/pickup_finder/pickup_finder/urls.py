from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from django.contrib import admin
admin.autodiscover()

#VIEWS
urlpatterns = patterns('pickup_finder.views',    
    url(r'^$', 'home'), 
    url(r'^portal/dashboard/$', 'dashboard'),
    url(r'^portal/create-game/$', 'create_game'),
    url(r'^portal/view-games/$', 'view_games'),
    url(r'^portal/help/$', 'help'),
    url(r'^portal/explore/$', 'explore'),
    url(r'^game/(?P<game>\d+)/$', 'game_rsvp'),
    url(r'^game/(?P<game>\d+)/thanks/$', 'game_rsvp_thanks'),
)

#ADMIN
urlpatterns += patterns('pickup_finder.views',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
