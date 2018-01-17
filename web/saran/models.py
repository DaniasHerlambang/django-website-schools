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

#-----------------------------------------------> data_saran <-----------------------------------------------#
class SaranQuerySet(models.QuerySet):
    def saran_active(self):
        return self.filter(publish_saran=True)

class data_saran(models.Model):
    id_saran = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=120)

    # alamat_saran = models.CharField(max_length=120)
    nomor_atau_email = models.CharField(max_length=120)
    saran = models.TextField()

    updt = models.DateTimeField(auto_now=True , auto_now_add=False)
    tms = models.DateTimeField(auto_now_add=True)

    publish_saran = models.BooleanField(default=False)

    objects = SaranQuerySet.as_manager()


    class Meta:
        ordering = ["-updt","-tms"]
        verbose_name = 'Detail data saran'
        verbose_name_plural = 'data saran'
