# coding:utf-8
# Author:kaidee

from django.conf.urls import patterns, include, url
# from django.contrib.auth.views import login, logout

from django.conf import settings
# from django.conf.urls.static import static

from todos.views import *
from django.contrib import admin
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	('^$', 'todos.views.dashboard'),
    ('^base/$', base),
	('^test/$', test),
	url(r'^todo/', include('todos.urls')),    
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('trips.urls')),
    url(r'^', include('photos.urls')),
    url(r'^accounts/', include('profiles.urls')),
    # (r'^photologue/', include('photologue.urls')),
    # (r'^accounts/login/$', login),
    # (r'^accounts/logout/$', logout),
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