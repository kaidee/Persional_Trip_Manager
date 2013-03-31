#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import *
# from trips.views import *

urlpatterns = patterns(('trips.views'),
	(r'^archive/$', 'archive'),
	(r'^archive/(?P<id>\d+)/$', 'archive_detail'),
	(r'^archive/edit/(?P<id>\d+)/$', 'archive_edit'),
	(r'^archive/delete/(?P<id>\d+)/$', 'archive_delete'),

	(r'^plan/$', 'plan'),
	(r'^plan/(?P<id>\d+)/$', 'plan_detail'),
	(r'^plan/edit/(?P<id>\d+)/$', 'plan_edit'),
	(r'^plan/delete/(?P<id>\d+)/$', 'plan_delete'),
)