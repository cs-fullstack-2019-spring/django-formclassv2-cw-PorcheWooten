from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmployeeApp

# Create your views here.

def index(request):
    return HttpResponse("test")

# sends form submission to console
def gotEmployeeInfo(request):
    print(request.POST)
    return HttpResponse("Check Console")


def employee(request):
    user_form = EmployeeApp()
    context = {
        "newForm": user_form
    }
    return render(request, 'employeeApp/index.html', context)