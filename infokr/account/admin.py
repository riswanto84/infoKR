from django.contrib import admin
from .models import Satker, UserAdmin

@admin.register(UserAdmin)
class UserAdmin(admin.ModelAdmin):
    list_display = ['user', 'nama', 'email']
    search_fields = ['nama',]
    list_filter = ['nama',]

@admin.register(Satker)
class SatkerAdmin(admin.ModelAdmin):
    list_display = ['nama_satker']
    search_fields = ['nama_satker']