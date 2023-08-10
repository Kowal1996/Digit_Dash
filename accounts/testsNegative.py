from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import Client

from .forms import MyRegistrationForm
from .models import Profile

# Create your tests here.
# class MyRegistrationFormTestCase(TestCase): # pass
#     def test_my_registartion_form_valid(self):
#         form_data = {
#             'username': 'Anna',
#             'email': 'maill', # wrong email
#             'password1': 'Anna1234',
#             'password2': 'Anna1234',
#             'first_name': 'Anna',
#             # 'city': 'Warszawa',
#             # 'country': 'Polska',
#             # 'birth_date': '03.04.1901'
#         }
#         form = MyRegistrationForm(data=form_data)
#         self.assertTrue(form.is_valid())

    # def test_my_registartion_form_valid1(self):
    #     form_data = {
    #         'username': 'Anna',
    #         'email': 'anna@wp.pl',
    #         'password1': 'Anna1234',
    #         'password2': 'hyoh', # wrong password 2 
    #         'first_name': 'Anna',
    #         # 'city': 'Warszawa',
    #         # 'country': 'Polska',
    #         # 'birth_date': '03.04.1901'
    #     }
    #     form = MyRegistrationForm(data=form_data)
    #     self.assertTrue(form.is_valid())   

    # def test_my_registartion_form_valid(self):
    #     form_data = {
    #         'username': 'anna', 
    #         'email': ' anna@wp.pl',
    #         'password1': 'Anna1234', # with space 
    #         'password2': 'Anna1234',
    #         'first_name': '', # blank 
    #         # 'city': 'Warszawa',
    #         # 'country': 'Polska',
    #         # 'birth_date': '03.04.1901'
    #     }
    #     form = MyRegistrationForm(data=form_data)
    #     self.assertTrue(form.is_valid())

    # def test_my_registration_form_invalid(self):
    #     form_data = {
    #         'username': '',
    #         'email': '@email',
    #         'password1': '123',
    #         'password2': '1234'
    #     }
    #     form = MyRegistrationForm(data=form_data)
    #     self.assertFalse(form.is_valid())
    #     self.assertIn('email', form.errors)
    #     self.assertIn('password2', form.errors)


class ProfileModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        user = User.objects.create(username='Anna',
                                   email='anna@wp.pl',
                                   password='Anna1234!')
        
        cls.profile = Profile.objects.create(city='Chojnice',
                               pictures='profilePics/blankUser.png',
                               birth_date='1990-06-03',
                               country='Poland',
                               account_balance='0',
                               owner=user)

    def test_city_max_length(self):
        profile = Profile.objects.get(id=1)
        max_length = profile._meta.get_field('city').max_length
        self.assertEqual(max_length,200)

    def test_country_max_length(self):
        profile = Profile.objects.get(id=1)
        max_length = profile._meta.get_field('country').max_length # _meta attribute to get an instance of the field and use that to query for the additional information.
        self.assertEqual(max_length,30)

    def test_profile_field(self):
        self.assertEqual(self.profile.city, 'Chojnice')
        self.assertEqual(self.profile.pictures, 'profilePics/blankUser.png')
        self.assertEqual(self.profile.birth_date, '1990-06-03')
        self.assertEqual(self.profile.country, 'Poland')
        self.assertEqual(self.profile.account_balance, '0')
        # self.assertEqual(self.profile.owner, user) # do sparwdzenia

class LeaderboarsPageTestsCase(TestCase):
    def test_url_exists_at_correct_location(self):
        url = reverse('leaderboards')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        url = reverse('leaderboards')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'leaderboard.html')

    # def test_template_content(self):
    #     url = reverse('leadboards')
    #     response = self.client.get(url)
    #     self.assertContains(response,)
    #     self.assertNotContains(response, 'Not on the page')

class LoginUserMainTestCase(TestCase):
    def test_url_exists_at_correct_location(self):
        url = reverse('loginUser')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        url = reverse('loginUser')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'loginUser.html')

    def test_template_content(self):
        url = reverse('loginUser')
        response = self.client.get(url)
        self.assertContains(response, '<h1>LOGIN</h1>')
        self.assertNotContains(response, 'Not on the page')

class RegistrationMainTestCase(TestCase):
    def test_url_exists_at_correct_location(self):
        url = reverse('register')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_template_name_core(self):
        url = reverse('register')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'register.html')

    # def test_template_content(self):
    #     url = reverse('register')
    #     response = self.client.get(url)
    #     self.assertContains(response, )
    #     self.assertNotContains(response, 'Not on the page')

class LoginUserTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='Anna', password="Anna1234")

    def test_login_user(self):
        self.client.login(username='Anna', password="Anna1234")
        response = self.client.get(reverse('loginUser'))
        self.assertEqual(response.status_code, 200)




class EditMainTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        user = User.objects.create(username='Anna',
                                   email='anna@wp.pl',
                                   password='Anna1234!')
        
        cls.profile = Profile.objects.create(city='Chojnice',
                               pictures='profilePics/blankUser.png',
                               birth_date='1990-06-03',
                               country='Poland',
                               account_balance='0',
                               owner=user)
        
    def setUp(self):
        c = Client()

    def test_logged_in_uses_correct_template(self):
        c.login(username="Anna", password="Anna1234!")
        response = c.get("/editProfile/")
        self.assertEqual(response.status_code, 302)

    def test_url_exists_at_correct_location(self):
        login = self.client.login(username='Anna', password='Anna1234!')
        url = reverse('editProfile')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_template_name_core(self):
        login = self.client.login(username='Anna', password='Anna1234!')
        url = reverse('editProfile')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'editProfile.html')

    # def test_template_content(self):
    #     url = reverse('register')
    #     response = self.client.get(url)
    #     self.assertContains(response, )
    #     self.assertNotContains(response, 'Not on the page')