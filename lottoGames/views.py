from django.shortcuts import render, get_object_or_404, redirect
import random
from accounts.models import Profile
from .models import OneOutOfTwenty
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def random_number():
    lucky_num = random.choice([i for i in range(1,21)])
    return lucky_num
    

@login_required      
def gameOneOutOfTwenty(request):
    profile = get_object_or_404(Profile, owner=request.user)
    user = get_object_or_404(User, username=request.user)    
    if 'lucky_number' not in request.session:
        request.session['lucky_number'] = random_number() 
    lucky_num = request.session['lucky_number'] 
    if 'score' not in request.session:
        request.session['score'] = 10
    score = request.session['score']
    if 'tries_count' not in request.session:
        request.session['tries_count'] = 0
    tries_count = request.session['tries_count'] 
    if request.method == 'POST': 
        if tries_count != 9:
            user_number = request.POST.get('user_number')
            if user_number.isdigit():
                user_number = int(user_number)
                if 1 <= user_number <= 20: 
                    if user_number < lucky_num:
                        score -= 1
                        tries_count += 1
                        request.session['tries_count'] = tries_count
                        request.session['score'] = score  
                        message = 'Your number is too low'
                    elif user_number > lucky_num:
                        score -= 1
                        tries_count += 1
                        request.session['tries_count'] = tries_count
                        request.session['score'] = score  
                        message = 'Your number is too high'
                    else:
                        request.session['score'] = score  
                        # message = 'Good job! You picked the correct number!'
                        game = OneOutOfTwenty.objects.create(
                            owner=profile,
                            luckyNumber=lucky_num,
                            user_score=score
                        )
                        game.save()
                        profile.account_balance += score
                        profile.save()
                        if 'lucky_number' in request.session:
                            del request.session['lucky_number']
                        if 'score' in request.session:
                            del request.session['score']
                        if 'tries_count' in request.session:
                            del request.session['tries_count']
                        return redirect('gameResult')  
                else:
                    message = 'Number should be between 1 and 20'
            else:
                message = 'Please input a number between 1 and 20'          
        else:
            user_number = request.POST.get('user_number')
            if user_number.isdigit():
                user_number = int(user_number)
                if user_number != lucky_num:
                    # message = 'You used all your chances'
                    score = 0
                    game = OneOutOfTwenty.objects.create(
                                owner=profile,
                                luckyNumber=lucky_num,
                                user_score=score
                            )
                    game.save()
                    profile.account_balance += score
                    profile.save()
                    if 'lucky_number' in request.session:
                        del request.session['lucky_number']
                    if 'score' in request.session:
                        del request.session['score']
                    if 'tries_count' in request.session:
                        del request.session['tries_count']
                    return redirect('gameResult')
                else:
                    request.session['score'] = score  
                    # message = 'Good job! You picked the correct number!'
                    game = OneOutOfTwenty.objects.create(
                        owner=profile,
                        luckyNumber=lucky_num,
                        user_score=score
                    )
                    game.save()
                    profile.account_balance += score
                    profile.save()
                    if 'lucky_number' in request.session:
                        del request.session['lucky_number']
                    if 'score' in request.session:
                        del request.session['score']
                    if 'tries_count' in request.session:
                        del request.session['tries_count']
                    return redirect('gameResult')            
    else:
        if 'lucky_number' in request.session:
            del request.session['lucky_number']
            request.session['lucky_number'] = random_number()
            lucky_num = request.session['lucky_number']
        if 'score' in request.session:
            del request.session['score']
            request.session['score'] = 10
        score = request.session['score']
        if 'tries_count' in request.session:
            del request.session['tries_count']
            request.session['tries_count'] = 0
        tries_count = request.session['tries_count']
        return render(request, 'gameOneOutOfTwenty.html', {'lucky_number': lucky_num, 'user':user, 'score':score, 'tries': tries_count})
    
    return render(request, 'gameOneOutOfTwenty.html', {'message': message, 'score': score, 'tries': tries_count, 'user':user})


def leaderboard(request):
    if request.method == 'GET':
        highest_score = Profile.objects.order_by('-account_balance')
        return render(request,'leaderboard.html', {'highest_score':highest_score})
    

@login_required    
def gameRules(request):
    return render(request, 'gameRules.html')


@login_required  
def gameResult(request):
    if request.method == 'GET':
        owner = get_object_or_404(Profile, owner=request.user)
        game = OneOutOfTwenty.objects.filter(owner=owner).order_by('-gameDate').first()
        points = int(game.user_score)
        if points == 10:
            feedback = 'You are amazing. Good job!'
        elif points >= 7:
            feedback = 'Good job!'
        elif points >= 4:
            feedback = 'Try harder. You can do it better!' 
        elif points >=1:
            feedback = 'You have to work on your memory! '
        else:
            feedback = 'You lost because you used all your chances!'
        return render(request, 'gameResult.html', {'game':game, 'owner':owner, 'feedback':feedback})


@login_required      
def userGames(request):
    if request.method == 'GET':
        owner = get_object_or_404(Profile, owner=request.user)
        games = OneOutOfTwenty.objects.filter(owner=owner).order_by('-gameDate')
        numOfGames = len(games)
        paginator = Paginator(games, 5)
        page = request.GET.get('page')
        try:
            games_on_page = paginator.page(page)
        except PageNotAnInteger:
            games_on_page = paginator.page(1)
        except EmptyPage:
            games_on_page = paginator.page(paginator.num_pages)
        start_index = (games_on_page.number - 1) * paginator.per_page + 1
        return render(request, 'userGames.html',{'games_on_page':games_on_page, 'numOfGames':numOfGames, 'page':page, 'start_index':start_index})
