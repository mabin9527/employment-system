from django.test import TestCase
from django.urls import reverse
from .models import Admin
from .views import *


# class EmployeeTestCase(TestCase):
#     def setUp(self):
#         employee = UserInfo.objects.create(
#             name = 'Jack Chen',
#             password = 'Abc123@'
#             age = 25,
#             account = 199,
#             create_time = '2020-05-13',
#             gender = 'Male'
#         )

#     def test_employee_creation(self):
#         self.assertEqual(employee.name, 'Jack Chen')
#         self.assertEqual(employee.password, 'Abc123@')
#         self.assertEqual(employee.age, 25)
#         self.assertEqual(employee.balance, 199)
#         self.assertEqual(employee.join_date, '2020-05-13')
#         self.assertEqual(employee.gender, 'Male')

#     def test_employee_list_view(self):
#         url = reverse('employee_list')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, 'Jack Chen')
#         self.assertContains(response, 'Abc123@')
#         self.assertContains(response, 25)
#         self.assertContains(response, 199)
#         self.assertContains(response, '2020-05-13')
#         self.assertContains(response, 'Male')
class AdminTestCase(TestCase):
    def test_admin_list(self):
        admin = Admin.objects.create(
            username = 'Andy',
            password = 'ABc123@'
        )
        self.assertEqual(admin.username, 'Andy')
        self.assertEqual(admin.password, 'ABc123@')

