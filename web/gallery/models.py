# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone

from django.utils.text import slugify

from django.core.exceptions import ObjectDoesNotExist

# Create your models here.
#-----------------------------------------------> data_foto <-----------------------------------------------#
class FotoQuerySet(models.QuerySet):
	def foto_active(self):
	       return self.filter(publish_foto=True)

class foto(models.Model):
	id_foto = models.AutoField(primary_key=True)
	nama_foto = models.CharField(max_length=120)

	dokumen_foto = models.FileField(upload_to='Dokumen_foto/')

	updt = models.DateTimeField(auto_now=True , auto_now_add=False)
	tms = models.DateTimeField(auto_now_add=True)

	publish_foto = models.BooleanField(default=True)

	objects = FotoQuerySet.as_manager()

	

	class Meta:
		ordering = ["-updt","-tms"]
		verbose_name = 'Detail foto'
		verbose_name_plural = ' foto'
