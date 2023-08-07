from django.urls import path
from . import views

urlpatterns = [
    path('gameOneOutOfTwenty/', views.gameOneOutOfTwenty, name='gameOneOutOfTwenty'),
    path('leaderboards/', views.leaderboard, name= 'leaderboards'),
    path('gameRules/', views.gameRules, name='gameRules'),
    path('gameResult/', views.gameResult, name='gameResult'),
]