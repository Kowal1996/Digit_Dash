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
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('registrationSuccessfull/', views.registrationSuccessfull, name='registrationSuccessfull'),
]
