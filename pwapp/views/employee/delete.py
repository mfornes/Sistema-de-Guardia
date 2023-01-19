from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from pwapp.models import Employee


class EmployeeDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
   
   model = Employee
   template_name = 'employee/delete.html'
   success_url = reverse_lazy('employee-list')
   permission_required = 'pwapp.delete_employee'
