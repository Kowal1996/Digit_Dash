from django.shortcuts import render
from .forms import MyRegistrationForm
# Create your views here.


def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'GET':
        userForm = MyRegistrationForm()
        profileForm = ProfileForm()
        return render(request, 'register.html', {'userForm': userForm, 'profileForm': profileForm})