# coding:utf-8
# Author:kaidee

from django.conf.urls import *

urlpatterns = patterns(('todos.views'),
	url(r'^$', 'dashboard', name = 'dashboard'),
	url(r'^todo_add/$', 'todo_add', name = 'todo_add'),
	url(r'^todo_del/$', 'todo_del', name = 'todo_del'),
)