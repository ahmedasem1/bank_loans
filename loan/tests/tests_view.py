from django.urls import path, reverse, include, resolve
from django.test import SimpleTestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from rest_framework import status
from loan.models import User
from rest_framework.views import APIView
from loan.views import RegisterUserAPIView
from rest_framework.test import APIRequestFactory

# Using the standard RequestFactory API to create a form POST request


class CustomerAPIViewTests(APITestCase):
    def test_Post_User_is_resolved(self):
        factory = APIRequestFactory()
        request = factory.post(
            "/signup/",
            {
                "username": "aasem@gmail.com",
                "password": "Zaz16927",
                "password2": "Zaz16927",
                "type": "BP",
            },
        )

    def test_Post_Provider_is_resolved(self):
        factory = APIRequestFactory()
        request = factory.post(
            "/signup/",
            {
                "username": "aasem@gmail.com",
                "password": "Zaz16927",
                "password2": "Zaz16927",
                "type": "BP",
            },
        )

    def test_post_customer_authenticated(self):
        data = {
            "username": "aasem@gmail.com",
            "password": "Zaz16927",
            "password2": "Zaz16927",
            "type": "BP",
        }
        response = self.client.post("/signup/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
