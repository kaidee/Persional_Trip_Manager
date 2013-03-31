from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from todos.models import Todo


# Create your views here.

def base(request):
	return render_to_response('base.html')

def dashboard(request):
	user = request.user
	if user is not None:
		
		todos_1 = Todo.objects.filter(owner=user).filter(is_done=False).filter(priority=1)
		todos_2 = Todo.objects.filter(owner=user).filter(is_done=False).filter(priority=2)
		todos_3 = Todo.objects.filter(owner=user).filter(is_done=False).filter(priority=3)
		todos_4 = Todo.objects.filter(owner=user).filter(is_done=False).filter(priority=4)
		dones = Todo.objects.filter(owner=user).filter(is_done=True)
	else:
		return HttpResponse("Please login!")
	return render_to_response('todolist.html', locals())

# @login_required
def test(request):
	return render_to_response('test.html')