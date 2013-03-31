from django.conf.urls import patterns, include, url
# from django.contrib.auth.views import login, logout

from todos.views import *
from django.contrib import admin
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	('^$', test),
	('^base/$', base),
	('^todos/$', dashboard),    
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('trips.urls')),
    url(r'^photos/', include('photos.urls')),
    url(r'^accounts/', include('userena.urls')),
    # (r'^photologue/', include('photologue.urls')),
    # (r'^accounts/login/$', login),
    # (r'^accounts/logout/$', logout),
)
