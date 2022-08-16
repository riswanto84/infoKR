from django.db.models import fields
from django.forms import ModelForm, widgets
from kendaraan.models import *
from django import forms
from django.utils.translation import ugettext_lazy as _

class PegawaiForm(ModelForm):
    class Meta:
        model = Pegawai
        fields = '__all__'
        
        labels = {
            'nama': _('Nama Lengkap'),
            'nip': _('NIP'),
            'unit_kerja': _('Unit Kerja'),
            'nomor_hp': _('Nomor HP'),
        }
    
    def __init__(self, *args, **kwargs):
        super(PegawaiForm, self).__init__(*args, **kwargs)
        
        self.fields['nama'].widget.attrs['class'] = 'mb-2'
        self.fields['nama'].widget.attrs['placeholder'] = 'Masukan nama lengkap'
        self.fields['unit_kerja'].widget.attrs['class'] = 'unit-kerja'
        self.fields['nip'].widget.attrs['class'] = 'mb-2'
        self.fields['nip'].widget.attrs['placeholder'] = 'Masukan NIP / NIK'
        self.fields['nomor_hp'].widget.attrs['placeholder'] = 'Masukan nomor HP'
        self.fields['email'].widget.attrs['class'] = 'email'
        self.fields['email'].widget.attrs['placeholder'] = 'Masukan alamat email'

class KendaraanForm(ModelForm):
    class Meta:
        model = Kendaraan
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(KendaraanForm, self).__init__(*args, **kwargs)
        self.fields['nomor_polisi'].widget.attrs['class'] = 'mb-2'
        self.fields['jenis_kendaraan'].widget.attrs['class'] = 'mb-2'
        
class FotoKendaraanForm(ModelForm):
    foto_kendaraan = forms.ImageField(label="Foto", widget=forms.ClearableFileInput(attrs={"multiple": True}),)
    
    class Meta:
        model = FotoKendaraan
        fields = ("foto_kendaraan",)
    
    