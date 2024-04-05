import datetime
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.client.models import ClientModel
from apps.employee.models import EmployeeModel
from apps.shop.models import OrderModel


class EmployeeStatisticsViewTests(APITestCase):
    def setUp(self):
        self.employee = EmployeeModel.objects.create(full_name="John Doe")
        self.client = ClientModel.objects.create(full_name="Alice Smith")
        self.order = OrderModel.objects.create(employee=self.employee, client=self.client, price=100)

    def test_employee_statistics_view(self):
        url = reverse('employee-statistics', kwargs={'id': self.employee.id})
        response = self.client.get(url, {'month': 4, 'year': 2024})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['full_name'], self.employee.full_name)
        self.assertEqual(response.data['total_clients'], 1)
        self.assertEqual(response.data['total_products_sold'], 1)
        self.assertEqual(response.data['total_sales'], 100)

class AllEmployeesStatisticsViewTests(APITestCase):
    def setUp(self):
        self.employee1 = EmployeeModel.objects.create(full_name="John Doe")
        self.employee2 = EmployeeModel.objects.create(full_name="Jane Smith")
        self.client = ClientModel.objects.create(full_name="Alice Smith")
        self.order1 = OrderModel.objects.create(employee=self.employee1, client=self.client, price=100)
        self.order2 = OrderModel.objects.create(employee=self.employee2, client=self.client, price=200)

    def test_all_employees_statistics_view(self):
        url = reverse('all-employees-statistics')
        response = self.client.get(url, {'month': 4, 'year': 2024})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['full_name'], self.employee1.full_name)
        self.assertEqual(response.data[1]['full_name'], self.employee2.full_name)

class ClientStatisticsViewTests(APITestCase):
    def setUp(self):
        self.employee = EmployeeModel.objects.create(full_name="John Doe")
        self.client = ClientModel.objects.create(full_name="Alice Smith")
        self.order = OrderModel.objects.create(employee=self.employee, client=self.client, price=100)

    def test_client_statistics_view(self):
        url = reverse('client-statistics', kwargs={'id': self.client.id})
        response = self.client.get(url, {'month': 4, 'year': 2024})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['full_name'], self.client.full_name)
        self.assertEqual(response.data['total_products_bought'], 1)
        self.assertEqual(response.data['total_sales'], 100)