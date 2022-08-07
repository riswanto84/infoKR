from pyexpat import model
from django.contrib import admin
from .models import Pegawai, UnitKerja, Kendaraan, FotoKendaraan

@admin.register(UnitKerja)
class UnitKerjaAdmin(admin.ModelAdmin):
    list_display = ['nama_unit',]
    search_fields = ['nama_unit']

@admin.register(Pegawai)
class PegawaiAdmin(admin.ModelAdmin):
    list_display = ['nama', 'unit_kerja', 'nomor_hp',]
    search_fields = ['nama']

class FotoKendaraaAdmin(admin.StackedInline):
    model = FotoKendaraan

@admin.register(Kendaraan)
class KendaraanAdmin(admin.ModelAdmin):
    list_display = ['nomor_polisi', 'merk_type', 'pemilik',]
    search_fields = ['nomor_polisi']
    inlines = [FotoKendaraaAdmin]

    class Meta:
        model = Kendaraan