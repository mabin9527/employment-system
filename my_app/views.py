from django.shortcuts import render


def depart_list(request):
    """
    Department list
    """
    return render(request, 'depart_list.html')
