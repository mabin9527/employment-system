from my_app import models
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from utils.bootstrap import BootStrapModelForm
from utils.encrypt import md5


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
    """
    AdminForm contains username, password and confirmed password. Use screct key 
    to protect users' password and confirmed password. Also password must same as 
    confirmed password if users want to submit their data successfully.
    """

    confirm_password = forms.CharField(
        label = 'Confirm your password',
        widget = forms.PasswordInput(render_value=True)
    )

    class Meta:

        model = models.Admin
        fields = ['username', 'password', 'confirm_password']
        widgets = {
            'password': forms.PasswordInput(render_value=True)
        }

    def clean_password(self):

        pwd = self.cleaned_data.get('password')
        return md5(pwd)

    def clean_confirm_password(self):
        
        pwd = self.cleaned_data.get('password')
        confirm = md5(self.cleaned_data.get('confirm_password'))
        if confirm != pwd:
            raise ValidationError('Your password does not match !')
        return confirm


class LoginForm(forms.Form):

    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    password = forms..CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

