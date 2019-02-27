from django import forms
# form details
class EmployeeApp(forms.Form):
    name = forms.CharField()
    dob = forms.DateField()
    position = forms.CharField()
    salary = forms.DecimalField()