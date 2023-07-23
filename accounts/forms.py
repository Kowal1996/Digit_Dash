from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    birth_date = forms.DateField()
    country = forms.CharField()
    account_balance = forms.DecimalField()
    creation_date = forms.DateField(auto_now_add=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'birth_date', 'country', 'account_balance')