# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone

from django.utils.text import slugify
from redactor.fields import RedactorField

from django.core.exceptions import ObjectDoesNotExist

# Create your models here.

class PostQuerySet(models.QuerySet):
    def active(self):
        return self.filter(publish=True)

def upload_location(instance, filename):
	# filebase, extension = filename.split(".")
	return "%s/%s" %(instance.id , filename)

class Post(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default = 1)
	title = models.CharField(max_length=120)
	slug = models.SlugField(unique=True)
	cover = models.ImageField(upload_to=upload_location,
		null=True,
		blank=True,
		width_field="width_field",
		height_field="height_field")
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	content = RedactorField()
	publish = models.BooleanField(default=True)
	# publish = models.DateField(auto_now=False, auto_now_add=False)
	launching = models.DateField(auto_now=False, auto_now_add=False)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	# objects = PostManager()
	objects = PostQuerySet.as_manager()

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title
    #
	def get_absolute_url(self):
		return reverse ("post_detail", kwargs={"slug": self.slug})

	class Meta:
		ordering = ["-timestamp","-updated"]


def create_slug(instance, new_slug=None):
	slug = slugify(instance.title)
	if new_slug is not None:
		slug = new_slug
	qs = Post.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()
	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug(instance, new_slug=new_slug)
	return slug

def pre_save_post_receiver(sender , instance , *args , **kwargs):
	# slug = slugify(instance.title)
	# exists = Post.objects.filter(slug=slug).exists()
	# if exists:
	# 	slug = "%s-%s" %(slug, instance.id)
	# instance.slug = slug

	if not instance.slug:
		instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, sender=Post)


#-----------------------------------------------> data_kepala_sekolah <-----------------------------------------------#
class data_kepala_sekolah(models.Model):
    nama_kep_sek = models.CharField(max_length=120)
    nip_kep_sek= models.CharField(max_length=120)
    foto_kep_sek = models.ImageField(upload_to='Foto_kepala_sekolah %Y %m %d',
                               null=True,
                               blank=True,
                               help_text="Upload your photo for Avatar")
    pesan_kep_sek = models.TextField()

    class Meta:
        verbose_name = 'Detail Kepala Sekolah'
        verbose_name_plural = 'Kepala Sekolah'

#-----------------------------------------------> jenis_kelamin <-----------------------------------------------#
from dj.choices import Choices, Choice

class jenis_kelamin(Choices):
    perempuan = Choice("perempuan")
    laki = Choice("laki")
    not_specified = Choice("not specified")

#-----------------------------------------------> data_guru <-----------------------------------------------#
class GuruQuerySet(models.QuerySet):
    def guru_active(self):
        return self.filter(publish_guru=True)

class data_guru(models.Model):
    id_guru = models.AutoField(primary_key=True)
    nip_guru = models.CharField(max_length=120)
    nama_guru = models.CharField(max_length=120)

    # alamat_guru = models.CharField(max_length=120)
    pendidikan_guru = models.CharField(max_length=120)
    jurusan_guru = models.CharField(max_length=120)

    kelamin_guru = models.IntegerField(choices=jenis_kelamin(),
            default=jenis_kelamin.not_specified.id)
    pelajaran_guru = models.CharField(max_length=120)
    foto_guru = models.ImageField(upload_to='Foto_guru %Y %m %d',
                               null=True,
                               blank=True,
                               help_text="Upload your photo for Avatar")

    updt = models.DateTimeField(auto_now=True , auto_now_add=False)
    tms = models.DateTimeField(auto_now_add=True)

    publish_guru = models.BooleanField(default=True)


    objects = GuruQuerySet.as_manager()

    class Meta:
        ordering = ["-updt","-tms"]
        verbose_name = 'Detail data Guru'
        verbose_name_plural = 'data Guru'

#-----------------------------------------------> data_TU <-----------------------------------------------#
class TuQuerySet(models.QuerySet):
    def tu_active(self):
        return self.filter(publish_tu=True)

class data_tu(models.Model):
    id_tu = models.AutoField(primary_key=True)
    nip_tu = models.CharField(max_length=120)
    nama_tu = models.CharField(max_length=120)

    # alamat_tu = models.CharField(max_length=120)
    pendidikan_tu = models.CharField(max_length=120)
    jurusan_tu = models.CharField(max_length=120)

    kelamin_tu = models.IntegerField(choices=jenis_kelamin(),
            default=jenis_kelamin.not_specified.id)
    pelajaran_tu = models.CharField(max_length=120)
    foto_tu = models.ImageField(upload_to='Foto_tu %Y %m %d',
                               null=True,
                               blank=True,
                               help_text="Upload your photo for Avatar")

    updt = models.DateTimeField(auto_now=True , auto_now_add=False)
    tms = models.DateTimeField(auto_now_add=True)

    publish_tu = models.BooleanField(default=True)


    objects = TuQuerySet.as_manager()

    class Meta:
        ordering = ["-updt","-tms"]
        verbose_name = 'Detail data Tu'
        verbose_name_plural = 'data Tu'

#-----------------------------------------------> data_siswa <-----------------------------------------------#
class SiswaQuerySet(models.QuerySet):
    def siswa_active(self):
        return self.filter(publish_siswa=True)

class siswa(models.Model):
    id_siswa = models.AutoField(primary_key=True)
    nis_siswa = models.CharField(max_length=120)
    nama_siswa = models.CharField(max_length=120)

    # alamat_siswa = models.CharField(max_length=120)
    # pendidikan_siswa = models.CharField(max_length=120)
    siswa_kelas = models.CharField(max_length=120)

    kelamin_siswa = models.IntegerField(choices=jenis_kelamin(),
            default=jenis_kelamin.not_specified.id)
    siswa_jurusan = models.CharField(max_length=120)
    foto_siswa = models.ImageField(upload_to='Foto_siswa %Y %m %d',
                               null=True,
                               blank=True,
                               help_text="Upload your photo for Avatar")

    updt = models.DateTimeField(auto_now=True , auto_now_add=False)
    tms = models.DateTimeField(auto_now_add=True)

    publish_siswa = models.BooleanField(default=True)


    objects = SiswaQuerySet.as_manager()

    class Meta:
        ordering = ["-updt","-tms"]
        verbose_name = 'Detail data Siswa'
        verbose_name_plural = 'data Siswa'

#-----------------------------------------------> data_silabus <-----------------------------------------------#
class SilabusQuerySet(models.QuerySet):
	def silabus_active(self):
	       return self.filter(publish_silabus=True)

class silabus(models.Model):
	id_silabus = models.AutoField(primary_key=True)
	nama_silabus = models.CharField(max_length=120)

	dokumen_silabus = models.FileField(upload_to='Dokumen_silabus/')

	updt = models.DateTimeField(auto_now=True , auto_now_add=False)
	tms = models.DateTimeField(auto_now_add=True)

	publish_silabus = models.BooleanField(default=True)

	objects = SilabusQuerySet.as_manager()

	class Meta:
		ordering = ["-updt","-tms"]
		verbose_name = 'Detail data Silabus'
		verbose_name_plural = 'data Silabus'

#-----------------------------------------------> data_file <-----------------------------------------------#
class FileQuerySet(models.QuerySet):
	def file_active(self):
	       return self.filter(publish_file=True)

class filex(models.Model):
	id_file = models.AutoField(primary_key=True)
	nama_file = models.CharField(max_length=120)

	dokumen_file = models.FileField(upload_to='Dokumen_file/')

	updt = models.DateTimeField(auto_now=True , auto_now_add=False)
	tms = models.DateTimeField(auto_now_add=True)

	publish_file = models.BooleanField(default=True)

	objects = FileQuerySet.as_manager()

	class Meta:
		ordering = ["-updt","-tms"]
		verbose_name = 'Detail data File'
		verbose_name_plural = 'data File'


#-----------------------------------------------> Home_views <-----------------------------------------------#
class Home_Views(models.Model):
    post = models.ForeignKey(Post, related_name='post_views')
    ip = models.CharField(max_length=40)
    created = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.post.title

    class Meta:
        verbose_name_plural = "Post Views"
        ordering = ['-created']
