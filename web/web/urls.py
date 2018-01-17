"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse ,  HttpResponseRedirect , Http404

from django.conf.urls import include ,url
from django.contrib import admin
from django.views.generic import TemplateView

from portal import views as portal
from gallery import views as gallery
from saran import views as saran

from django.conf.urls import (
    handler404
)
handler404 = 'portal.views.error'

urlpatterns = [
    #static
    url(r'^e$', portal.error, name='error'),

	url(r'^visi$', portal.visi, name='visi'),
	url(r'^sejarah$', portal.sejarah, name='sejarah'),
	url(r'^datasekolah$', portal.datasekolah, name='datasekolah'),
	url(r'^struktur$', portal.struktur, name='struktur'),
	url(r'^keplasekolah$', portal.kepalasekolah, name='kepalasekolah'),

	url(r'^osis$', portal.osis, name='osis'),

	url(r'^ekstrakurikuler$', portal.ekstrakurikuler, name='ekstrakurikuler'),
    url(r'^pramuka$', portal.pramuka, name='pramuka'),
    url(r'^karawitan$', portal.karawitan, name='karawitan'),
    url(r'^pmr$', portal.pmr, name='pmr'),
    url(r'^pks$', portal.pks, name='pks'),
    url(r'^rohis$', portal.rohis, name='rohis'),
    url(r'^basket$', portal.basket, name='basket'),
    url(r'^redaksi$', portal.redaksi, name='redaksi'),
    url(r'^paskibra$', portal.paskibra, name='paskibra'),

	url(r'^dataguru', portal.dataguru, name='dataguru'),
	url(r'^datatu', portal.datatu, name='datatu'),
	url(r'^datasiswa', portal.datasiswa, name='datasiswa'),
	url(r'^datasilabus', portal.datasilabus, name='datasilabus'),
	url(r'^datafile', portal.datafile, name='datafile'),

    url(r'^gallery', gallery.gallery_foto, name='gallery'),
    url(r'^saran', saran.tambah_saran, name='saran'),
    url(r'^daftar_saran', saran.daftar_saran, name='daftar_saran'),

    url(r'^admin/', admin.site.urls),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^$', portal.post_home, name='post_home'),

    #anti httrack
    url(r'^robots.txt$', TemplateView.as_view(template_name="robots.txt", content_type="text/plain"), name="robots_file"),

    url(r'^(?P<slug>[\w-]+)/$', portal.post_detail, name='post_detail'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# if settings.DEBUG:
# 	urlpatterns +=  static (settings.STATIC_URL, document_root= settings.STATIC_ROOT)
#
#     #menyimpan gambar ke file media
# 	urlpatterns +=  static (settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
