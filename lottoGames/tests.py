from django.test import TestCase
from django.contrib.auth.models import User
from accounts.models import Profile
from .models import OneOutOfTwenty
import datetime


class GamePlayedTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username= 'Testuser',
            email='test@test.pl',
            password = 'Test1234!',
            first_name='Testname'
            )
        self.profile = Profile.objects.create(
            city="Testcity",
            country="Testcountry",
            birth_date = "1990-01-01",
            owner=self.user
        )
        def create_game(self):
            game = OneOutOfTwenty.objects.create(
            owner = self.profile,
            user_score = 10,
            luckyNumber = 10
        )
            
            self.assertTrue(game.luckyNumber, 10)
            self.assertTrue(game.user_score, 10)
            self.assertTrue(game.owner, self.profile)
            self.assertTrue(game.gameDate, datetime.datetime.now())


class UserGamesTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username= 'Testuser',
            email='test@test.pl',
            password = 'Test1234!',
            first_name='Testname'
            )
        self.profile = Profile.objects.create(
            city="Testcity",
            country="Testcountry",
            birth_date = "1990-01-01",
            owner=self.user
        )
    def test_user_games(self):
        game1 = OneOutOfTwenty.objects.create(
            owner = self.profile,
            user_score = 8,
            luckyNumber = 7
        )
        self.profile.account_balance += game1.user_score
        game2 = OneOutOfTwenty.objects.create(
            owner = self.profile,
            user_score = 4,
            luckyNumber = 8
        )
        self.profile.account_balance += game2.user_score
        self.assertTrue(game1.owner, self.profile)
        self.assertTrue(game2.owner, self.profile)
        self.assertTrue(self.profile.account_balance, 12)
