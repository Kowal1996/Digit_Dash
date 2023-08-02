from django.shortcuts import render, redirect
from .forms import MyRegistrationForm, ProfileForm
import re
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password 
from django.core.exceptions import ValidationError
from verify_email.email_handler import send_verification_email
# Create your views here.

def validate_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.fullmatch(regex, email):
        return True
    else:
        return False
    
def validate_first_name(first_name):
    regex = r'\b[A-Z][a-zA-Z]{0,49}\b'
    if re.fullmatch(regex,first_name):
        return True
    else:
        return False
    
def validate_city(city):
    regex = r'\b[A-Z][a-zA-Z]{0,100}\b'
    if re.fullmatch(regex,city):
        return True
    else:
        return False
    

def validate_country(country):
    regex = r'\b[A-Z][a-zA-Z]{0,100}\b'
    if re.fullmatch(regex,country):
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
        userForm = MyRegistrationForm()
        profileForm = ProfileForm()
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        first_name = request.POST.get('first_name')
        city = request.POST.get('city')
        country = request.POST.get('country')

        if password1 == password2:
            firstNameValid = validate_first_name(first_name)
            if firstNameValid:
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
                                userForm = MyRegistrationForm(request.POST)
                                cityValid = validate_city(city)
                                if cityValid:
                                    countryValid = validate_country(country)
                                    if countryValid:
                                        profileForm = ProfileForm(request.POST, request.FILES)
                                        if userForm.is_valid() and profileForm.is_valid():
                                            inactive_user = send_verification_email(request, userForm)
                                            return redirect('home')
                                    else:
                                        error = 'Country is not valid'
                                else:
                                    error = 'City is not valid'
                            else:
                                error = 'Email is not valid'
            else:
                error = 'Name is invalid'                
        else:
            error = 'Passwords did not match'   
        return render(request, 'register.html', {'userForm': userForm, 'profileForm': profileForm, 'error': error})