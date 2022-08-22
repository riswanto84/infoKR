from django import forms
from django.forms import ModelForm, widgets
from .models import UserAdmin
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.forms import PasswordChangeForm

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserAdminForm(ModelForm):
    class Meta:
        model = UserAdmin
        fields = '__all__'
        exclude = ['user',]

        labels = {
            'nama': _('Nama Lengkap'),
            'no_hp': _('Nomor HP'),
            'nip': _('Masukan NIP / NIK'),
            'email': _('Alamat Email'),
            'profil_pic': _('Foto Profil'),
        }

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Masukan Kembali Password', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('username', 'is_active')
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Password tidak sama.')
        return cd['password2']

class UbahPasswordForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ("old_password","new_password1","new_password2")
        
    old_password = forms.CharField(label = 'Password Lama', widget = forms.PasswordInput(attrs={'class':'form-control mt-1 mb-2', 'type':'password', "placeholder":"Masukan password lama"}))
    new_password1 = forms.CharField(label = 'Password Baru',max_length=50, widget = forms.PasswordInput(attrs={'class':'form-control mt-1 mb-2', 'type':'password', "placeholder":"Masukan password baru"}))
    new_password2 = forms.CharField(label = 'Konfirmasi Password Baru', max_length=50, widget = forms.PasswordInput(attrs={'class':'form-control mt-1 mb-2', 'type':'password', "placeholder":"Konfirmasi password baru"}))