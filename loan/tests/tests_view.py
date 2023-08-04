from django.urls import path, reverse, include, resolve
from django.test import SimpleTestCase
from loan.views import *
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from rest_framework import status
from loan.models import User,Provider
from django.test.runner import DiscoverRunner

from rest_framework.views import APIView



# testing weather the object created or not
class ApiUrlsTests(SimpleTestCase,DiscoverRunner):
    
    databases = '__all__'
    url = reverse("signup")

    def test_signup_is_resolved(self):
        user = User.objects.create(
        username='apsa1assp@gmail.com',
            type='BP',     
            password="Zaz16827"
        )
        user.set_password('Zaz16927')
        user.save()
        print('000000000000')

        print(user)
        self.assertEquals(user.username, "apsa1assp@gmail.com")   
        