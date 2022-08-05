from django.db import models
from django.contrib.auth.models import User

class UserAdmin(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.RESTRICT)
    nama = models.CharField(max_length=200)
    no_hp = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    profil_pic = models.ImageField(
        default="profilepics/avatar.jpg", blank=True, null=True, upload_to='profilepics')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nama
