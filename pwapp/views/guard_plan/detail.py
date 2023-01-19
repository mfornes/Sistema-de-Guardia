from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from pwapp.models import GuardPlan


class GuardPlanDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    
    model = GuardPlan
    template_name = 'guard_plan/detail.html'
    context_object_name = 'guard_plan'
    permission_required = 'pwapp.view_guard_plan'
