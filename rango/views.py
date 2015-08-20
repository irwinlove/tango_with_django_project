from django.shortcuts import render
from rango.models import Category,Page
from rango.forms import CategoryForm,PageForm
# from rango.models import Page
# Create your views here.
from django.http import HttpResponse
import pdb;
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
        context_dict['category_name_url'] = category_name_slug
    except Category.DoesNotExist:
        pass
    return render(request,'rango/category.html',context_dict)
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
        form = CategoryForm()
    context_dict = {'form':form}        
    return render(request,'rango/add_category.html',context_dict)
def add_page(request,category_name_slug):
    pdb.set_trace()
    try:
        cat = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        cat = None
    if request.method == 'POST':
        form = PageForm(request.POST)
        print category_name_slug
        print cat
        if form.is_valid():
            if cat:
                page = form.save(commit=False)
                page.category = cat
                page.views = 0
                page.save()
                return category(request,category_name_slug)
        else:
            # print form
            print form.errors
            pass
    else:
        form = PageForm()
    # print category_name_slug
    # print cat
    # print form
    context_dict = {'form':form,'category': cat,'category_name_url': category_name_slug}
    return render(request,'rango/add_page.html',context_dict)