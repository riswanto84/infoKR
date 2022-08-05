from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .decorators import check_superadmin, check_admin_and_superadmin

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'kendaraan/dashboard.html')

@login_required(login_url='login')
@check_admin_and_superadmin
def pegawai(request):
    return HttpResponse('ini laman pegawai, hanya bisa dilihat admin dan superadmin')

@login_required(login_url='login')
@check_admin_and_superadmin
def kendaraan(request):
    return HttpResponse('ini laman kendaraan, hanya bisa dilihat admin dan superadmin')

@login_required(login_url='login')
@check_superadmin
def admin_system(request):
    return HttpResponse('ini laman admin system, hanya untuk superadmin')


