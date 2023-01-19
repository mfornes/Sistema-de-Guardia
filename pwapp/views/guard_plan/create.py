from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from pwapp.forms import CreateGuardPlanForm

class GuardPlanCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = CreateGuardPlanForm
    template_name = 'guard_plan/create.html'
    success_url = reverse_lazy('guard_plan-list')
    permission_required = 'pwapp.add_guard_plans'
