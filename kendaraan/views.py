from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .decorators import check_superadmin, check_admin_and_superadmin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import FotoKendaraan, Kendaraan, Pegawai

from django.contrib import messages
from .forms import *

@login_required(login_url='login')
def dashboard(request):
    kendaraan_list = Kendaraan.objects.all().order_by('id')
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
            # return HttpResponse('keyword tidak boleh kosong')
            messages.info(request, 'Kolom pencarian tidak boleh kosong!')
            allert = 'alert-danger'
            context = {
                'kendaraan': kendaraan,
                'jumlah_pegawai': jumlah_pegawai,
                'jumlah_kendaraan': jumlah_kendaraan,
                'allert': allert,
            }
            return render(request, 'kendaraan/dashboard.html', context)
        
        query_nopol = Kendaraan.objects.filter(nomor_polisi__contains=nopol_keyword)
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
        
        query_pegawai = Pegawai.objects.filter(nama__contains=pegawai_keyword)
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
    }
    return render(request, 'kendaraan/pegawai.html', context)

@login_required(login_url='login')
def tambah_pegawai(request):
    jumlah_pegawai = Pegawai.objects.count()
    jumlah_kendaraan = Kendaraan.objects.count()
    
    form = PegawaiForm
    
    context = {
        'jumlah_pegawai': jumlah_pegawai,
        'jumlah_kendaraan': jumlah_kendaraan,
        'form': form,
    }
    return render(request, 'kendaraan/tambah_pegawai.html', context)

@login_required(login_url='login')
@check_admin_and_superadmin
def kendaraan(request):
    return HttpResponse('ini laman kendaraan, hanya bisa dilihat admin dan superadmin')

@login_required(login_url='login')
@check_superadmin
def admin_system(request):
    return HttpResponse('ini laman admin system, hanya untuk superadmin')


