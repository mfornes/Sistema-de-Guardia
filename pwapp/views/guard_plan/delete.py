from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from pwapp.models import GuardPlan


class GuardPlanDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
   
   model = GuardPlan
   template_name = 'guard_plan/delete.html'
   success_url = reverse_lazy('guard_plan-list')
   permission_required = 'pwapp.delete_guard_plan'
