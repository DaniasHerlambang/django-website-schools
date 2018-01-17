from django.utils import timezone
from django import forms

from .models import data_saran

class SaranForm(forms.ModelForm):
	today = timezone.now().date()

	nama = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control','id' : 'name'
                                                      ,'placeholder' : 'Masukan Nama Anda',}),
                        label=(""))
	nomor_atau_email = forms.CharField( widget=forms.TextInput(attrs={'class' : 'form-control','id' : 'email'
                                                      ,'placeholder' : 'Masukan Nomor Hp Atau Email Anda', }),
                                    label=(""))
	saran = forms.CharField( widget=forms.Textarea(attrs={'class' : 'form-control','id' : 'message'
                                                      ,'placeholder' : 'Tuliskan Kritik dan Saran Anda', }),
                                    label=(""))

	class Meta:
		model = data_saran
		fields = [
			"nama",
			"nomor_atau_email",
			"saran",
		]
