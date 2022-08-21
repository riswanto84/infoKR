from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('adminkr/', admin.site.urls),
    path('', include('account.urls')),

    # path kendaraan
    path('kendaraan/', include('kendaraan.urls'),)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)