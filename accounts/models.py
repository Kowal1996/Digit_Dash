from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    city = models.CharField(max_length=200)
    pictures = models.ImageField(upload_to='profilePics', default='profilePics/blankUser.png')
    birth_date = models.DateField(blank=False)
    country = models.CharField(max_length=30)
    account_balance = models.PositiveBigIntegerField(default=0) 
    owner = models.OneToOneField(User,on_delete=models.CASCADE)

    def clean(self):
        self.city = self.city.capitalize()
        self.country = self.country.capitalize()

    def __str__(self):
        return f'{self.owner}'