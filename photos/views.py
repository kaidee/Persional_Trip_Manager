# coding:utf-8
# Author:kaidee

from django.shortcuts import get_object_or_404, render_to_response
from django.core.paginator import QuerySetPaginator, InvalidPage
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.urlresolvers import reverse

from django.conf import settings
from django.utils import simplejson
from django.template import RequestContext
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404

from photos.models import Gallery, Photo
from photos.forms import PhotoForm, GalleryForm

import Image
import ImageFile

MAX_FILE_SIZE = 30000000	# 图片最大容量值
MIN_FILE_SIZE = 1000	# 图片最新容量值

#上传图片数量
MAXNUMBEROFFILES = 30

#允许的文件类型
ACCEPTED_FORMATS = (
            "image/pjpeg",
            "image/jpeg",
            "image/png",
            )

@login_required
def gallery_index(request):
	user = request.user
	galleries = Gallery.objects.filter(owner=user)

	return render_to_response("photos/gallery_index.html", {
        "galleries": galleries,
        }, context_instance=RequestContext(request)
        )

@login_required
def add_gallery(request):
	form = GalleryForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			form.save(owner=request.user)
			return HttpResponseRedirect('/photos/')
		
	return render_to_response("photos/add_gallery.html",{
		"form": form,
		}, context_instance=RequestContext(request)
		)

@login_required
def gallery_view(request, id):
	gallery_item = Gallery.objects.get(id=id)

	return render_to_response("photos/gallery_view.html",{
		"gallery_item": gallery_item,
		}, context_instance=RequestContext(request)
		)

@login_required
def upload_photo(request):
	if request.method == 'POST':
		user = request.user
		album_id = request.GET.get('album_id')
		form = PhotoForm(request.POST, request.FILES)
		if form.is_valid():
			cd = form.cleaned_data
			title = cd['title']
			description = cd['description']
			image = cd['image']
			owner = user
			gallery = get_object_or_404(Gallery, id=album_id)

			photo = Photo(title=title, description=description,
				image=image, owner=owner, gallery=gallery,
				)
			photo.save()
			return HttpResponseRedirect("/photos/")
	else:
		form = PhotoForm()
	return render_to_response("photos/photo_upload.html", {
        "form": form,
        }, context_instance=RequestContext(request)
        )

def response_mimetype(request):
    if "application/json" in request.META['HTTP_ACCEPT']:
        return "application/json"
    else:
        return "text/plain"

@login_required
@csrf_exempt
def multi_upload(request, album_id):
	if request.method == 'POST':

		owner = request.user
		print album_id
		gallery = get_object_or_404(Gallery, id=album_id)

		file = request.FILES[u'files[]']
		error = False
		#文件是否合法
		if file.size > MAX_FILE_SIZE:
			error = "maxFileSize"
		if file.size < MIN_FILE_SIZE:
			error = "minFileSize"
		if file.content_type not in ACCEPTED_FORMATS:
			error = "acceptFileTypes"
		if request.session["is_allow_upload"] == 0:
			error = "maxNumberOfFiles"
		else:
			request.session["is_allow_upload"] -= 1

		response_data = {
			"name": file.name,
			"size": file.size,
			"type": file.content_type,
			}
		if error:
			response_data["error"] = error
			response_data = simplejson.dumps([response_data])
			return HttpResponse(response_data, mimetype=response_mimetype(request))
		#保存文件
		image = Photo(
			title=file.name, description='description',
			image=file, owner=owner, gallery=gallery,
			)
		image.save()
		response_data["url"] = image.image.url
		response_data['thumbnail_url'] = image.image['thumbnail'].url
		print 'url:',image.image['thumbnail'].url
		#删除链接
		response_data["delete_url"] = "/photos/del/" + str(image.id)
		response_data["delete_type"] = "GET"
		response_data = simplejson.dumps({"files":[response_data]})

		return HttpResponse(response_data, mimetype=response_mimetype(request))

	else:
		request.session["is_allow_upload"] = MAXNUMBEROFFILES
		print request.session["is_allow_upload"]
		return render_to_response('photos/multi_upload.html',{
			"open_tv":u'{%',"close_tv": u'%}',"maxfilesize": MAX_FILE_SIZE,
			"minfilesize": MIN_FILE_SIZE,"maxnumberoffiles":MAXNUMBEROFFILES,
			}, context_instance=RequestContext(request)
			)

@login_required	
def del_image(request,image_id):
	image = get_object_or_404(Photo,id=image_id)
	print image_id
	image.delete()
	response_data = simplejson.dumps(True)
	return HttpResponse(response_data, mimetype="application/json")

def ajax_del_image(request, id=0):

	id = request.GET.get("id")
	print 'id:',id
	ret = 0
	obj = get_object_or_404(Photo, id=int(id))
	print 'obj:',obj
	if obj:
		obj.delete()
		ret = 1
		print 'ret:',ret
	else:
		ret = 2
	response=HttpResponse()
	response.write(ret)
	return response

@login_required
def manage(request, pk=0):
	user = request.user
	
	if pk:
		gallery = get_object_or_404(Gallery, pk=pk)
		if gallery.owner != request.user:
			return HttpResponse(u'您没有权限执行该操作')
		return render_to_response("photos/gallery_edit.html", {
	        "gallery": gallery,
	        }, context_instance=RequestContext(request)
	        )
	else:
		galleries = Gallery.objects.filter(owner=user)
		return render_to_response("photos/mygallery.html", {
	        "galleries": galleries,
	        }, context_instance=RequestContext(request)
	        )

@login_required
def gallery_edit(request, pk=0):
	ctx = {}
	gallery = get_object_or_404(Gallery, pk=pk)
	print 'gallery.owner:',gallery.owner
	if gallery.owner != request.user:
		return HttpResponse(u'您没有权限执行该操作')
	form = GalleryForm(instance=gallery)
	if request.method == 'POST':
		form = GalleryForm(request.POST,instance=gallery)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('manage'))
	return render_to_response("photos/add_gallery.html",{
		"form": form, 'gallery': gallery
		}, context_instance=RequestContext(request)
		)

@login_required
def gallery_del(request, pk):
	gallery = get_object_or_404(Gallery, pk=pk)
	if gallery.owner != request.user:
		return HttpResponse(u'您没有权限执行该操作')
	gallery.delete()
	
	return HttpResponseRedirect(reverse('manage'))