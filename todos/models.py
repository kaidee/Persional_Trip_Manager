# coding: utf-8
from django.db import models
from django.contrib import admin

PRIORITY_CHOICES = [(1, '重要且紧急'), (2, '重要不紧急'), (3, '紧急不重要'), (4, '不重要不紧急')]
# PRIORITY_CHOICES = [(1, 'aa'), (2, 'bb'), (3, 'cc'), (4, 'dd')]

class Todo(models.Model):
	"""docstring for Todo"""
	content = models.CharField(max_length=100)
	is_done = models.BooleanField(default=False)
	owner = models.ForeignKey('auth.User')
	priority = models.IntegerField(choices=PRIORITY_CHOICES, default=1)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return u'%s %s' % (self.content, self.owner)

	class Meta:
		ordering = ['priority',]

admin.site.register(Todo)

def get_objects(user, is_done, priority):
	if priority:
		return Todo.objects.filter(owner=user).filter(is_done=False).filter(priority=priority)
	else:
		return Todo.objects.filter(owner=user).filter(is_done=True)