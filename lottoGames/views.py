from django.shortcuts import render, get_object_or_404
import random
from accounts.models import Profile

from .models import OneOutOfTwenty
from django.core.exceptions import ValidationError

# Create your views here.
def random_number():
    lucky_num = random.choice([i for i in range(1,21)])
    return lucky_num
      
def gameOneOutOfTwenty(request):
    user = get_object_or_404(Profile, owner=request.user)    
    if 'lucky_number' not in request.session:
        request.session['lucky_number'] = random_number() 
    lucky_num = request.session['lucky_number']
    if request.method == 'POST':
        if 'score' not in request.session:
            request.session['score'] = 10
        score = request.session['score'] 
        
        tries = 0     
        for _ in range (10): 
            user_number = request.POST.get('user_number') 
            if tries <= 10:
                if user_number.isdigit():
                    user_number = int(user_number)
                    if 1 <= user_number <= 20: 
                        if user_number < lucky_num:
                            score -= 1
                            message = 'Your number is too low'
                            tries += 1
                            return render(request, 'gameOneOutOfTwenty.html', {'message': message, 'score':score, 'user':user, 'tries': tries})
                        elif user_number > lucky_num:
                            score -= 1
                            message = 'Your number is too high'
                            tries +=1
                            return render(request, 'gameOneOutOfTwenty.html', {'message': message, 'score':score, 'user':user, 'tries': tries})
                        else:
                            message = 'Good job! You pick correct number!'
                            game = OneOutOfTwenty.objects.create(
                                owner = user,
                                luckyNumber = lucky_num,
                                user_score = score
                            )
                            game.save()
                            user.account_balance += score
                            user.save()
                            if 'lucky_number' in request.session:
                                del request.session['lucky_number']
                            return render(request, 'gameOneOutOfTwenty.html', {'message': message, 'score':score, 'user':user, 'tries': tries})
            else:
                message = 'You used all your chances'
                score = 0
                game = OneOutOfTwenty.objects.create(
                            owner = user,
                            luckyNumber = lucky_num,
                            user_score = score
                        )
                game.save()
                user.account_balance += score
                user.save()
                if 'lucky_number' in request.session:
                    del request.session['lucky_number']
                return render(request, 'gameOneOutOfTwenty.html', {'message': message, 'score':score, 'user':user})
    else:
        return render(request, 'gameOneOutOfTwenty.html', {'lucky_number': lucky_num})

