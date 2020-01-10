from django.test import TestCase

from django.test import TestCase
from rest_framework.test import APIRequestFactory
from django.db.models.query import QuerySet
from rest_framework.test import force_authenticate
from django.contrib.auth.models import User

from order.models import Order, UserDetails
from order.views import OrderModelViewSet

class OrderViewsTestCase(TestCase):
    def setUp(self):
        # Create a test instance
        self.user_details = UserDetails.objects.create(
        full_name =  "erwer",
        phone = "+201222546785",
        address_line1 = "awewqe",
        address_line2 = "qwewqe",
        department = 4,
        building = 3
        )
        self.config = Order.objects.create(
        pizza_number = 4,
        pizza_size = "4",
        describe_order = "eqwewqe",
        user_details = self.user_details)

        # Create auth user for views using api request factory
        self.username = 'thomas'
        self.password = 'adel'
        self.user = User.objects.create_superuser(self.username, 'test@example.com', self.password)

    def test_view_set1(self):
        api_request = APIRequestFactory().get("")
        detail_view = OrderModelViewSet.as_view({'get': 'retrieve'})
        response = detail_view(api_request, pk=self.config.pk)
        self.assertEqual(response.status_code, 200)
