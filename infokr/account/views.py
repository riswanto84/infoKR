from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import UserAdminForm
from django.contrib import messages


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