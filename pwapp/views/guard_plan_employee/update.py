from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from pwapp.forms import CreateEmployeeForm
from pwapp.models import GuardPlan


class GuardPlanEmployeeUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = GuardPlan
    form_class = CreateEmployeeForm
    template_name = 'guard_plan_employee/update.html'
    context_object_name = 'guard_plan'
    permission_required = 'pwapp.change_guard_plan'

    def get_success_url(self):
        return reverse_lazy('guard_plan_employee-detail', kwargs={'pk': self.object.id})

