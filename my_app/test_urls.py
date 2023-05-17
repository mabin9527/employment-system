from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import *

class TestUrls(SimpleTestCase):
    def test_depart_list_resolved(self):
        url = reverse('depart_list')
        self.assertEquals(resolve(url).func, depart_list)

    def test_depart_add_resolved(self):
        url = reverse('depart_add')
        self.assertEquals(resolve(url).func, depart_add)

    def test_employee_list_resolved(self):
        url = reverse('employee_list')
        self.assertEquals(resolve(url).func, employee_list)

    def test_employee_add_resolved(self):
        url = reverse('employee_add')
        self.assertEquals(resolve(url).func, employee_add)
    
    def test_admin_list_resolved(self):
        url = reverse('admin_list')
        self.assertEquals(resolve(url).func, admin_list)

    def test_employee_list_resolved(self):
        url = reverse('admin_add')
        self.assertEquals(resolve(url).func, admin_add)


