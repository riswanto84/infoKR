from django.urls import path
from . import views

urlpatterns = [
    path('kendaraan/', views.dashboard, name='dashboard'),
    
]