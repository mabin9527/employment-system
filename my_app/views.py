from django.shortcuts import render, redirect
from my_app import models
from .forms import DepartmentForm


def depart_list(request):
    """
    Department list
    """

    # Get all the deparment list from database
    queryset = models.Department.objects.all()
    return render(request, 'depart_list.html', {'queryset': queryset})

def depart_add(request):
    """
    First to check if the request.method is GET method. If it is true, then link the user to 
    depart_add page. If the request.method is POST method, save the data collected from user
    to database and redirect user to depart_list page 
    """
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            return redirect('/depart/list')

    form = DepartmentForm()       
    context = {
        'form': form
    }
    return render(request, 'depart_add.html', context)

def depart_delete(request):
    pass



    
    
