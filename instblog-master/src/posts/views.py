#Views handles the request and returns the response
# for shareable links
from django.contrib import messages #flash the successful msg
from django.http import HttpResponse, HttpResponseRedirect ,Http404 # HttpResponseRedirect:it redirects to the detail page after updating or creating a post
from django.shortcuts import render, get_object_or_404 , redirect 
from .models import Post
from .forms import *
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render
from django.shortcuts import render,redirect #login page#redirect = to redirect user to any specified page after login
from django.contrib.auth import authenticate,login #login page#authenticate:to check the entered fields with existing ones in db
from django.views.generic import View#login page

from django.contrib.auth import logout
from django.contrib import messages


# Create your views here.

def post_create(request):
	if not request.user.is_staff or not request.user.is_superuser: #imp
		raise Http404


	form =PostForm(request.POST or None, request.FILES or None) # request.FILES or None:for images
	if form.is_valid():
		instance = form.save(commit = False)
		instance.user = request.user
		instance.save()
		#message success
		
		return HttpResponseRedirect(instance.get_absolute_url()) #redirects to detail page
	context={
		"form": form,
	}
	return render(request, "post_form.html", context) 

def post_detail(request,slug=None): #in url.py it is taking two arguments request and id hence here also we have to pass two
	instance = get_object_or_404(Post, slug =slug)
	
	context = {
			"instance":instance,
			"title": instance.title,    #inside context we declare variables which can be used in html files
			
	}



	return render(request,"post_detail.html",context)

def post_list(request):
	queryset_list = Post.objects.all().order_by("-timestamp") # order_by("-timestamp") : to order posts in increasing timestamp
	if request.user.is_staff or request.user.is_superuser:
		queryset_list = Post.objects.all().order_by("-timestamp")
	query = request.GET.get("q")
	if query:
		queryset_list = queryset_list.filter(
			Q(title__icontains=query) |
			Q(content__icontains=query)
			).distinct()
	paginator = Paginator(queryset_list, 1000) # Show 25 contacts per page
	page_request_var ="page"
	page = request.GET.get("page_request_var")


	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
	# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
	# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)
	context = {
		"title":"Instblog",
		"object_list": queryset,
		"page_request_var" : page_request_var,
	}
	return render(request, "post_list.html",context)




    

    
def post_update(request,slug = None):
	#if not request.user.is_staff or not request.user.is_superuser:
		#raise Http404
	instance = get_object_or_404(Post, slug =slug)
	form =PostForm(request.POST or None,request.FILES or None,instance = instance )
	if form.is_valid():
		instance = form.save(commit = False)
		instance.save()
		# message success
		
		return HttpResponseRedirect(instance.get_absolute_url()) #redirects to detail page

	context = {
			"instance":instance,
			"title": instance.title,   
			 #inside context we declare variables which can be used in html files
			"form":form,
	}

	return render(request,"post_form.html",context)



def post_delete(request, slug=None):

	#if not request.user.is_staff or not request.user.is_superuser:
		#raise Http404
	instance = get_object_or_404(Post, slug=slug)
	instance.delete()
	messages.success(request, "Succesfully deleted")
	return redirect("posts:list", )


	



