from django.shortcuts import render
from .forms import MyRegistrationForm, ProfileForm
import re
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password 
from django.core.exceptions import ValidationError
# Create your views here.

def validate_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.fullmatch(regex, email):
        return True
    else:
        return False


def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'GET':
        userForm = MyRegistrationForm()
        profileForm = ProfileForm()
        return render(request, 'register.html', {'userForm': userForm, 'profileForm': profileForm})
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 == password2:
            usernameTaken = User.objects.filter(username=username).exists()
            emailTaken = User.objects.filter(email=email).exists()
            if usernameTaken:
                error = 'Username is already taken'
            if emailTaken:
                error = 'Email is already taken'
            if not usernameTaken and not emailTaken:
                try:
                    validate_password(password1)
                except ValidationError as e:
                    return render(request, 'register.html', {'userForm': userForm, 'profileForm': profileForm, 'passwordError': e.messages})    
                else:
                    emailValid = validate_email(email)
                    if emailValid:
                        pass
                    else:
                        error = 'Email is not valid'
        else:
            error = 'Passwords did not match'
        return render(request, 'register.html', {'userForm': userForm, 'profileForm': profileForm, 'error': error})