from hashlib import new
from multiprocessing import context
from tokenize import group
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .forms import *
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from kendaraan.decorators import check_superadmin, check_admin_and_superadmin
from .models import *
from kendaraan.models import Pegawai, Kendaraan
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@login_required(login_url='login')
def account_setting(request):
    user = request.user.useradmin
    form = UserAdminForm(instance=user)

    if request.method == 'POST':
        form = UserAdminForm(request.POST, request.FILES, instance=user)
        if form.is_valid:
            form.save()
            messages.info(request, 'Data berhasil diubah')
    context = {
        'form': form,
    }
    return render(request, 'account/account_setting.html', context)


@login_required(login_url='login')
@check_admin_and_superadmin
def user_register(request):
    grup_user = User.objects.filter(groups__name = 'user')
    profil = UserAdmin.objects.filter(user__in=list(grup_user)).order_by('-id')
    page = request.GET.get('page', 1)
    paginator = Paginator(profil, 10)
    allert = 'alert-success'
    
    jumlah_pegawai = Pegawai.objects.count()
    jumlah_kendaraan = Kendaraan.objects.count()
    
    try:
        profil = paginator.page(page)
    except PageNotAnInteger:
        profil = paginator.page(1)
    except EmptyPage:
        profil = paginator.page(paginator.num_pages)
    
    if request.method == 'POST':
        user_keyword = request.POST['keyword']
        if user_keyword == '':
            messages.info(request, 'Kolom pencarian tidak boleh kosong!')
            allert = 'alert-danger'
            context = {
                'profil': profil,
                'jumlah_pegawai': jumlah_pegawai,
                'jumlah_kendaraan': jumlah_kendaraan,
                'allert': allert,
            }
            return render(request, 'account/user_register.html', context)
        
        query_profil = UserAdmin.objects.filter(nama__contains=user_keyword)
        if query_profil:
            messages.info(request, 'Data User ditemukan.')
            allert = 'alert-success'
            context = {
                'profil': query_profil,
                'jumlah_pegawai': jumlah_pegawai,
                'jumlah_kendaraan': jumlah_kendaraan,
                'allert': allert,
            }
            return render(request, 'account/user_register.html', context)
        else:
            messages.info(request, 'Data User tidak ditemukan!')
            allert = 'alert-danger'
            context = {
                'profil': query_profil,
                'jumlah_pegawai': jumlah_pegawai,
                'jumlah_kendaraan': jumlah_kendaraan,
                'allert': allert,
            }
            return render(request, 'account/user_register.html', context)
    
    context = {
        'profil': profil,
        'jumlah_pegawai': jumlah_pegawai,
        'jumlah_kendaraan': jumlah_kendaraan,
        'allert': allert,
    }
    return render(request, 'account/user_register.html', context)

@login_required(login_url='login')
@check_admin_and_superadmin
def tambah_user(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profil_form = UserAdminForm(request.POST, request.FILES)
        if user_form.is_valid() and profil_form.is_valid():
            user = user_form.save(commit=False)
            password = user_form.cleaned_data['password']
            user.set_password(password)
            user.save()
            
            group = Group.objects.get(name='user')
            user.groups.add(group)
            profil = profil_form.save(commit=False)
            profil.user = user
            profil.save()
            messages.info(request, 'Data berhasil disimpan')
            return redirect('user_register')
    user_form = UserRegistrationForm()
    profil = UserAdminForm()
    context = {
        'user_form': user_form,
        'profil_form': profil,
    }
    return render(request, 'account/tambah_user.html', context)

@login_required(login_url='login')
@check_admin_and_superadmin
def detail_user(request, pk):
    data_user = UserAdmin.objects.get(id=pk)
    context = {
        'data': data_user,
    }
    return render(request, 'account/detail_user.html', context)

@login_required(login_url='login')
@check_admin_and_superadmin
def edit_user(request, pk):
    user = UserAdmin.objects.get(id=pk)
    username = User.objects.get(id=user.user_id)
    user_form = UserRegistrationForm(instance=username)
    profil_form = UserAdminForm(instance=user)
    
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST, instance=username)
        profil_form = UserAdminForm(request.POST, request.FILES, instance=user)
        if user_form.is_valid() and profil_form.is_valid():
            user = user_form.save(commit=False)
            password = user_form.cleaned_data['password']
            user.set_password(password)
            user.save()
            
            group = Group.objects.get(name='user')
            user.groups.add(group)
            profil = profil_form.save(commit=False)
            profil.user = user
            profil.save()
            messages.info(request, 'Data berhasil diubah')
            return redirect('user_register')
    
    context = {
        'user_form': user_form,
        'profil_form': profil_form,
    }
    return render(request, 'account/ubah_user.html', context)

@login_required(login_url='login')
@check_superadmin
def admin_system(request):
    grup_user = User.objects.filter(groups__name = 'admin')
    profil = UserAdmin.objects.filter(user__in=list(grup_user)).order_by('-id')
    page = request.GET.get('page', 1)
    paginator = Paginator(profil, 10)
    allert = 'alert-success'
    
    jumlah_pegawai = Pegawai.objects.count()
    jumlah_kendaraan = Kendaraan.objects.count()
    context = {
        'jumlah_pegawai': jumlah_pegawai,
        'jumlah_kendaraan': jumlah_kendaraan,
        'allert': allert,
        'profil': profil,
    }
    return render(request, 'account/user_admin_register.html', context)

@login_required(login_url='login')
@check_superadmin
def detail_useradmin(request, pk):
    data_user = UserAdmin.objects.get(id=pk)
    context = {
        'data': data_user,
    }
    return render(request, 'account/detail_useradmin.html', context)

@login_required(login_url='login')
@check_superadmin
def edit_useradmin(request, pk):
    user = UserAdmin.objects.get(id=pk)
    username = User.objects.get(id=user.user_id)
    user_form = UserRegistrationForm(instance=username)
    profil_form = UserAdminForm(instance=user)
    
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST, instance=username)
        profil_form = UserAdminForm(request.POST, request.FILES, instance=user)
        if user_form.is_valid() and profil_form.is_valid():
            user = user_form.save(commit=False)
            password = user_form.cleaned_data['password']
            user.set_password(password)
            user.save()
            
            group = Group.objects.get(name='user')
            user.groups.add(group)
            profil = profil_form.save(commit=False)
            profil.user = user
            profil.save()
            messages.info(request, 'Data berhasil diubah')
            return redirect('admin_system')
    
    context = {
        'user_form': user_form,
        'profil_form': profil_form,
    }
    return render(request, 'account/ubah_useradmin.html', context)

@login_required(login_url='login')
def ubah_password(request):
    if request.method == 'POST':
        form = UbahPasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.info(request, 'Password berhasil diubah')
            return redirect('ubah_password')
        else:
            messages.error(request, 'Terjadi kesalahan.')
    else:
        form = UbahPasswordForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'account/ubah_password.html', context)