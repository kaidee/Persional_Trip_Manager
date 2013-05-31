from django.contrib import admin

from photos.models import Gallery, Photo

class GalleryAdmin(admin.ModelAdmin):
	list_display = ('title',)

admin.site.register(Gallery, GalleryAdmin)

class PhotoAdmin(admin.ModelAdmin):
	list_display = ('title', 'gallery', 'location')

admin.site.register(Photo, PhotoAdmin)