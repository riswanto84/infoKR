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
        ('Sepeda Motor Dinas', 'Sepeda Motor Dinas'),
        ('Mobil Dinas', 'Mobil Dinas'),
        ('Sepeda Motor Pribadi', 'Sepeda Motor Pribadi'),
        ('Mobil Pribadi', 'Mobil Pribadi'),
        ('Bus Jemputan', 'Bus Jemputan'),
        ('Ambulans', 'Ambulans'),
        ('Kendaraan Lainnya', 'Kendaraan Lainnya')
    )

    WARNA = (
        ('Hitam', 'Hitam'),
        ('Silver', 'Silver'),
        ('Putih', 'Putih'),
        ('Abu-abu', 'Abu-Abu'),
        ('Biru', 'Biru'),
        ('Coklat', 'Coklat'),
        ('Hijau', 'Hijau'),
        ('Merah', 'Merah'),
        ('Kuning', 'Kuning'),
        ('Lainnya', 'Lainnya'),
    )
    nomor_polisi = models.CharField(max_length=10, blank=False, null=False)
    jenis_kendaraan = models.CharField(max_length=200, choices=CATEGORY)
    pemilik = models.ForeignKey(Pegawai, on_delete=models.CASCADE)
    warna = models.CharField(max_length=200, choices=WARNA, default='Lainnya')
    merk_type = models.CharField(max_length=300, blank=True, null=True)
    keterangan = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.nomor_polisi

class FotoKendaraan(models.Model):
    nomor_polisi = models.ForeignKey(Kendaraan, on_delete=models.CASCADE)
    foto_kendaraan = models.ImageField(blank=True, null=True, upload_to='foto_kendaraan')

    