# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.shortcuts import render , get_object_or_404 , redirect
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse ,  HttpResponseRedirect , Http404
from django.shortcuts import render , get_object_or_404 , redirect
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from django.views.generic import RedirectView

#enkripsi html
from htmlmin.decorators import minified_response

from .models import data_saran
from .forms import SaranForm

# Create your views here.
@minified_response
def tambah_saran(request):
    print ("asu")
    if request.method == "POST":
        form = SaranForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_home')
    else:
        form = SaranForm()
    return render(request, 'saran.html', {'form': form})


# def daftar_saran(request):
#     context = {}
#     template_name = 'daftar_saran.html'
#     return render(request,template_name,context)


# Create your views here.
@minified_response
def daftar_saran (request):
	today = timezone.now().date()
	queryset_list = data_saran.objects.saran_active()

	query = request.GET.get('q')
	if query:
		queryset_list = queryset_list.filter(
			Q(title__icontains=query) |
			Q(content__icontains=query) |
			Q(user__first_name__icontains=query)|
			Q(user__last_name__icontains=query)
			).distinct()

	#<Paginator
	paginator = Paginator(queryset_list, 10) # Show 25 contacts per page
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
	    queryset = paginator.page(page)
	except PageNotAnInteger:
	    # If page is not an integer, deliver first page.
	    queryset = paginator.page(1)
	except EmptyPage:
	    # If page is out of range (e.g. 9999), deliver last page of results.
	    queryset = paginator.page(paginator.num_pages)
	#Paginator>

	context = {
		"list_saran" : queryset,
		"title" : "List",
		"page_request_var": page_request_var,
		"today" : today,
	}

	template_name = 'daftar_saran.html'
	return render(request, template_name, context)
