from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile
from datetime import date

class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    
    

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name')


class ProfileForm(forms.ModelForm):
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        initial=date.today
    )
    class Meta:
        model = Profile
        fields = ('city', 'country', 'birth_date', 'pictures')


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('city', 'country', 'pictures')