from django.shortcuts import render
from rango.models import Category,Page
from rango.forms import CategoryForm,PageForm,UserForm,UserProfileForm
from django.contrib.auth.decorators import login_required
# from rango.models import Page
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
import pdb;
def index(request):
	category_list = Category.objects.order_by('-likes')[:10]
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
    # pdb.set_trace()
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
def register(request):
    registered = False
    if request.method == 'POST':
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            profile=profile_form.save(commit=False)
            profile.user=user
            if 'picture' in request.FILES:
                profile.picture=request.FILES['picture']
            profile.save()
            registered=True
        else:
            print user_form.errors,profile_form.errors
        pass
    else:
        user_form=UserForm()
        profile_form=UserProfileForm()
    return render(request,'rango/register.html',
        {'user_form':user_form,'profile_form':profile_form,'registered':registered})
    pass
def user_login(request):
    if request.method=='POST':
        username =request.POST.get('username')
        password =request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect('/rango')
            else:
                return HttpResponse("Your Rango account is disable.")
        else:
            print "Invalid login details:{0},{1}".format(username,password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request,'rango/login.html',{})
@login_required
def restricted(request):
    return HttpResponse("Since you're logged in,you can see this text!")
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/rango/')
        
