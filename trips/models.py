# coding:utf-8
# Author:kaidee

from django.db import models
from django.contrib import admin

class Post(models.Model):
	title = models.CharField('标题',max_length=150)
	content = models.TextField('内容')
	owner = models.ForeignKey('auth.User')
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return u'%s %s' % (self.title, self.content)

	class Meta:
		ordering = ['-created',]

class Plan(models.Model):
	title = models.CharField(max_length=150, blank=True, null=True)
	content = models.TextField()
	owner = models.ForeignKey('auth.User')
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return u'%s %s' % (self.title, self.content)

	class Meta:
		ordering = ['-created',]

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'owner', 'modified')
	class Media:
		js = ('js/tiny_mce/tiny_mce.js',
			'js/textareas.js',)

admin.site.register(Post, PostAdmin)
admin.site.register(Plan)