from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # post views
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('account_setting', views.account_setting, name='account_setting'),

    # reset password urls
    path('password_reset/', auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    
    # admin system
    path('account/user_register', views.user_register, name='user_register'),
    path('account/tambah_user', views.tambah_user, name='tambah_user'),
    path('account/admin_system', views.admin_system, name='admin_system'),
    path('account/detail_user/<str:pk>', views.detail_user, name='detail_user'),
    path('account/edit_user/<str:pk>', views.edit_user, name='edit_user'),
    path('account/detail_useradmin/<str:pk>', views.detail_useradmin, name='detail_useradmin'),
    path('account/edit_useradmin/<str:pk>', views.edit_useradmin, name='edit_useradmin'),
    path('account/ubah_password', views.ubah_password, name='ubah_password'),
]