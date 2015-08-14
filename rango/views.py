from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
	context_dict={'boldmessage':"i am bold font from the context"}
	#return HttpResponse("Rango says: Hello world! <br/> <a href='/rango/about'>About</a>")
	return render(request,'rango/index.html',context_dict)
	pass

def about(request):
	return HttpResponse("Rango says here is the about page<br/> <a href='/rango/'>index</a>")
	pass	