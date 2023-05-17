from django.test import TestCase, Client
from django.urls import reverse


class TestAdminViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_list_url = reverse('admin_list')
        self.admin_add_url = reverse('admin_add')

    def test_admin_list_GET(self):
        response = self.client.get(self.admin_list_url)

        self.assertEqual(response.status_code, 200)

    def test_admin_add_GET(self):
        response = self.client.get(self.admin_add_url)

        self.assertEqual(response.status_code, 200)


class TestDepartmentViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.depart_list_url = reverse('depart_list')
        self.depart_add_url = reverse('depart_add')

    def test_depart_list_GET(self):
        response = self.client.get(self.depart_list_url)

        self.assertEqual(response.status_code, 200)

    def test_admin_add_GET(self):
        response = self.client.get(self.depart_add_url)

        self.assertEqual(response.status_code, 200)


class TestEmployeeViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.employee_list_url = reverse('employee_list')
        self.employee_add_url = reverse('employee_add')

    def test_depart_list_GET(self):
        response = self.client.get(self.employee_list_url)

        self.assertEqual(response.status_code, 200)

    def test_admin_add_GET(self):
        response = self.client.get(self.employee_add_url)

        self.assertEqual(response.status_code, 200)