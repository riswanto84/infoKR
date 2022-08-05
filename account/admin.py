from django.contrib import admin
from .models import UserAdmin

@admin.register(UserAdmin)
class UserAdmin(admin.ModelAdmin):
    list_display = ['user', 'nama', 'email']
    search_fields = ['nama',]
