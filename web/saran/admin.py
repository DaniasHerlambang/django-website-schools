# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

#app webshit dari models
from saran.models import data_saran

# Register your models here.
def publish_saran(modeladmin, request, queryset):
    queryset.update(publish_saran='True')
publish_saran.short_description = "Publish Saran Pilihan"

def publish_batal(modeladmin, request, queryset):
    queryset.update(publish_saran='False')
publish_batal.short_description = "Batal Publish Saran Pilihan"

class DataSaranAdmin(admin.ModelAdmin):
    list_display = ('nama', 'nomor_atau_email',
                    'saran',"updt","tms","publish_saran")
    search_fields = ['nama', 'nomor_atau_email']
    actions = [publish_saran , publish_batal]


admin.site.register(data_saran , DataSaranAdmin)
