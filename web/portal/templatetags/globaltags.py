from __future__ import unicode_literals
from django import template
from django.shortcuts import render , get_object_or_404 , redirect
from django.contrib import messages
from django.shortcuts import render

from portal.models import *
from saran.models import *
# from saran.forms import SaranForm

register = template.Library()

@register.assignment_tag
def recentposts():
    posts = Post.objects.active()
    return posts[:4]

@register.assignment_tag
def recentcomments():
    comments = data_saran.objects.saran_active()
    return comments[:4]


# @register.assignment_tag
# def tambah():
#     form = SaranForm()
#     if form.is_valid():
#         post = form.save(commit=True)
#         post.save()
#         return redirect('post_home')
#         print ("test njir")
#     return form
