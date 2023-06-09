import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

from my_app import models
from my_app.utils.pagination import Pagination
from my_app.utils.form import DepartmentForm, EmployeeForm, AdminForm, LoginForm


# department


def depart_list(request):
    """
    Department list
    """
    data_dict = {}
    search_data = request.GET.get('search', '')
    if search_data:
        data_dict['title__contains'] = search_data

    queryset = models.Department.objects.filter(**data_dict)
    page_object = Pagination(request, queryset)
    context = {
        'search_data': search_data,
        'queryset': page_object.page_queryset,
        'page_string': page_object.html(),
    }
    return render(request, 'depart_list.html', context)


def depart_add(request):
    """
    First to check if the request.method is GET method. If it is true,
    then link the user to depart_add page. If the request.method is POST 
    method, save the data collected from user to database and redirect user 
    to depart_list page
    """
    title_name = 'Create New Department'
    if request.method == 'GET':
        form = DepartmentForm()
        return render(
            request, 'depart_base.html', 
            {'form': form, 'title_name': title_name}
            )

    form = DepartmentForm(data=request.POST)       
    if form.is_valid(): 
        form.save()
    return redirect('/depart/list/')


def depart_delete(request, nid):

    models.Department.objects.filter(id=nid).delete()
    return JsonResponse({'status': True})


def depart_edit(request, nid):
    """
    User can update their department name using edit button. When user click edit button, 
    they will be linked to depart_edit page and the title is original name. Then user can 
    change it to a new title.
    """
    title_name='Update Department Title' 
    row_object=models.Department.objects.filter(id=nid).first()
    if request.method=='GET':
        form = DepartmentForm(instance=row_object)
        return render(request, 'depart_base.html', {'form': form, 'title_name': title_name})

    form = DepartmentForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/depart/list')
    return render(request, 'depart_base.html', {'form': form, 'title': title})

# employee


def employee_list(request):
    """
    Display all the employee's detail from database
    """
    data_dict = {}
    search_data = request.GET.get('search', '')
    if search_data:
        data_dict['depart__title__contains'] = search_data

    queryset = models.UserInfo.objects.filter(**data_dict)
    page_object = Pagination(request, queryset)
    context = {
        'queryset': page_object.page_queryset,
        'page_string': page_object.html(),
        'search_data': search_data,
    }
    return render(request, 'employee_list.html', context)


def employee_add(request):
    """
    Use if statement to check whether request.method is GET. If it is true, user will
    jump to employee_add page. As user submit their data to database, it will be
    validated firstly. Employee's datail will be saved to database if passing validation
    and users are redirected to employee_list page. Otherwise errors will be raised.
    """
    title = 'New Employee'
    if request.method == 'GET':
        form=EmployeeForm()
        return render(request, 'employee_base.html', {'form': form, 'title': title})
    
    form = EmployeeForm(data = request.POST)
    if form.is_valid():
        form.save()
        return redirect('/employee/list')
    return render(request, 'employee_base.html', {'form': form, 'title': title})


def employee_edit(request, nid):
    """
    Allow user to update employee's details. Click edit button and user will 
    be redirected to edit page.
    """
    title = 'Edit Employee'
    row_object = models.UserInfo.objects.filter(id=nid).first()
    if request.method == 'GET':
        form = EmployeeForm(instance = row_object)
        return render(request, 'employee_base.html', {'form': form, 'title': title})
    
    form = EmployeeForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/employee/list/')
    
    return render(request, 'employee_base.html', {'form': form, 'title': title})


def employee_delete(request, nid):
    """
    Delete the employee's information
    """
    models.UserInfo.objects.filter(id=nid).delete()
    return JsonResponse({'status': True})

# admin


def admin_list(request):
    """
    Admin list
    """
    data_dict = {}
    search_data = request.GET.get('search', '')
    if search_data:
        data_dict['username__contains'] = search_data
    
    queryset = models.Admin.objects.filter(**data_dict)
    page_object = Pagination(request, queryset)
    context = {
        'serch_data': search_data,
        'queryset': page_object.page_queryset,
        'page_string': page_object.html(),
        
    }
    return render(request, 'admin_list.html', context)


def admin_add(request):
    """
    Add admin
    """
    title = 'New Admin'
    if request.method == 'GET':
        form = AdminForm()
        return render(request, 'admin_base.html', {'form': form, 'title': title})

    form = AdminForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/admin/list')

    return render(request, 'admin_base.html', {'form': form, 'title': title})
    

def admin_edit(request, nid):
    """
    Update admin
    """
    title = 'Edit Admin'
    row_object = models.Admin.objects.filter(id=nid).first()
    if request.method == 'GET':
        form = AdminForm(instance=row_object)
        return render(request, 'admin_base.html', {'form': form, 'title': title})

    form = AdminForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')
    return render(request, 'admin_base.html', {'form': form, 'title': title})


def admin_delete(request, nid):

    models.Admin.objects.filter(id=nid).delete()
    return JsonResponse({'status': True})


def login(request):
    
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    form = LoginForm(data=request.POST)
    if form.is_valid():
        admin_object = models.Admin.objects.filter(**form.cleaned_data).first()
        if not admin_object:
            form.add_error('password', 'Your username or password is incorrect !')
            return render(request, 'login.html', {'form': form})
        
        request.session['info'] = {'id': admin_object.id, 'name': admin_object.username}
        return redirect('/admin/list')
    return render(request, 'login.html', {'form': form})


def logout(request):
    """
    Clear the session and users can be only accessed to login page.
    """
    request.session.clear()
    return redirect('/login/')
