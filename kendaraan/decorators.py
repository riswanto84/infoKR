from django.http import Http404

def check_superadmin(function):
    def wrapper(request, *args, **kwargs):
        if request.user.groups.filter(name="superadmin").exists():
            return function(request, *args, **kwargs)
        raise Http404
    return wrapper

def check_admin_and_superadmin(function):
    def wrapper(request, *args, **kwargs):
        if request.user.groups.filter(name__in=['superadmin', 'admin']).exists():
            return function(request, *args, **kwargs)
        raise Http404
    return wrapper