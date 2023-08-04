from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('loginUser/', views.loginUser, name='loginUser'),
    path('logoutUser/', views.logoutUser, name='logoutUser'),
    path('profileInformation/', views.profileInformation, name='profileInformation'),
    path('editProfile', views.editProfile, name='editProfile'),
    path('deleteUser/,', views.deleteUser, name='deleteUser'),
]
