from django.urls import path
from . import views

urlpatterns = [
    # url pegawai
    path('kendaraan_app/pegawai', views.pegawai, name='pegawai'),
    path('kendaraan_app/tambah_pegawai', views.tambah_pegawai, name='tambah_pegawai'),
    path('kendaraan_app/detail_pegawai/<str:pk>', views.detail_pegawai, name='detail_pegawai'),
    path('kendaraan_app/ubah_pegawai/<str:pk>', views.ubah_pegawai, name='ubah_pegawai'),
    path('kendaraan_app/hapus_pegawai/<str:pk>', views.hapus_pegawai, name='hapus_pegawai'),
    
    # url kendaraan
    path('kendaraan_app/', views.dashboard, name='dashboard'),
    path('kendaraan_app/detail_kendaraan/<str:pk>', views.detail_kendaraan, name='detail_kendaraan'),
    path('kendaraan_app/data_kendaraan', views.kendaraan, name='kendaraan'),
    path('kendaraan_app/tambah_kendaraan', views.tambah_kendaraan, name='tambah_kendaraan'),
    path('kendaraan_app/hapus_kendaraan/<str:pk>', views.hapus_kendaraan, name='hapus_kendaraan'),
    path('kendaraan_app/detail_kendaraan_admin/<str:pk>', views.detail_kendaraan_admin, name='detail_kendaraan_admin'),
    path('kendaraan_app/edit_kendaraan/<str:pk>', views.edit_kendaraan, name='edit_kendaraan'),
    
    # admin system
    path('kendaraan_app/admin_system', views.admin_system, name='admin_system'),
    
]