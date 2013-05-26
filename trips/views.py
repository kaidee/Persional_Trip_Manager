# coding:utf-8
# Author:kaidee

from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from trips.models import Post, Plan
from django.db.models import Q
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
		'posts': posts, 'contacts': contacts, 'form': form, 'this_path': request.path
		}, context_instance=RequestContext(request)
		)

@login_required
def archive_detail(request, id):
	archive_instance = Post.objects.get(id=id)

	return render_to_response("archive_detail.html",{
		"archive_instance": archive_instance
		})

@login_required
def archive_edit(request, id):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			title = form.cleaned_data['title']
			content = form.cleaned_data['content']
			archive = get_object_or_404(Post, id=id)
			if title:
				archive.title = title
				archive.content = content
				archive.save()
			else:
				pass
		else:
			pass
		return HttpResponseRedirect('/archive/')
	else:
		archive = get_object_or_404(Post, id=id)
		form = PostForm(initial={'title':archive.title, 'content':archive.content }, auto_id=False)
		return render_to_response("archive_edit.html",{
			"form": form
			}, context_instance=RequestContext(request)
			)

@login_required
def archive_delete(request, id):
	archive_instance = Post.objects.get(id=id)
	try:
		Post.objects.get(id=id).delete()
	except :
		pass

	return HttpResponseRedirect("/archive/")

def archive_search(request):
	s = request.GET.get('s')
	# posts = None
	if s != 'Search...' and s != '':
		print 's:',s
		# if s != None:
 		qset = (Q(title__icontains=s)|Q(content__icontains=s))
		posts = Post.objects.filter(qset, owner=request.user)
		contacts = posts
		return render_to_response('archive.html', {
			'posts': posts, 'contacts': contacts,
			}, context_instance=RequestContext(request)
			)
	else:
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
		'plans': plans, 'contacts': contacts,'this_path': request.path
		}, context_instance=RequestContext(request)
		)

@login_required
def plan_detail(request, id):
	plan_instance = Plan.objects.get(id=id)

	return render_to_response("plan_detail.html",{
		"plan_instance": plan_instance
		})

@login_required
def plan_edit(request, id):
	if request.method == 'POST':
		form = PlanForm(request.POST)
		if form.is_valid():
			content = form.cleaned_data['content']
			plan = get_object_or_404(Plan, id=id)
			if content:
				plan.content = content
				plan.save()
			else:
				pass
		else:
			pass
		return HttpResponseRedirect('/plan/')
	else:
		plan = get_object_or_404(Plan, id=id)
		form = PlanForm(initial={'content':plan.content }, auto_id=False)
		return render_to_response("plan_edit.html",{
			"form": form
			}, context_instance=RequestContext(request)
			)

@login_required
def plan_delete(request, id):
	plan_instance = Plan.objects.get(id=id)
	try:
		Plan.objects.get(id=id).delete()
	except :
		pass

	return HttpResponseRedirect("/plan/")

def plan_search(request):
	s = request.GET.get('s')
	if s != 'Search...' and s != '':
		print 's:',s
		qset = (Q(content__icontains=s))
		plans = Plan.objects.filter(qset, owner=request.user)

		paginator = Paginator(plans, ITEMS_PER_PAGE)
		try:
			page = int(request.GET.get('page', '1'))
		except ValueError:
			page = 1
		try:
			contacts = paginator.page(page)
		except (EmptyPage, InvalidPage):
			contacts = paginator.page(paginator.num_pages)

		return render_to_response('plan.html', {
			'plans': plans, 'contacts': contacts,
			}, context_instance=RequestContext(request)
			)
	else: 
		return HttpResponseRedirect("/plan/")