#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import *
# from trips.views import *

urlpatterns = patterns(('photos.views'),
	url(r'^$',
	view = 'gallery_index',
	name = 'photo_gallery_index',
	),
	(r'^upload/$', 'upload_photo'),
)