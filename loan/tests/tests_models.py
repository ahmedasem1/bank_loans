from rest_framework.test import APITestCase, APIRequestFactory

# from .views import PostListCreateView
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model


User = get_user_model()


class PostListCreateTestCase(APITestCase):
    def setUp(self):
        self.url = reverse("viewloan")

    def authenticate(self):
        self.client.post(
            reverse("signup"),
            {
                "username": "aasem@gmail.com",
                "password": "Zaz16927",
                "password2": "Zaz16927",
                "type": "BP",
            },
        )

        response = self.client.post(
            reverse("login"),
            {
                "email": "aasem@gmail.com",
                "password": "Zaz16927",
            },
        )

        # print(response.data)

        # token = response.data["tokens"]["access"]

        # self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 0)
        self.assertEqual(response.data["results"], [])
        response = self.client.post(
            reverse("personnelloan"),
            {
                "min_amount": 1500,
                "max_amount":1000,
                "max_duration":1000,
                "interest_rate":1000,
                "provider":1,
                "coustmer":2,

                
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_Bad_Request)



    

    def authenticate_1(self):
        self.client.post(
            reverse("signup"),
            {
                "username": "aasem@gmail.com",
                "password": "Zaz16927",
                "password2": "Zaz16927",
                "type": "PR",
            },
        )

        response = self.client.post(
            reverse("login"),
            {
                "email": "aasem@gmail.com",
                "password": "Zaz16927",
            },
        )

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 0)
        self.assertEqual(response.data["results"], [])    

