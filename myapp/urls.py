# coding:utf-8
# Author:kaidee

from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.conf import settings

from todos.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	('^$', 'todos.views.dashboard'),
    ('^base/$', base),
    ('^test/$', test),
	url(r'^maps/$', direct_to_template, {'template':'GoogleMaps.html'}),
	url(r'^todo/', include('todos.urls')),    
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('trips.urls')),
    url(r'^', include('photos.urls')),
    url(r'^accounts/', include('profiles.urls')),
    url(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/static/images/favicon.ico'}),
)

# if settings.DEBUG:
#     urlpatterns += patterns('',
#         url(r'^media/(?P<path>.*)$', 'django_dynamic_media_serve.serve', {  #这里有编码问题，无法获取中文名图片
#             'document_root': settings.MEDIA_ROOT,
#         }),
#    )

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )