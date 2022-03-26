from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import CookieStand
class CookieStandTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser', password='pass')
        testuser1.save()

        test_cookie = CookieStand.objects.create(
            location='Orlando', owner=testuser1, description='i dont like salmon cookies',
            minimum_customers_per_hour=5,
            maximum_customers_per_hour=6,
            average_cookies_per_sale=2)
        test_cookie.save()

    def test_cookiestands_model(self):
        cookie = CookieStand.objects.get(id=1)
        actual_location = str(cookie.location)
        actual_owner = str(cookie.owner)
        actual_description = str(cookie.description)
        actual_minimum_customers_per_hour = int(cookie.minimum_customers_per_hour)
        actual_maximum_customers_per_hour = int(cookie.maximum_customers_per_hour)
        actual_average_cookies_per_sale = float(cookie.average_cookies_per_sale)
        self.assertEqual(actual_location, 'Orlando')
        self.assertEqual(actual_owner,'testuser')
        self.assertEqual(actual_description,'i dont like salmon cookies')
        self.assertEqual(actual_minimum_customers_per_hour,5)
        self.assertEqual(actual_maximum_customers_per_hour,6)
        self.assertEqual(actual_average_cookies_per_sale,2)
