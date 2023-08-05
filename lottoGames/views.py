from django.shortcuts import render, get_object_or_404
import random
from accounts.models import Profile
from .models import OneOutOfTwenty

# Create your views here.
def random_number():
    lucky_num = random.choice([i for i in range(1,21)])
    return lucky_num

def gameOneOutOfTwenty(request):
    user = get_object_or_404(Profile, owner=request.user)
    if request.method=='GET':
        return render(request, 'gameOneOutOfTwenty.html', {'user':user})
    else:
        pass 
