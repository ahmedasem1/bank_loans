from django.urls import resolve, reverse
from loan.views import *
from django.test import SimpleTestCase


# testing weather the right url handeld by the right view function
class TestUrls(SimpleTestCase):
    def test_signup_is_resolved(self):
        url = reverse("signup")
        self.assertEquals(resolve(url).func.view_class, RegisterUserAPIView)

    def test_registerprovider_is_resolved(self):
        url = reverse("registerprovider", args=["0f4ea1df-f966-440a-8db6-dcfe2be071d1"])
        self.assertEquals(resolve(url).func.view_class, RegisterProviderAPIView)

    def test_registercustomer_is_resolved(self):
        url = reverse("registercustomer", args=["f114c3f0-01c0-4739-8620-11a8b579d3b1"])
        self.assertEquals(resolve(url).func.view_class, RegisterCustomerAPIView)    

    def test_registerpersonnel_is_resolved(self):
        url = reverse("registerpersonnel", args=["afcd7507-8543-4a02-9a12-23d2a859795e"])
        self.assertEquals(resolve(url).func.view_class, RegisterPersonnelAPIView) 

    