from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile

class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    
    

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('city', 'country', 'birth_date', 'pictures')