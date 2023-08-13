from django.test import TestCase
from django.contrib.auth.models import User
from .forms import MyRegistrationForm, ProfileForm, EditProfileForm
from datetime import date
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Profile
from django.urls import reverse
from django.test import Client


class MyRegistrationFormTestCase(TestCase):
    def test_my_registartion_form_valid(self):
        form_data = {
            'username': 'UserTest',
            'email': 'test@test.pl',
            'password1': 'Test1234!',
            'password2': 'Test1234!',
            'first_name': 'Testname',
        }
        form = MyRegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())
        
    def test_my_registration_form_username_invalid(self):
        form_data = {
            'username': '',
            'email': 'test@test.pl',
            'password1': 'Test1234!',
            'password2': 'Test1234!',
            'first_name': 'Testname',
        }
        form = MyRegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())

    
    def test_my_registartion_form_email_invalid(self):
        form_data = {
            'username': 'UserTest',
            'email': '@email',
            'password1': 'Test1234!',
            'password2': 'Test1234!',
            'first_name': 'Testname',
            }
        form = MyRegistrationForm(data=form_data)
        self.assertIn('email', form.errors)

    def test_my_registartion_form_password_invalid(self):
        form_data = {
            'username':'UserTest',
            'email': 'test@email',
            'password1': 'Test1234!',
            'password2': 'Test123',
            'first_name': 'Testname',
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


class LoginUserTestCase(TestCase):
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
            'city': 'Testcity',
            'country': 'Testcountry',
            'birth_date': date.today(),
        }
        form = ProfileForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_profile_form_invalid_city(self):       
        form_data = {
            'city': '',
            'country': 'Testcountry',
            'birth_date': date.today(),
        }
        form = ProfileForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_profile_form_invalid_country(self):       
        form_data = {
            'city': 'Testcity',
            'country': '',
            'birth_date': date.today(),
        }
        form = ProfileForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_profile_form_invalid_date(self):       
        form_data = {
            'city': 'Testcity',
            'country': 'Testcountry',
            'birth_date': '1'
        }
        form = ProfileForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_profile_form_invalid_pictures(self):
        file = SimpleUploadedFile('testfile.txt', b"test text" , content_type='text/plain')       
        form_data = {
            'city': 'Testcity',
            'country': 'Testcountry',
            'birth_date': date.today(),
            'pictures': file,
        }
        form = ProfileForm(data=form_data, files={'pictures': file})
        self.assertFalse(form.is_valid())


class EditProfileFormTestCase(TestCase):
    @classmethod
    def setUp(cls):
        user = User.objects.create(
            username = 'TestUser',
            email = 'test@test.pl',
            password = 'Test1234!',
            first_name = 'Testname'
        )
        profile = Profile.objects.create(
            city='Testcity',
            country='Testcountry',
            pictures = 'profilePics/blankUser.png',
            birth_date = '1995-01-01',
            account_balance = 0,
            owner = user
        )
    def test_user_field(self):
        user = User.objects.get(id=1)
        self.assertEqual(user.username, 'TestUser') 
        self.assertEqual(user.password, 'Test1234!')
        self.assertEqual(user.email, 'test@test.pl')
        self.assertEqual(user.first_name, 'Testname')

    def test_profile_field(self):
        user = User.objects.get(id=1)
        profile = Profile.objects.get(id=1)
        self.assertEqual(profile.city, 'Testcity')
        self.assertEqual(profile.country, 'Testcountry')
        self.assertEqual(profile.birth_date, date(1995,1,1))
        self.assertEqual(profile.account_balance, 0)
        self.assertEqual(profile.pictures, 'profilePics/blankUser.png')
        self.assertEqual(profile.owner, user)


    def test_edit_profile_form_valid(self):
        profile_to_edit = Profile.objects.get(id=1)
        with open('media/testPics/testPic.png', 'rb') as img:
            pic = img.read()

        image = SimpleUploadedFile(
            'testsPic.png',
            pic,
            content_type='image/jpeg'
        )
        form_data = {
            'city': 'Testcityone',
            'country': 'Testcountryone',
            'pictures': image,
        }
        form = EditProfileForm(instance=profile_to_edit, data=form_data, files={'pictures':image})
        self.assertTrue(form.is_valid())
        self.assertEqual(profile_to_edit.city, 'Testcityone')
        self.assertEqual(profile_to_edit.country, 'Testcountryone')
        self.assertEqual(profile_to_edit.pictures, image)

    def test_edit_profile_form_invalid_city(self):
        profile_to_edit = Profile.objects.get(id=1)
        with open('media/testPics/testPic.png', 'rb') as img:
            pic = img.read()

        image = SimpleUploadedFile(
            'testsPic.png',
            pic,
            content_type='image/jpeg'
        )
        form_data = {
            'city': '',
            'country': 'Testcountryone',
            'pictures': image,
        }
        form = EditProfileForm(instance=profile_to_edit, data=form_data, files={'pictures':image})
        self.assertFalse(form.is_valid())

    def test_edit_profile_form_invalid_country(self):
        profile_to_edit = Profile.objects.get(id=1)
        with open('media/testPics/testPic.png', 'rb') as img:
            pic = img.read()

        image = SimpleUploadedFile(
            'testsPic.png',
            pic,
            content_type='image/jpeg'
        )
        form_data = {
            'city': 'Testcityone',
            'country': '',
            'pictures': image,
        }
        form = EditProfileForm(instance=profile_to_edit, data=form_data, files={'pictures':image})
        self.assertFalse(form.is_valid())

    def test_edit_profile_form_invalid_picture(self):
        profile_to_edit = Profile.objects.get(id=1)
        file = SimpleUploadedFile('testfile.txt', b"test text" , content_type='text/plain')
        form_data = {
            'city': 'Testcityone',
            'country': '',
            'pictures': file,
        }
        form = EditProfileForm(instance=profile_to_edit, data=form_data, files={'pictures':file})
        self.assertFalse(form.is_valid())

class UserDeletionTestCase(TestCase):
    def test_user_deletion(self):
        user = User.objects.create(
            username = 'TestUser',
            password= 'Test1234!',
            email= 'test@test.pl',
            first_name = 'Testname'
        )
        user.delete()

        user_exists = User.objects.filter(
            username = 'TestUser',
            # password= 'Test1234!',
        ).exists()
        self.assertFalse(user_exists)

class UserLogoutTestCase(TestCase):
    def test_logout_user(self):
        user = User.objects.create(
            username = 'TestUser',
            password= 'Test1234!',
        )
        self.client.login(
            username = 'TestUser',
            password= 'Test1234!'
        )
        url = reverse('logoutUser')
        response = self.client.post(url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.wsgi_request.user.is_authenticated)

class LeaderboarsPageTestsCase(TestCase):
    def test_url_exists_at_correct_location(self):
        url = reverse('leaderboards')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        url = reverse('leaderboards')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'leaderboard.html')

    def test_template_content(self):
        url = reverse('leaderboards')
        response = self.client.get(url)
        self.assertContains(response, 'Leaderboards')
        self.assertNotContains(response, 'Not on the page')

class LoginUserPageTestCase(TestCase):
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
        self.assertContains(response, 'Log in')
        self.assertNotContains(response, 'Not on the page')

class RegistrationPageTestCase(TestCase):
    def test_url_exists_at_correct_location(self):
        url = reverse('register')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_template_name_core(self):
        url = reverse('register')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'register.html')

    def test_template_content(self):
        url = reverse('register')
        response = self.client.get(url)
        self.assertContains(response,'Create your account')
        self.assertNotContains(response, 'Not on the page')
