from django.shortcuts import render, redirect
from my_app import models
from django import forms


def depart_list(request):
    """
    Department list
    """

    # Get all the deparment list from database
    queryset = models.Department.objects.all()
    return render(request, 'depart_list.html', {'queryset': queryset})

class DepartmentForm(forms.ModelForm):
    """
    Create form class to allow user to add department data
    """
    class Meta:
        model = models.Department
        fields = ['title',]
        widgets = {
            'title': forms.TextInput(attrs= {'class': 'form-control'}),
        }

def depart_add(request):
    """
    First to check if the request.method is GET method. If it is true, then link the user to 
    depart_add page. If the request.method is POST method, save the data collected from user
    to database and redirect user to depart_list page 
    """
    if request.method == 'GET':
        form = DepartmentForm()
        return render(request, 'depart_add.html', {'form': form})

    form = DepartmentForm(data=request.POST)       
    if form.is_valid():
        form.save()
    return redirect('/depart/list/')

def depart_delete(request):
    pass



    
    
