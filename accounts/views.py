from django.shortcuts import render, redirect, get_object_or_404
from .forms import MyRegistrationForm, ProfileForm, EditProfileForm
import re
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password 
from django.core.exceptions import ValidationError
from verify_email.email_handler import send_verification_email
from .models import Profile
from datetime import datetime
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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
                                            profile_form = ProfileForm(request.POST, request.FILES)
                                            if profile_form.is_valid():
                                                profile = profile_form.save(commit=False)
                                                profile.owner = inactive_user
                                                profile.save()
                                                return redirect('registrationSuccessfull')                           
            else:
                error = 'Name is invalid'                
        else:
            error = 'Passwords did not match'   
        return render(request, 'register.html', {'userForm': userForm, 'profileForm': profileForm, 'error': error})
    

def loginUser(request):
    if request.method == 'GET':
        return render(request, 'loginUser.html', {'form': AuthenticationForm()})
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error = 'Wrong username or password'
            return render(request, 'loginUser.html', {'form': AuthenticationForm(), 'error':error})

@login_required
def logoutUser(request):
    logout(request)
    return render(request, 'logoutUser.html')

@login_required
def profileInformation(request):
    profile_info = get_object_or_404(Profile, owner=request.user)
    # user_info = get_object_or_404(User, user=request.user)
    return render(request, 'profileInformation.html', {'profile_info': profile_info})

@login_required
def editProfile(request):
    profile_info = get_object_or_404(Profile, owner=request.user)
    if request.method == 'GET':
        edit_profile_info = EditProfileForm(instance=profile_info)
        return render(request, 'editProfile.html', {'profile_info':profile_info, 'edit_profile_info': edit_profile_info})
    else:
        new_coutry = request.POST.get('country')
        new_city = request.POST.get('city')
        new_city_valid = validate_city(new_city)
        if not new_city_valid:
            error = 'City is not valid'
        else:
            new_country_valid = validate_country(new_coutry)
            if not new_country_valid:
                error ='Country is not valid'
            else:
                edit_profile_info = EditProfileForm(request.POST, request.FILES, instance=profile_info)
                if edit_profile_info.is_valid():
                    edit_profile_info.save()
                    return redirect('profileInformation')
                else:
                    error = 'Something gone wrong, try again!'
        return render(request, 'editProfile.html', {'profile_info':profile_info, 'edit_profile_info': edit_profile_info, 'error': error})

@login_required
def deleteUser(request):
    user = User.objects.filter(username=request.user)
    user.delete()
    logout(request)
    message = 'Your account was deleted'
    return render(request, 'home.html', {'message':message})


def registrationSuccessfull(request):
    if request.method == 'GET':
        message = 'Your account has been successfully created, confirm your registration by clicking on the link in the email'
        return render(request, 'registrationSuccessfull.html', {'message':message})

    