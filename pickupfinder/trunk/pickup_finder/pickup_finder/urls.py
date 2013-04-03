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

#MOBILE
urlpatterns += patterns('pickup_finder.views',
    url(r'^mobile/view/$', 'mobile_view_games'),
    url(r'^mobile/view/(?P<game>\d+)/details/$', 'mobile_game_details'),
    url(r'^mobile/view/(?P<game>\d+)/details/rsvp/$', 'mobile_game_rsvp'),
    url(r'^mobile/view/(?P<game>\d+)/details/rsvp/thanks/$', 'mobile_game_rsvp_thanks'),
    url(r'^mobile/create/$', 'mobile_create_game'),
)

#ADMIN
urlpatterns += patterns('pickup_finder.views',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
