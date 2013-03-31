# coding:utf-8
# Author:kaidee

from django.shortcuts import get_object_or_404, render_to_response
from django.core.paginator import QuerySetPaginator, InvalidPage
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.core.files.uploadedfile import SimpleUploadedFile
from photos.models import Gallery, Photo
from photos.forms import PhotoForm
import Image
import ImageFile 

def gallery_index(request):
	galleries = Gallery.objects.all()[:6]

	return render_to_response("gallery_index.html", {
        "galleries": galleries,
        }, context_instance=RequestContext(request)
        )

@login_required
def upload_photo(request):
	if request.method == 'POST':
		user = request.user
		form = PhotoForm(request.POST, request.FILES)
		if form.is_valid():
			# newfile = Photo(title=form.cleaned_data['title'],
			# 	description=form.cleaned_data['description'],
			# 	owner=user,
			# 	# original=form.cleaned_data['original'],
			# 	)
			# img = request.FILES["original"]
			# file_data = {'original': SimpleUploadedFile(img.name, img.read())}
			# parser = ImageFile.Parser()
			# for chunk in img.chunks():
			# 	parser.feed(chunk)
			# imge = parser.close()
			# imge.save(img.name, img)
			# s = PhotoForm(original=img)
			# s.save()
			# newfile.save()
			# form['owner'] = user
			form.save()
			# f = PhotoForm(newfile, file_data)
			# f.save()
			return HttpResponseRedirect("/photos/")
		# else:
			# return HttpResponse("提交表格有问题，请重新填写。")
		# else:
		# 	raise Http404
	else:
		form = PhotoForm()
	return render_to_response("photo_upload.html", {
        "form": form,
        }, context_instance=RequestContext(request)
        )