from django import forms
from django.forms import ModelForm, widgets
from .models import UserAdmin
from django.utils.translation import ugettext_lazy as _

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
            'email': _('Alamat Email'),
            'profil_pic': _('Foto Profil'),
        }