from django.shortcuts import render
from rango.models import Category
from rango.models import Page
# Create your views here.
from django.http import HttpResponse

def index(request):
	category_list = Category.objects.order_by('-likes')[:5]
	context_dict = {'boldmessage':"i am bold font from the context",'categories':category_list}
	#return HttpResponse("Rango says: Hello world! <br/> <a href='/rango/about'>About</a>")
	return render(request,'rango/index.html',context_dict)
	pass

def about(request):
    return HttpResponse("Rango says here is the about page<br/> <a href='/rango/'>index</a>")
    pass

def category(request,category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
        pass
    except Category.DoesNotExist:
        pass
    return render(request,'rango/category.html',context_dict)