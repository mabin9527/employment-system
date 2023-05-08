from django.shortcuts import render
from my_app import models


def depart_list(request):
    """
    Department list
    """

    # Get all the deparment list from database
    queryset = models.Department.objects.all()
    return render(request, 'depart_list.html', {'queryset': queryset})

def depart_add(request):
    """
    Allow users to add the department 
    """
    return render(request, 'depart_add.html')
