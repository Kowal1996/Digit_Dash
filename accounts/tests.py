from django.test import TestCase
from .forms import ProfileForm
from datetime import datetime, date
from django.core.files.uploadedfile import SimpleUploadedFile

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

    