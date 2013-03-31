from PIL import Image

from django.db import models
from django.contrib.auth.models import User
from django.db.models import permalink
from django.utils.translation import ugettext_lazy as _
from django.utils.text import truncate_words
# from django.core.files.storage import FileSystemStorage

# fs = FileSystemStorage(location='static/o/%Y-%m')

# Create your models here.
class Gallery(models.Model):
	"""
	Gallery model.
	"""
	title		= models.CharField(_('title'), max_length=100)
	description	= models.TextField(_('description'), blank=True, null=True)
	owner		= models.ForeignKey('auth.User')
	created		= models.DateTimeField(_('created'), auto_now_add=True)
	modified	= models.DateTimeField(_('modified'), auto_now=True)
	
	class Meta:
		verbose_name		= _('gallery')
		verbose_name_plural	= _('galleries')
		db_table			= 'photo_galleries'
		ordering			= ('title',)
	
	def __unicode__(self):
		return u"%s" % self.title
	
	# @permalink
	# def get_absolute_url(self):
	#   	return ('photo_gallery_title', None, {
	# 		'gallery_slug'	: self.slug
	# 	})
	
	# @permalink
	# def get_gallery_url(self):
	# 	return ('photo_gallery_detail', None, {
	# 		'gallery_slug'	: self.slug
	# 	})
	
	@property
	def latest_photo(self):
		photo = Photo.objects.filter(gallery=self).order_by('-created')[0]
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
	
	original	= models.ImageField(_('original'), upload_to='static/o/%Y-%m')
	large		= models.ImageField(_('large'), upload_to='static/l/%Y-%m',  editable=False) # Image size no greater than 480x480
	thumbnail	= models.ImageField(_('thumbnail'), upload_to='static/t/%Y-%m', editable=False) # Image size no greater than 220x220
	small		= models.ImageField(_('small'), upload_to='static/s/%Y-%m',  editable=False) # Image size no greater than 90x90
	
	created		= models.DateTimeField(_('created'), auto_now_add=True)
	modified	= models.DateTimeField(_('modified'), auto_now=True)
	
	class Meta:
		verbose_name		= _('photo')
		verbose_name_plural	= _('photos')
		db_table			= 'photos'
		ordering			= ('-modified',)
	
	def __unicode__(self):
		return u"%s" % self.title
	
	# @permalink
	# def get_absolute_url(self):
	# 	return ('photo_gallery_photo_detail', None, {
	# 		'photo_slug'	: self.slug,
	# 		'gallery_slug'	: self.gallery.slug,
	# 	})
	
	def save(self):
		LARGE_SIZE = (480, 480)
		THUMBNAIL_SIZE = (220, 220)
		SMALL_SIZE = (90, 90)
		
		# TODO: Still thinking of a good way to to this.
		# Need to convert the Photos to Large and Small thumbnails.
		
		super(Photo, self).save()
	
	# def admin_thumbnail(self):
	# 	"""
	# 	Adds a photo thumbnail to the administration interface.
	# 	"""
	# 	return u"<img src=\"%s/%s\" />" % (settings.MEDIA_URL, self.small)
	
	# admin_thumbnail.sort_description = 'Thumbnail'
	# admin_thumbnail.allow_tags = True
