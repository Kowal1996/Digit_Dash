from django.shortcuts import render
from .forms import MyRegistrationForm
# Create your views here.


def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'GET':
        form = MyRegistrationForm()
        return render(request, 'register.html', {'form': form})