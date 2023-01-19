from django.views.generic import ListView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from pwapp.models import GuardPlan

class GuardPlanEmployeeListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):

    model = GuardPlan
    template_name = 'guard_plan_employee/list.html'
    context_object_name = 'guard_plans'
    paginate_by = 5
    permission_required = 'pwapp.view_guard_plan'

    def get_context_data(self, **kwargs):
        context = super(GuardPlanEmployeeListView, self).get_context_data(**kwargs)
        guard_plans = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(guard_plans, self.paginate_by)
        try:
            guard_plans = paginator.page(page)
        except PageNotAnInteger:
            guard_plans = paginator.page(1)
        except EmptyPage:
            guard_plans = paginator.page(paginator.num_pages)
        context['guard_plans'] = guard_plans
        return context

    def get_queryset(self):
        object_list = GuardPlan.objects.filter(~Q(employees_first_turn=None) | ~Q(employees_second_turn=None) )
        return object_list