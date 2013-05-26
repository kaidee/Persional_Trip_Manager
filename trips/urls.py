#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import *
# from trips.views import *

urlpatterns = patterns(('trips.views'),
	(r'^archive/$', 'archive'),
	url(r'^archive/search/$', 'archive_search', name = 'archive_search'),
	(r'^archive/(?P<id>\d+)/$', 'archive_detail'),
	(r'^archive/edit/(?P<id>\d+)/$', 'archive_edit'),
	(r'^archive/delete/(?P<id>\d+)/$', 'archive_delete'),

	url(r'^plan/$', 'plan', name = 'plan'),
	url(r'^plan/search/$', 'plan_search', name = 'plan_search'),
	url(r'^plan/(?P<id>\d+)/$', 'plan_detail', name = 'plan_detail'),
	(r'^plan/edit/(?P<id>\d+)/$', 'plan_edit'),
	(r'^plan/delete/(?P<id>\d+)/$', 'plan_delete'),
)