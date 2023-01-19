from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from pwapp.models import Employee


class EmployeeDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    
    model = Employee
    template_name = 'employee/detail.html'
    context_object_name = 'employee'
    permission_required = 'pwapp.view_employee'
