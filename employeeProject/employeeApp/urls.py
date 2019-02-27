from django.urls import path
from . import views

urlpatterns = [
    #sets paths
    path('', views.index, name='index'),
    path('employee/', views.employee, name='employee'),
    path('gotEmployeeInfo/', views.employee, name='gotEmployeeInfo'),
    path('', views.employee, name='gotEmployeeInfo')
]