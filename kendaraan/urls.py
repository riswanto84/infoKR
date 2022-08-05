from django.urls import path
from . import views

urlpatterns = [
    path('kendaraan_app/', views.dashboard, name='dashboard'),
    path('kendaraan_app/pegawai', views.pegawai, name='pegawai'),
    path('kendaraan_app/data_kendaraan', views.kendaraan, name='kendaraan'),
    path('kendaraan_app/admin_system', views.admin_system, name='admin_system'),
]