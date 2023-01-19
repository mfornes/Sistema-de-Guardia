from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from pwapp.forms import CreateEmployeeForm
from pwapp.models import Employee


class EmployeeUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Employee
    form_class = CreateEmployeeForm
    template_name = 'employee/update.html'
    context_object_name = 'employee'
    permission_required = 'pwapp.change_employee'

    def get_success_url(self):
        return reverse_lazy('employee-detail', kwargs={'pk': self.object.id})

    def form_invalid(self, form):
        return super(EmployeeUpdateView, self).form_invalid(form)
    
    def form_valid(self, form):  
        form.save()     
        return super(EmployeeUpdateView, self).form_valid(form)