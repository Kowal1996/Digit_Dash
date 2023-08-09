from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from .forms import MyRegistrationForm
from .models import Profile

# Create your tests here.
class MyRegistrationFormTestCase(TestCase): # pass
    def test_my_reagistartion_form_valid(self):
        form_data = {
            'username': 'Anna',
            'email': 'anna@wp.pl',
            'password1': 'Anna1234',
            'password2': 'Anna1234',
            'first_name': 'Anna',
            # 'city': 'Warszawa',
            # 'country': 'Polska',
            # 'birth_date': '03.04.1901'
        }
        form = MyRegistrationForm(data=form_data)
        self.assertTrue(form.is_valid)


# class ProfileModelTest(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         # Set up non-modified objects used by all test methods
#         Profile.objects.create(city='Warszawa', country='Poland', birth_day='03.06.1990')

#     def test_city_max_length(self):
#         profile = Profile.objects.get(id=1)
#         max_length = profile._meta.get_field('city').max_length
#         self.assertEqual(max_length,200)

#     def test_country_max_length(self):
#         profile = Profile.objects.get(id=1)
#         max_length = profile._meta.get_field('country').max_length # _meta attribute to get an instance of the field and use that to query for the additional information.
#         self.assertEqual(max_length,30)

class HomepageLeaderboarsPageTestsCase(TestCase):
    def test_url_exists_at_correct_location(self):
        url = reverse('leaderboards')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        url = reverse('leaderboards')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'leaderboard.html')