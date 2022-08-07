from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .decorators import check_superadmin, check_admin_and_superadmin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Kendaraan

@login_required(login_url='login')
def dashboard(request):
    kendaraan_list = Kendaraan.objects.all().order_by('id')
    page = request.GET.get('page', 1)

    paginator = Paginator(kendaraan_list, 5)
    try:
        kendaraan = paginator.page(page)
    except PageNotAnInteger:
        kendaraan = paginator.page(1)
    except EmptyPage:
        kendaraan = paginator.page(paginator.num_pages)

    context = {
        'kendaraan': kendaraan,
    }
    return render(request, 'kendaraan/dashboard.html', context)

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


