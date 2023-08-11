from django.test import TestCase
from django.contrib.auth.models import User
from .forms import MyRegistrationForm, ProfileForm
from datetime import date
from django.core.files.uploadedfile import SimpleUploadedFile

# Create your tests here.
  
class MyRegistrationFormTestCase(TestCase): # pass
    def test_my_registartion_form_valid(self):
        form_data = {
            'username': 'UserTest',
            'email': 'test@test.pl',
            'password1': 'Test1234!',
            'password2': 'Test1234!',
            'first_name': 'TestName',
        }
        form = MyRegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())
        
    def test_my_registration_form_user_invalid(self):
        form_data = {
            'username': 'tes',
            'email': 'test@test.pl',
            'password1': 'Test1234!',
            'password2': 'Test1234!',
            'first_name': 'TestName',
        }
        form = MyRegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())

    
    def test_my_registartion_form_email_invalid(self):
        form_data = {
            'username': 'UserTest',
            'email': '@email',
            'password1': 'Test1234!',
            'password2': 'Test1234!',
            'first_name': 'TestName',
            }
        form = MyRegistrationForm(data=form_data)
        self.assertIn('email', form.errors)

    def test_my_registartion_form_password_invalid(self):
        form_data = {
            'username':'UserTest',
            'email': 'test@email',
            'password1': 'Test1234!',
            'password2': 'Test123',
            'first_name': 'TestName',
            }
        form = MyRegistrationForm(data=form_data)
        self.assertIn('password2', form.errors)

    def test_my_registartion_form_first_name_invalid(self):
        form_data = {
            'username':'UserTest',
            'email': 'test@email',
            'password1': 'Test1234!',
            'password2': 'Test1234!',
            'first_name': '',
            }
        form = MyRegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())


class LoginUserTestCase(TestCase): # pass
    def setUp(self):
        User.objects.create(username='UserTest', password='Test1234!')
        User.objects.create(username='UserTest1', password='Test12345!')

    def test_user_login(self):
        UserTest = User.objects.get(username='UserTest')
        UserTest1 = User.objects.get(username='UserTest1')
        self.assertEqual(UserTest.password, 'Test1234!')
        self.assertEqual(UserTest1.password, 'Test12345!')


class ProfileFormTestCase(TestCase):
    def test_profile_form_is_valid(self):       
        form_data = {
            'city': 'TestCity',
            'country': 'TestCountry',
            'birth_date': date.today(),
        }
        form = ProfileForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_profile_form_invalid_city(self):       
        form_data = {
            'city': '',
            'country': 'TestCountry',
            'birth_date': date.today(),
        }
        form = ProfileForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_profile_form_invalid_country(self):       
        form_data = {
            'city': 'TestCity',
            'country': '',
            'birth_date': date.today(),
        }
        form = ProfileForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_profile_form_invalid_date(self):       
        form_data = {
            'city': 'TestCity',
            'country': 'TestCountry',
            'birth_date': '1'
        }
        form = ProfileForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_profile_form_invalid_pictures(self):
        file = SimpleUploadedFile('testfile.txt', b"test text" , content_type='text/plain')       
        form_data = {
            'city': 'TestCity',
            'country': 'TestCountry',
            'birth_date': date.today(),
            'pictures': file,
        }
        form = ProfileForm(data=form_data, files={'pictures': file})
        self.assertFalse(form.is_valid())

