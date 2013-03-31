from django.contrib import admin

from photos.models import Gallery, Photo

class GalleryAdmin(admin.ModelAdmin):
	list_display = ('title',)
	# prepopulated_fields = {'slug': ('title',)}

admin.site.register(Gallery, GalleryAdmin)

class PhotoAdmin(admin.ModelAdmin):
	# prepopulated_fields = {'slug': ('title',)}
	list_display = ('title', 'gallery', 'location')

admin.site.register(Photo, PhotoAdmin)