# coding:utf-8
# Author:kaidee

from django.shortcuts import render_to_response
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from trips.models import Post, Plan
from trips.forms import PostForm, PlanForm
from django import forms

ITEMS_PER_PAGE = 5

@login_required
def archive(request):
	posts = Post.objects.filter(owner=request.user)

	paginator = Paginator(posts, ITEMS_PER_PAGE)
	try:
		page = int(request.GET.get('page', '1'))
	except ValueError:
		page = 1
	try:
		contacts = paginator.page(page)
	except (EmptyPage, InvalidPage):
		contacts = paginator.page(paginator.num_pages)

	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			newpost = Post(title=form.cleaned_data['title'],
				content=form.cleaned_data['content'],
				owner=request.user,
				)
			newpost.save()
			# return HttpResponse(newpost.id)
			return HttpResponseRedirect("/archive/" + str(newpost.id) +"/")

		else:
			raise Http404
	else:
		form = PostForm()

	return render_to_response('archive.html', {
		'posts': posts, 'contacts': contacts, 'form': form
		}, context_instance=RequestContext(request)
		)

def archive_detail(request, id):
	archive_instance = Post.objects.get(id=id)

	return render_to_response("archive_detail.html",{
		"archive_instance": archive_instance
		})

def archive_edit(request, id):
	archive_instance = Post.objects.get(id=id)
	form = PostForm(request.POST or None, initial={'title':archive_instance.title,
		'content':archive_instance.content })
	if form.is_valid():
		newpost = Post(title=form.cleaned_data['title'],
				content=form.cleaned_data['content'],
				owner=request.user,
				)
		newpost.save()
		return HttpResponseRedirect("/archive/" + str(newpost.id) +"/")
	return render_to_response("archive_edit.html",{
		"form": form
		}, context_instance=RequestContext(request)
		)

def archive_delete(request, id):
	archive_instance = Post.objects.get(id=id)
	try:
		Post.objects.get(id=id).delete()
	except :
		pass

	return HttpResponseRedirect("/archive/")


@login_required
def plan(request):
	plans = Plan.objects.filter(owner=request.user)

	paginator = Paginator(plans, ITEMS_PER_PAGE)
	try:
		page = int(request.GET.get('page', '1'))
	except ValueError:
		page = 1
	try:
		contacts = paginator.page(page)
	except (EmptyPage, InvalidPage):
		contacts = paginator.page(paginator.num_pages)

	if request.method == 'POST':
		form = (request.POST.get('content', ''))
		if form:
			newplan = Plan(title='',
				content=form,
				owner=request.user,
				)
			newplan.save()
			# return HttpResponse(newpost.id)
			return HttpResponseRedirect("/plan/" + str(newplan.id) +"/")
	else:
		pass
		# form = forms.CharField(widget=forms.Textarea(attrs={'placeholder': '内容'}), required=True)

	return render_to_response('plan.html', {
		'plans': plans, 'contacts': contacts,
		}, context_instance=RequestContext(request)
		)

def plan_detail(request, id):
	plan_instance = Plan.objects.get(id=id)

	return render_to_response("plan_detail.html",{
		"plan_instance": plan_instance
		})

def plan_edit(request, id):
	plan_instance = Plan.objects.get(id=id)
	form = PlanForm(request.POST or None, initial={'content':plan_instance.content })
	if form.is_valid():
		newpost = Plan(
				content=form.cleaned_data['content'],
				owner=request.user,
				)
		newpost.save()
		return HttpResponseRedirect("/plan/" + str(newpost.id) +"/")
	return render_to_response("plan_edit.html",{
		"form": form
		}, context_instance=RequestContext(request)
		)

def plan_delete(request, id):
	plan_instance = Plan.objects.get(id=id)
	try:
		Plan.objects.get(id=id).delete()
	except :
		pass

	return HttpResponseRedirect("/plan/")