# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import (render, render_to_response, redirect, get_object_or_404)
from django.template import RequestContext

from django.views import generic
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse ,  HttpResponseRedirect , Http404
from django.shortcuts import render , get_object_or_404 , redirect
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from django.views.generic import RedirectView

#enkripsi html
from htmlmin.decorators import minified_response


#table
from django.shortcuts import render

# model
from .models import Post , data_kepala_sekolah , data_guru , data_tu, siswa , silabus , filex

# Create your views here.
@minified_response
def post_home(request):
	today = timezone.now().date()
	queryset_list = Post.objects.active() #.order_by("-timestamp")
	# if request.user.is_staff or request.user.is_superuser:
		# queryset_list = Post.objects.all()

	query = request.GET.get('q')
	if query:
		queryset_list = queryset_list.filter(
			Q(title__icontains=query) |
			Q(content__icontains=query) |
			Q(user__first_name__icontains=query)|
			Q(user__last_name__icontains=query)
			).distinct()

	#<Paginator
	paginator = Paginator(queryset_list, 4) # Show 25 contacts per page
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
		"object_list" : queryset,
		"title" : "List",
		"page_request_var": page_request_var,
		"today" : today,
	}

	template_name = 'index.html'
	return render(request, template_name, context)

	# context = {}
	# template_name = 'index.html'
	# return render(request,template_name,context)

@minified_response
def post_detail(request, slug=None):
	post = get_object_or_404(Post, slug=slug)

	# if post.publish > timezone.now().date():
	# 	if not request.user.is_staff or not request.user.is_superuser:
	# 		raise Http404

	# def get_client_ip():
	# 	ip = request.META.get("HTTP_X_FORWARDED_FOR", None)
	# 	if ip:
	# 		ip = ip.split(", ")[0]
	# 	else:
	# 		ip = request.META.get("REMOTE_ADDR", "")
	# 	return ip
	#
	# def tracking_hit_post():
	# 	try:
	# 		Post_Views.objects.get(post=post, ip=get_client_ip())
	# 	except ObjectDoesNotExist:
	# 		import socket
	# 		dns = str(socket.getfqdn(get_client_ip())).split('.')[-1]
	# 		try:
	# 			if str(dns) == 'localhost': #int(dns):
	# 				view = Post_Views(post=post, ip=get_client_ip())
	# 				view.save()
	# 			else: pass
	# 		except ValueError: pass
	# 	return Post_Views.objects.filter(post=post).count()

	context = {
		"post" : post,
		# "total_visitor": tracking_hit_post()
	}
	template_name = 'post_detail.html'
	return render(request,template_name,context)

	# context = {}
	# template_name = 'post_detail.html'
	# return render(request,template_name,context)



	template_name = 'index.html'
	return render(request, template_name, context)

@minified_response
def kepalasekolah(request):
	diri_kepalasekolah = data_kepala_sekolah.objects.all()
	template_name = 'kepalasekolah.html'
	context = {
	"diri_kepalasekolah" : diri_kepalasekolah
	}
	return render(request,template_name,context)

@minified_response
def dataguru(request):
	# diri_guru = get_object_or_404(data_guru) .order_by("-timestamp")
	list_diri_guru = data_guru.objects.guru_active()

	context = {
		"list_guru" : list_diri_guru,
		# "diri_guru" : diri_guru,
		# "total_visitor": tracking_hit_post()
	}
	template_name = 'dataguru.html'
	return render(request,template_name,context)

@minified_response
def datatu(request):
	list_diri_tu = data_tu.objects.tu_active()

	context = {
		"list_tu" : list_diri_tu,
	}
	template_name = 'datatu.html'
	return render(request,template_name,context)

@minified_response
def datasiswa(request):
	list_diri_siswa = siswa.objects.siswa_active()

	context = {
		"list_siswa" : list_diri_siswa,
	}
	template_name = 'datasiswa.html'
	return render(request,template_name,context)

@minified_response
def datasilabus(request):
	list_silabus = silabus.objects.silabus_active()

	context = {
	"list_silabus" : list_silabus,
	}
	template_name = 'silabus.html'
	return render(request,template_name,context)

@minified_response
def datafile(request):
	list_file = filex.objects.file_active()

	context = {
	"list_file" : list_file,
	}
	template_name = 'file.html'
	return render(request,template_name,context)


#_______________STATIC_____________________#
@minified_response
def sejarah(request):
	context = {}
	template_name = 'sejarah.html'
	return render(request,template_name,context)
@minified_response
def visi(request):
	context = {}
	template_name = 'visi.html'
	return render(request,template_name,context)
@minified_response
def struktur(request):
	context = {}
	template_name = 'struktur.html'
	return render(request,template_name,context)
@minified_response
def datasekolah(request):
	context = {}
	template_name = 'datasekolah.html'
	return render(request,template_name,context)
@minified_response
def ekstrakurikuler(request):
	context = {}
	template_name = 'ekstrakurikuler.html'
	return render(request,template_name,context)
@minified_response
def osis(request):
	context = {}
	template_name = 'osis.html'
	return render(request,template_name,context)


@minified_response
def pramuka(request):
	context = {}
	template_name = 'ekstrakurikuler/pramuka.html'
	return render(request,template_name,context)


@minified_response
def rohis(request):
	context = {}
	template_name = 'ekstrakurikuler/rohis.html'
	return render(request,template_name,context)


@minified_response
def pks(request):
	context = {}
	template_name = 'ekstrakurikuler/pks.html'
	return render(request,template_name,context)


@minified_response
def pmr(request):
	context = {}
	template_name = 'ekstrakurikuler/pmr.html'
	return render(request,template_name,context)


@minified_response
def redaksi(request):
	context = {}
	template_name = 'ekstrakurikuler/redaksi.html'
	return render(request,template_name,context)


@minified_response
def paskibra(request):
	context = {}
	template_name = 'ekstrakurikuler/paskibra.html'
	return render(request,template_name,context)


@minified_response
def basket(request):
	context = {}
	template_name = 'ekstrakurikuler/basket.html'
	return render(request,template_name,context)


@minified_response
def karawitan(request):
	context = {}
	template_name = 'ekstrakurikuler/karawitan.html'
	return render(request,template_name,context)



#_______________STATIC_____________________#


def error(request):
    response = render_to_response('error404.html', {'title': '400 Bad Request', 'message': '404'},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response
