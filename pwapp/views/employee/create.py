from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from pwapp.forms import CreateEmployeeForm

class EmployeeCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = CreateEmployeeForm
    template_name = 'employee/create.html'
    success_url = reverse_lazy('employee-list')
    permission_required = 'pwapp.add_employee'

    def form_invalid(self, form):
        return super(EmployeeCreateView, self).form_invalid(form)
    
    def form_valid(self, form):  
        form.save()     
        return super(EmployeeCreateView, self).form_valid(form)