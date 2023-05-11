from my_app import models
from django import forms
from django.core.validators import RegexValidator
from utils.pagination import Pagination
from utils.bootstrap import BootStrapModelForm


class DepartmentForm(BootStrapModelForm):
    """
    Create form class to allow user to add department data
    """
    class Meta:
        model = models.Department
        fields = ['title',]


class EmployeeForm(BootStrapModelForm):

    name = forms.CharField(
        label='Name',
        validators=[RegexValidator(r'^[a-zA-Z][a-zA-Z\s]{0,20}[a-zA-Z]$', 
        'Please type correct name')]
    )
    password = forms.CharField(
        label='Password',
        validators=[RegexValidator(
        r'^\S*(?=\S{6,})(?=\S*\d)(?=\S*[A-Z])(?=\S*[a-z])(?=\S*[!@#$%^&*? ])\S*$',
        'The password should contain at least 6 characters, one uppercase letter, one lowercase letter, one number and one special symbol'
        )]
    )
    age = forms.CharField(
        label='Age',
        validators=[RegexValidator(
            r'^(?:[1-9][0-9]?|1[01][0-9]|120)$', 'Please type correct age'
        )]
    )

    class Meta:
        model = models.UserInfo
        fields = [
            'name', 'password', 'age', 'account', 'create_time', 'gender', 'depart',
            ]



class AdminForm(BootStrapModelForm):
    
    class Meta:
        model = models.Admin
        fields = ['username', 'password',]
