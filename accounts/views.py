from django.shortcuts import render, redirect
from .forms import MyRegistrationForm, ProfileForm
import re
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password 
from django.core.exceptions import ValidationError
from verify_email.email_handler import send_verification_email
from .models import Profile
from datetime import datetime
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def validate_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.fullmatch(regex, email):
        return True
    else:
        return False
    
def validate_first_name(first_name):
    regex = r'\b[A-Z][a-z]{0,49}\b'
    if re.fullmatch(regex,first_name):
        return True
    else:
        return False
    
def validate_city(city):
    regex = r'\b[A-Z][a-z]{0,100}\b'
    if re.fullmatch(regex,city):
        return True
    else:
        return False
    

def validate_country(country):
    regex = r'\b[A-Z][a-z]{0,100}\b'
    if re.fullmatch(regex,country):
        return True
    else:
        return False
    

def validate_age(birth_date):
    current_date = datetime.now()
    age = current_date.year - int(birth_date[0:4]) - ((current_date.month, current_date.day)<(int(birth_date[5:7]), int(birth_date[8:10])))
    if age >= 18:
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
        birth_date = request.POST.get('birth_date')

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
                        if not emailValid:
                            error = 'Email is not valid'
                        else:
                            cityValid = validate_city(city)
                            if not cityValid:
                                error = 'City is not valid'
                            else:
                                countryValid = validate_country(country)
                                if not countryValid:
                                    error = 'Country is not valid'
                                else:
                                    ageValid = validate_age(birth_date)
                                    if not ageValid:
                                        error = 'You are too young'
                                    else:
                                        user_form = MyRegistrationForm(request.POST)
                                        if user_form.is_valid():
                                            inactive_user = send_verification_email(request, user_form)
                                            profile_form = ProfileForm(request.POST)
                                            if profile_form.is_valid():
                                                profile = profile_form.save(commit=False)
                                                profile.owner = inactive_user
                                                profile.save()
                                                return redirect('home')                           
            else:
                error = 'Name is invalid'                
        else:
            error = 'Passwords did not match'   
        return render(request, 'register.html', {'userForm': userForm, 'profileForm': profileForm, 'error': error})
    

def loginUser(request):
    if request.method == 'GET':
        return render(request, 'loginUser.hmtl', {'form': AuthenticationForm()})
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate