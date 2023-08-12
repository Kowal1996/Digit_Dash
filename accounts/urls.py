from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('loginUser/', views.loginUser, name='loginUser'),
    path('logoutUser/', views.logoutUser, name='logoutUser'),
    path('profileInformation/', views.profileInformation, name='profileInformation'),
    path('editProfile', views.editProfile, name='editProfile'),
    path('deleteUser/', views.deleteUser, name='deleteUser'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_change_form.html', success_url = '/password_change/done'), name='password_change', ),
    path('password_change/done', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='password_change_done'),
    path('registrationSuccessfull/', views.registrationSuccessfull, name='registrationSuccessfull'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]
