from distutils.command.upload import upload
from pyexpat import model
from sre_constants import CATEGORY
from tokenize import blank_re
from django.db import models

class UnitKerja(models.Model):
    nama_unit = models.CharField(max_length=300, blank=False, null=False)

    def __str__(self):
        return self.nama_unit

class Pegawai(models.Model):
    nama = models.CharField(max_length=200, blank=False, null=False)
    nip = models.CharField(max_length=20, blank=True, null=True)
    unit_kerja = models.ForeignKey(UnitKerja, on_delete=models.CASCADE)
    nomor_hp = models.CharField(max_length=15, blank=False, null=False)
    email = models.EmailField(blank=True, null=True)
    alamat = models.TextField(blank=True, null=True)
    foto = models.ImageField(default="profilepics/avatar.jpg", blank=True, null=True, upload_to='foto_pegawai')

    def __str__(self):
        return self.nama

class Kendaraan(models.Model):
    CATEGORY = (
        ('Sepeda Motor Dinas', 'sepeda motor dinas'),
        ('Mobil Dinas', 'mobil dinas'),
        ('Sepeda Motor Pribadi', 'sepeda motor pribadi'),
        ('Mobil Pribadi', 'mobil pribadi'),
        ('Bus Jemputan', 'bus jemputan'),
        ('Ambulans', 'ambulans'),
        ('Kendaraan Lainnya', 'kendaraan lainnya')
    )

    WARNA = (
        ('Abu-abu', 'abu-abu'),
        ('Biru', 'biru'),
        ('Coklat', 'coklat'),
        ('Hitam', 'hitam'),
        ('Hijau', 'hijau'),
        ('Merah', 'merah'),
        ('Putih', 'putih'),
        ('Kuning', 'kuning'),
        ('Silver', 'silver'),
        ('Ungu', 'ungu'),
        ('Pink', 'pink'),
        ('Lainnya', 'lainnya'),
    )
    nomor_polisi = models.CharField(max_length=10, blank=False, null=False)
    jenis_kendaraan = models.CharField(max_length=200, choices=CATEGORY)
    pemilik = models.ForeignKey(Pegawai, on_delete=models.CASCADE)
    warna = models.CharField(max_length=200, choices=WARNA)
    merk_type = models.CharField(max_length=300, blank=True, null=True)
    keterangan = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.nomor_polisi

class FotoKendaraan(models.Model):
    nomor_polisi = models.ForeignKey(Kendaraan, on_delete=models.CASCADE)
    foto_kendaraan = models.ImageField(blank=True, null=True, upload_to='foto_kendaraan')

    