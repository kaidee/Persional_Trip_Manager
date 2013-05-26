# coding:utf-8
# Author:kaidee

from PIL import Image

from django.db import models
from django.contrib.auth.models import User
from django.db.models import permalink
from django.utils.translation import ugettext_lazy as _
from django.utils.text import truncate_words

from easy_thumbnails.fields import ThumbnailerImageField

class Gallery(models.Model):
	"""
	Gallery model.
	"""
	title		= models.CharField(u'名称', max_length=100)
	description	= models.TextField(u'描述', blank=True, null=True)
	owner		= models.ForeignKey(User)
	created		= models.DateTimeField(_('created'), auto_now_add=True)
	modified	= models.DateTimeField(_('modified'), auto_now=True)
	
	class Meta:
		verbose_name		= _('gallery')
		verbose_name_plural	= _('galleries')
		db_table			= 'photo_galleries'
		ordering			= ('modified',)
	
	def __unicode__(self):
		return u"%s" % self.title
	
	@property
	def latest_photo(self):
		photo = Photo.objects.filter(gallery=self).order_by('-created')[0:8]
		return photo

	@property
	def all_photo(self):
		photo = Photo.objects.filter(gallery=self).order_by('-created')
		return photo
	
	@property
	def description_truncate(self):
		return u"%s" % truncate_words(self.description, 20)
	
	@property
	def photo_count(self):
		"""
		How many photos are in a given gallery.
		"""
		count = Photo.objects.filter(gallery=self).count()
		return u"%s" % count
	
	@property
	def date_last_photo(self):
		"""
		Date of last photo uploaded to the gallery.
		"""
		photo = Photo.objects.order_by('-created')[:0]
		return photo.created

class Photo(models.Model):
	"""
	Photo model.
	"""
	title		= models.CharField(_('title'), max_length=200, blank=True, null=True)
	location	= models.CharField(_('location'), max_length=50, blank=True, null=True)
	description	= models.TextField(_('description'), blank=True, null=True)
	gallery		= models.ForeignKey(Gallery)
	owner		= models.ForeignKey('auth.User')
	
	image	= ThumbnailerImageField(_('image'), upload_to='photos/%Y-%m')
	
	created		= models.DateTimeField(_('created'), auto_now_add=True)
	modified	= models.DateTimeField(_('modified'), auto_now=True)
	
	class Meta:
		verbose_name		= _('photo')
		verbose_name_plural	= _('photos')
		db_table			= 'photos'
		ordering			= ('-modified',)
	
	def __unicode__(self):
		return u"%s" % self.title
