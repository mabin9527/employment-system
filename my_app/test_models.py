from django.test import TestCase
from my_app.models import Admin, Department, UserInfo


class TestModels(TestCase):
    def test_admin(self):
        admin = Admin.objects.create(
            username='Andy',
            password='1234'
        )
        self.assertEqual(admin.username, 'Andy')
        self.assertEqual(admin.password, '1234')

    def test_depart(self):
        depart = Department.objects.create(
            title='IT'
        )
        self.assertEqual(depart.title, 'IT')

    def test_employee(self):
        employee = UserInfo.objects.create(
            name='Jack',
            password='ABc123@',
            age = 19,
            account=100,
            create_time='2020-09-10',
            gender='Male'
        )
        slef.assertEqual(employee.name, 'Jack')
        slef.assertEqual(employee.password, 'ABc123@')
        slef.assertEqual(employee.age, 19)
        slef.assertEqual(employee.account, 100)
        slef.assertEqual(employee.create_time, '2020-09-10')
        slef.assertEqual(employee.gender, 'Male')



