from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from .models import Customer, Order


class CustomerViewSetTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = Customer.objects.create_user(username='testuser', password='testpass', name='Test User', customer_code='CUST001', phone_number='0700123456')
        self.client.force_authenticate(user=self.user)
        self.customer_url = reverse('customer-list')

    def test_get_customers(self):
        response = self.client.get(self.customer_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], self.user.name)

    def test_create_customer(self):
        data = {
            'username': 'newuser',
            'password': 'newpass',
            'name': 'New Customer',
            'customer_code': 'CUST002',
            'phone_number': '0700123456'
        }
        response = self.client.post(self.customer_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 2)
        self.assertEqual(Customer.objects.get(id=response.data['id']).name, 'New Customer')



class OrderViewSetTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = Customer.objects.create_user(username='testuser', password='testpass', name='Test User', customer_code='CUST001', phone_number='0700123456')
        self.client.force_authenticate(user=self.user)
        self.customer = self.user
        self.order = Order.objects.create(customer=self.customer, item='Test Item', amount=100.00)
        self.order_url = reverse('order-list')

    def test_get_orders(self):
        response = self.client.get(self.order_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['item'], self.order.item)

    def test_create_order(self):
        data = {
            'customer': self.customer.id,
            'item': 'New Item',
            'amount': 200.00
        }
        response = self.client.post(self.order_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 2)
        self.assertEqual(Order.objects.get(id=response.data['id']).item, 'New Item')