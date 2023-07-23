from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    city = models.CharField(max_length=200)
    pictures = models.ImageField(upload_to='profilePics', default='blankUser.png')
    name = models.TextField(blank=True)
    surname = models.TextField(blank=True)
    owner = models.OneToOneField(User,on_delete=models.CASCADE) # Creating many to many relationship with User model

    def __str__(self):
        return f'{self.owner}'