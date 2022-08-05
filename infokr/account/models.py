from pickle import TRUE
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

class Satker(models.Model):
    nama_satker = models.CharField(max_length=500)

    def __str__(self):
        return self.nama_satker

class UserAdmin(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.RESTRICT)
    nama = models.CharField(max_length=200)
    nip = models.CharField(max_length=18, blank=TRUE, null=TRUE)
    satker = models.ForeignKey(Satker, on_delete=models.CASCADE)
    no_hp = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    profil_pic = models.ImageField(
        default="profilepics/avatar.jpeg", blank=True, null=True, upload_to='profilepics')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nama
