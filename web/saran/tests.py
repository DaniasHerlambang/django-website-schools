# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.
          <div class="col-md-6">
            <h4 class="text-uppercase">
              Saran
            </h4>
            <div class="form">
              <div id="sendmessage">Your message has been sent. Thank you!</div>
              <div id="errormessage"></div>
              {% if form %}
              <form action="" method="POST" role="form" class="contactForm">{% csrf_token %}
                {{ form.as_p }}
                  <div class="text-center"><button class="btn btn-sm btn-success" type="submit">Send Message</button></div>
              </form>
              {% endif %}
            </div>
          </div>




def tambah_saran(request):

	context = {}
	template_name = 'saran.html'
	return render(request,template_name,context)


<!-- {% extends "base.html" %} {% load staticfiles %} {% block content %}
<section id="page-breadcrumb">
  <div class="vertical-center sun">
    <div class="container">
      <div class="row">
        <div class="action">
          <div class="col-sm-12">
            <strong><h1 class="title">Saran </h1></strong>
            <ol class="breadcrumb">
              <li><a href='{% url "post_home" %}'>Home</a>
              </li>
              <li class="active">Saran</li>
            </ol>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
<section id="blog" class="padding-top">
  <div class="container">
    <div class="row">

      <div class="col-md-9 col-sm-7">
        <div class="row">
          <div class="well">
            <center>

              <div class="caption wow fadeInDown">
                <div class="thumbnail">
                  <p>
                    <p>Assalamu’alaikum Wr.Wb.</p>

                    <p>Gunakan layanan ini dengan sebaik mungkin , Kami akan mengoreksi kiriman anda sebelum ditampilkan di KUMPULAN SARAN</p>

                    <p>Untuk menghindari penyalah gunaan layanan ini dari pihak tidak bertanggung jawab atau spam yang merugikan</p>

                    <p>Wassalamu’alaikum wr.wb.</p>

                </div>
                {% if form %}
                <form action="" method="POST" role="form" class="contactForm caption wow fadeInUp">{% csrf_token %} {{ form.as_p }}
                  <div class="text-center"><button data-toggle="modal" class="btn btn-sm btn-success" type="submit">Send Message</button></div>
                </form>
                {% endif %}

              </div>
            </center>
          </div>
        </div>
      </div>

      {% endblock %}
 -->
