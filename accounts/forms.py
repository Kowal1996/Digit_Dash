from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile
from datetime import date

class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    username = forms.CharField(min_length=4)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name')

    def clean_email(self):
        return self.cleaned_data['email'].lower()
    
    def clean_first_name(self):
        return self.cleaned_data['first_name'].capitalize()


class ProfileForm(forms.ModelForm):
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        initial=date.today
    )
    class Meta:
        model = Profile
        fields = ('city', 'country', 'birth_date', 'pictures')

    def clean_city(self):
        return self.cleaned_data['city'].capitalize()
    
    def clean_country(self):
        return self.cleaned_data['country'].capitalize()

class EditProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ('city', 'country', 'pictures')

    def clean_city(self):
        return self.cleaned_data['city'].capitalize()
    
    def clean_country(self):
        return self.cleaned_data['country'].capitalize()
