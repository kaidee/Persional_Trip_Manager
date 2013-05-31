#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import *

urlpatterns = patterns(('trips.views'),
	url(r'^archive/$', 'archive', name = 'archive'),
	url(r'^archive/search/$', 'archive_search', name = 'archive_search'),
	url(r'^archive/(?P<id>\d+)/$', 'archive_detail', name = 'archive_detail'),
	url(r'^archive/edit/(?P<id>\d+)/$', 'archive_edit'),
	url(r'^archive/delete/(?P<id>\d+)/$', 'archive_delete'),

	url(r'^plan/$', 'plan', name = 'plan'),
	url(r'^plan/search/$', 'plan_search', name = 'plan_search'),
	url(r'^plan/(?P<id>\d+)/$', 'plan_detail', name = 'plan_detail'),
	url(r'^plan/edit/(?P<id>\d+)/$', 'plan_edit'),
	url(r'^plan/delete/(?P<id>\d+)/$', 'plan_delete'),
)