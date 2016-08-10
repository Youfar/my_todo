from django.shortcuts import render
from django.http import HttpResponse
from todo.models import Todo
# Create your views here.

def home(request):
	post_list = Todo.objects.all()
	return render(request, 'home.html', {'post_list' : post_list})
	#return HttpResponse("Hello World, Django")

#def detail(request, my_args):
#	post = Todo.objects.all()[int(my_args)]
#	str_content = ("todo = %s, priority = %s" % (post.todo, post.priority))
#	return HttpResponse(str_content)
