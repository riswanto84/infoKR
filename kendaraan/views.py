from ast import Or
from multiprocessing import context
from operator import and_
from ssl import create_default_context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from account.forms import UserRegistrationForm
from account.models import UserAdmin

from .decorators import check_superadmin, check_admin_and_superadmin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import FotoKendaraan, Kendaraan, Pegawai

from django.contrib import messages
from django.db.models.deletion import RestrictedError
from .forms import *
from django.forms import inlineformset_factory

@login_required(login_url='login')
def dashboard(request):
    kendaraan_list = Kendaraan.objects.all().order_by('-id')
    page = request.GET.get('page', 1)
    
    jumlah_pegawai = Pegawai.objects.count()
    jumlah_kendaraan = Kendaraan.objects.count()

    paginator = Paginator(kendaraan_list, 10)
    try:
        kendaraan = paginator.page(page)
    except PageNotAnInteger:
        kendaraan = paginator.page(1)
    except EmptyPage:
        kendaraan = paginator.page(paginator.num_pages)
        
    if request.method == 'POST':
        nopol_keyword = request.POST['keyword']
        if nopol_keyword == '':
            messages.info(request, 'Kolom pencarian tidak boleh kosong!')
            allert = 'alert-danger'
            context = {
                'kendaraan': kendaraan,
                'jumlah_pegawai': jumlah_pegawai,
                'jumlah_kendaraan': jumlah_kendaraan,
                'allert': allert,
            }
            return render(request, 'kendaraan/dashboard.html', context)
        
        query_nopol = Kendaraan.objects.filter(nomor_polisi__contains=nopol_keyword) or Kendaraan.objects.filter(pemilik__nama__contains=nopol_keyword)
        if query_nopol:
            messages.info(request, 'Nomor Polisi ditemukan.')
            allert = 'alert-success'
            context = {
                'kendaraan': query_nopol,
                'jumlah_pegawai': jumlah_pegawai,
                'jumlah_kendaraan': jumlah_kendaraan,
                'allert': allert,
            }
            return render(request, 'kendaraan/dashboard.html', context)
        else:
            messages.info(request, 'Nomor Polisi tidak ditemukan!')
            allert = 'alert-danger'
            context = {
                'kendaraan': query_nopol,
                'jumlah_pegawai': jumlah_pegawai,
                'jumlah_kendaraan': jumlah_kendaraan,
                'allert': allert,
            }
            return render(request, 'kendaraan/dashboard.html', context)

    context = {
        'kendaraan': kendaraan,
        'jumlah_pegawai': jumlah_pegawai,
        'jumlah_kendaraan': jumlah_kendaraan,
    }
    return render(request, 'kendaraan/dashboard.html', context)

@login_required(login_url='login')
def detail_kendaraan(request, pk):
    kendaraan = Kendaraan.objects.get(id=pk)
    id_kendaraan = kendaraan.id
    foto_kendaraan = FotoKendaraan.objects.filter(nomor_polisi_id=id_kendaraan)
    context = {
        'detail_kendaraan': kendaraan,
        'foto_kendaraan': foto_kendaraan,
    }
    return render(request, 'kendaraan/detail_kendaraan.html', context)

@login_required(login_url='login')
@check_admin_and_superadmin
def pegawai(request):
    pegawai_list = Pegawai.objects.all().order_by('id')
    page = request.GET.get('page', 1)
    
    allert = 'alert-success'
    
    jumlah_pegawai = Pegawai.objects.count()
    jumlah_kendaraan = Kendaraan.objects.count()
    
    
    paginator = Paginator(pegawai_list, 10)
    try:
        pegawai = paginator.page(page)
    except PageNotAnInteger:
        pegawai = paginator.page(1)
    except EmptyPage:
        pegawai = paginator.page(paginator.num_pages)
    
    if request.method == 'POST':
        pegawai_keyword = request.POST['keyword']
        if pegawai_keyword == '':
            messages.info(request, 'Kolom pencarian tidak boleh kosong!')
            allert = 'alert-danger'
            context = {
                'pegawai': pegawai,
                'jumlah_pegawai': jumlah_pegawai,
                'jumlah_kendaraan': jumlah_kendaraan,
                'allert': allert,
            }
            return render(request, 'kendaraan/pegawai.html', context)
        
        query_pegawai = Pegawai.objects.filter(nama__contains=pegawai_keyword) or Pegawai.objects.filter(nip__contains=pegawai_keyword) or Pegawai.objects.filter(unit_kerja__nama_unit__contains=pegawai_keyword)
        if query_pegawai:
            messages.info(request, 'Data pegawai ditemukan.')
            allert = 'alert-success'
            context = {
                'pegawai': query_pegawai,
                'jumlah_pegawai': jumlah_pegawai,
                'jumlah_kendaraan': jumlah_kendaraan,
                'allert': allert,
            }
            return render(request, 'kendaraan/pegawai.html', context)
        else:
            messages.info(request, 'Data pegawai tidak ditemukan!')
            allert = 'alert-danger'
            context = {
                'kendaraan': query_pegawai,
                'jumlah_pegawai': jumlah_pegawai,
                'jumlah_kendaraan': jumlah_kendaraan,
                'allert': allert,
            }
            return render(request, 'kendaraan/pegawai.html', context)
        
    
    context = {
        'pegawai': pegawai,
        'jumlah_pegawai': jumlah_pegawai,
        'jumlah_kendaraan': jumlah_kendaraan,
        'allert': allert,
    }
    return render(request, 'kendaraan/pegawai.html', context)

@check_admin_and_superadmin
@login_required(login_url='login')
def tambah_pegawai(request):
    jumlah_pegawai = Pegawai.objects.count()
    jumlah_kendaraan = Kendaraan.objects.count()
    
    form = PegawaiForm
    if request.method == 'POST':
        form = PegawaiForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, 'Data Pegawai berhasil disimpan')
            return redirect('pegawai')
    context = {
        'jumlah_pegawai': jumlah_pegawai,
        'jumlah_kendaraan': jumlah_kendaraan,
        'form': form,
    }
    return render(request, 'kendaraan/tambah_pegawai.html', context)

@check_admin_and_superadmin
@login_required(login_url='login')
def detail_pegawai(request, pk):
    data = Pegawai.objects.get(id=pk)
    kendaraan_terdaftar = Kendaraan.objects.filter(pemilik_id=data.id)
    
    context = {
        'data': data,
        'kendaraan_terdaftar': kendaraan_terdaftar,
    }
    return render(request, 'kendaraan/detail_pegawai.html', context)

@check_admin_and_superadmin
@login_required(login_url='login')
def ubah_pegawai(request, pk):
    pegawai = Pegawai.objects.get(id=pk)
    form = PegawaiForm(instance=pegawai)
    
    if request.method == 'POST':
        form = PegawaiForm(request.POST, request.FILES, instance=pegawai)
        form.save()
        messages.info(request, 'Data berhasil diubah')
        return redirect('pegawai')
    
    context = {
        'form': form,
    }
    return render(request, 'kendaraan/ubah_pegawai.html', context)

@check_admin_and_superadmin
@login_required(login_url='login')
def hapus_pegawai(request, pk):
    try:
        pegawai = Pegawai.objects.get(id=pk)
        pegawai.delete()
        messages.info(request, 'Data berhasil dihapus')
        return redirect('pegawai')
    except RestrictedError:
        return HttpResponse('Tidak dapat menghapus data..!')

@login_required(login_url='login')
@check_admin_and_superadmin
def kendaraan(request):
    jumlah_pegawai = Pegawai.objects.count()
    jumlah_kendaraan = Kendaraan.objects.count()
    kendaraan = Kendaraan.objects.all().order_by('-id')
    page = request.GET.get('page', 1)
    allert = 'alert-success'
    
    paginator = Paginator(kendaraan, 10)
    try:
        kendaraan = paginator.page(page)
    except PageNotAnInteger:
        kendaraan = paginator.page(1)
    except EmptyPage:
        kendaraan = paginator.page(paginator.num_pages)
    
    if request.method == 'POST':
        kendaraan_keyword = request.POST['keyword']
        if kendaraan_keyword == '':
            messages.info(request, 'Kolom pencarian tidak boleh kosong!')
            allert = 'alert-danger'
            context = {
                'kendaraan': kendaraan,
                'jumlah_pegawai': jumlah_pegawai,
                'jumlah_kendaraan': jumlah_kendaraan,
                'allert': allert,
            }
            return render(request, 'kendaraan/kendaraan.html', context)
        
        query_kendaraan = Kendaraan.objects.filter(nomor_polisi__contains=kendaraan_keyword) or Kendaraan.objects.filter(pemilik__nama__contains=kendaraan_keyword) or Kendaraan.objects.filter(pemilik__unit_kerja__nama_unit__contains=kendaraan_keyword)
        if query_kendaraan:
            messages.info(request, 'Data kendaraan ditemukan.')
            allert = 'alert-success'
            context = {
                'kendaraan': query_kendaraan,
                'jumlah_pegawai': jumlah_pegawai,
                'jumlah_kendaraan': jumlah_kendaraan,
                'allert': allert,
            }
            return render(request, 'kendaraan/kendaraan.html', context)
        else:
            messages.info(request, 'Data kendaraan tidak ditemukan!')
            allert = 'alert-danger'
            context = {
                'kendaraan': query_kendaraan,
                'jumlah_pegawai': jumlah_pegawai,
                'jumlah_kendaraan': jumlah_kendaraan,
                'allert': allert,
            }
            return render(request, 'kendaraan/kendaraan.html', context)
    
    context = {
        'jumlah_pegawai': jumlah_pegawai,
        'jumlah_kendaraan': jumlah_kendaraan,
        'kendaraan': kendaraan,
        'allert': allert,
    }
    return render(request, 'kendaraan/kendaraan.html', context)

@login_required(login_url='login')
@check_admin_and_superadmin
def tambah_kendaraan(request):
    jumlah_pegawai = Pegawai.objects.count()
    jumlah_kendaraan = Kendaraan.objects.count()
    
    form = KendaraanForm
    form_foto = FotoKendaraanForm
    
    if request.method == 'POST':
        form = KendaraanForm(request.POST, request.FILES)
        form_foto = FotoKendaraanForm(request.POST, request.FILES)
        images = request.FILES.getlist('foto_kendaraan')
        if form.is_valid() and form_foto.is_valid():
            data = request.POST
            kendaraan, created = Kendaraan.objects.get_or_create(
                nomor_polisi = data['nomor_polisi'],
                jenis_kendaraan = data['jenis_kendaraan'],
                pemilik_id = data['pemilik'],
                warna = data['warna'],
                merk_type = data['merk_type'],
                keterangan = data['keterangan'],
            )
            for image in images:
                foto_kendaraan = FotoKendaraan.objects.create(
                    nomor_polisi = kendaraan,
                    foto_kendaraan = image,
                )
            messages.info(request, 'Data kendaraan berhasil disimpan')
            return redirect('kendaraan')
    context = {
        'jumlah_pegawai': jumlah_pegawai,
        'jumlah_kendaraan': jumlah_kendaraan,
        'form': form,
        'form_foto': form_foto,
    }
    return render(request, 'kendaraan/tambah_kendaraan.html', context)

@login_required(login_url='login')
@check_admin_and_superadmin
def hapus_kendaraan(request, pk):
    try:
        kendaraan = Kendaraan.objects.get(id=pk)
        kendaraan.delete()
        messages.info(request, 'Data berhasil dihapus')
        return redirect('kendaraan')
    except RestrictedError:
        return HttpResponse('Tidak dapat menghapus data..!')

@login_required(login_url='login')
@check_admin_and_superadmin
def detail_kendaraan_admin(request, pk):
    kendaraan = Kendaraan.objects.get(id=pk)
    id_kendaraan = kendaraan.id
    foto_kendaraan = FotoKendaraan.objects.filter(nomor_polisi_id=id_kendaraan)
    context = {
        'detail_kendaraan': kendaraan,
        'foto_kendaraan': foto_kendaraan,
    }
    return render(request, 'kendaraan/detail_kendaraan_admin.html', context)

@login_required(login_url='login')
@check_admin_and_superadmin
def edit_kendaraan(request, pk):
    jumlah_pegawai = Pegawai.objects.count()
    jumlah_kendaraan = Kendaraan.objects.count()
    kendaraan = Kendaraan.objects.get(id=pk)
    form = KendaraanForm(instance = kendaraan)
    KendaraanFormset = inlineformset_factory(Kendaraan, FotoKendaraan, fields=('foto_kendaraan',), extra=1)
    formset = KendaraanFormset(instance=kendaraan)
    
    if request.method == 'POST':
        form = KendaraanForm(request.POST, request.FILES, instance=kendaraan)
        formset = KendaraanFormset(request.POST, request.FILES, instance=kendaraan)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            messages.info(request, 'Data berhasil diubah')
            return redirect('kendaraan')
    context = {
        'jumlah_pegawai': jumlah_pegawai,
        'jumlah_kendaraan': jumlah_kendaraan,
        'kendaraan': kendaraan,
        'form': form,
        'formset': formset,
    }
    return render(request, 'kendaraan/edit_kendaraan.html', context)



