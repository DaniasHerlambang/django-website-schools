# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

#app webshit dari models
from portal.models import Post , data_kepala_sekolah , data_guru , data_tu , siswa ,silabus , filex

# Register your models here.

class PostAdmin(admin.ModelAdmin):
	list_display = ["title","user","updated","timestamp","publish"]
	list_display_links = ["updated","title"]
	# list_editable = ["title"]
	prepopulated_fields = {'slug': ('title',)}
	list_filter = ["updated","timestamp"]
	search_fields = ["title","content"]

	class Meta:
		model = Post

class KepalaSekolahAdmin(admin.ModelAdmin):
    list_display = ('nama_kep_sek','nip_kep_sek','foto_kep_sek')
    search_fields = ['nama_kep_sek', 'nip_kep_sek']


class DataGuruAdmin(admin.ModelAdmin):
    list_display = ('id_guru', 'nip_guru',"updt","tms",
	'nama_guru','kelamin_guru', 'pelajaran_guru', "publish_guru")
    search_fields = ['nama_guru', 'nip_guru']

class DataTuAdmin(admin.ModelAdmin):
    list_display = ('id_tu', 'nip_tu',"updt","tms",
	'nama_tu','kelamin_tu', 'pelajaran_tu', "publish_tu")
    search_fields = ['nama_tu', 'nip_tu']

class DataSiswaAdmin(admin.ModelAdmin):
	list_display = ('id_siswa', 'nis_siswa',"updt","tms",
	'nama_siswa','kelamin_siswa', 'siswa_jurusan', 'siswa_kelas', "publish_siswa")
	search_fields = ['nama_siswa', 'nip_siswa']

class DataSilabusAdmin(admin.ModelAdmin):
	list_display = ('id_silabus',"updt","tms",'nama_silabus','dokumen_silabus', "publish_silabus")
	search_fields = ['nama_silabus', 'dokumen_silabus']

class DataFileAdmin(admin.ModelAdmin):
	list_display = ('id_file',"updt","tms",'nama_file','dokumen_file', "publish_file")
	search_fields = ['nama_file', 'dokumen_file']



# class Post_Views_Admin(admin.ModelAdmin):
#     list_display = ("post", "ip", "created")
#     list_per_page = 20
#
#
# admin.site.register(Post_Views, Post_Views_Admin)
admin.site.register(Post , PostAdmin)
admin.site.register(data_kepala_sekolah , KepalaSekolahAdmin)
admin.site.register(data_guru , DataGuruAdmin)
admin.site.register(data_tu , DataTuAdmin)
admin.site.register(siswa , DataSiswaAdmin)
admin.site.register(silabus , DataSilabusAdmin)
admin.site.register(filex , DataFileAdmin)
