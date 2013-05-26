from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from todos.models import Todo, get_objects
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt

def base(request):
	return render_to_response('base.html')

@login_required
def dashboard(request):
	if request.is_ajax():
		ctx = dict()
		id = request.GET.get("id")
		print 'id:',id
		todo = get_object_or_404(Todo, id=int(id))
		# print todo
		todo.is_done = True
		todo.save()
		
		# response['Content-Type']="text/javascript"
		mydata = '<li>' + todo.content + '</li>'
		# response.write(mydata)
		response=HttpResponse(mydata)
		print mydata
		response['Cache-Control'] = 'no-cache'
		return response
	else:
		user = request.user
		todos_1 = get_objects(user=user,is_done=False, priority=1)
		todos_2 = get_objects(user=user,is_done=False, priority=2)
		todos_3 = get_objects(user=user,is_done=False, priority=3)
		todos_4 = get_objects(user=user,is_done=False, priority=4)
	
		dones = get_objects(user=user, is_done=True, priority=0)
		 
		return render_to_response('todolist.html', locals(),
			context_instance=RequestContext(request))

# @login_required
def test(request):
	return render_to_response('test.html',{'hh':request.path},context_instance=RequestContext(request))

def todo_remove(request):
	pass

@login_required
@csrf_exempt
def todo_add(request):
	priority=int(request.POST.get("priority",''))
	if priority in [1, 2, 3, 4]:
		content=request.POST.get("content",'')
		user = request.user
		print "user:",user,"content:",content,"priority:",priority
		ret = 0
		if user and content:
			todo = Todo(content=content, owner=user, priority=priority)
			todo.save()
			ret = 1
		else:
			ret = 2
		response=HttpResponse()
		# response['Content-Type']="text/javascript"
		response.write(ret)
		response['Cache-Control'] = 'no-cache'
		return response
	else:
		pass

@login_required
def todo_del(request):
	id = request.GET.get("id")
	ret = 0
	obj = get_object_or_404(Todo, id=int(id))
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