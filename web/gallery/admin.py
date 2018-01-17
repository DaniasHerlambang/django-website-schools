# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from gallery.models import foto

class DatafotoAdmin(admin.ModelAdmin):
	list_display = ('id_foto',"updt","tms",'nama_foto','dokumen_foto', "publish_foto")
	search_fields = ['nama_foto', 'dokumen_foto']

admin.site.register(foto , DatafotoAdmin)
