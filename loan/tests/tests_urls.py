from django.urls import resolve, reverse
from loan.views import *
from django.test import SimpleTestCase


# testing weather the right url handeld by the right view function
class TestUrls(SimpleTestCase):
    def test_signup_is_resolved(self):
        url = reverse("signup")
        self.assertEquals(resolve(url).func.view_class, RegisterUserAPIView)

    def test_registerprovider_is_resolved(self):
        url = reverse("registerprovider")
        self.assertEquals(resolve(url).func.view_class, RegisterProviderAPIView)

    def test_registercustomer_is_resolved(self):
        url = reverse("registercustomer")
        self.assertEquals(resolve(url).func.view_class, RegisterCustomerAPIView)

    def test_registerpersonnel_is_resolved(self):
        url = reverse("registerpersonnel")
        self.assertEquals(resolve(url).func.view_class, RegisterPersonnelAPIView)

        
