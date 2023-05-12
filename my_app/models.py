from django.db import models


class Admin(models.Model):
    """
    Table for companies' administrator
    """
    username = models.CharField(verbose_name="Username", max_length=32)
    password = models.CharField(verbose_name='Password', max_length=64)


class Department(models.Model):
    """
    Diagram for department information
    """
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title


class UserInfo(models.Model):
    """
    Employees table
    """
    name = models.CharField(max_length=16)
    password = models.CharField(max_length=64)
    age = models.IntegerField(verbose_name = 'age')
    account = models.DecimalField(verbose_name='balance', max_digits=10, decimal_places=2, default=0)
    create_time = models.DateField(verbose_name='Hire Date')
    depart = models.ForeignKey(Department, on_delete=models.CASCADE)

    gender_choices = (
        (1, 'Male'),
        (2, 'Female'),
    )
    gender = models.SmallIntegerField(choices=gender_choices)


