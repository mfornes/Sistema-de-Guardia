from django.db.models import Q
from django.views.generic import ListView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from pwapp.models import Employee

class EmployeeSearchResultsView(LoginRequiredMixin, PermissionRequiredMixin, ListView):

    model = Employee
    template_name = 'employee/list.html'
    context_object_name = 'employees'
    paginate_by = 5
    permission_required = 'pwapp.view_employee'

    def get_context_data(self, **kwargs):
        context = super(EmployeeSearchResultsView, self).get_context_data(**kwargs)
        employees = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(employees, self.paginate_by)
        try:
            employees = paginator.page(page)
        except PageNotAnInteger:
            employees = paginator.page(1)
        except EmptyPage:
            employees = paginator.page(paginator.num_pages)
        context['employees'] = employees
        return context

    def get_queryset(self):
        query = self.request.GET.get("search")
        object_list = Employee.objects.filter(
            Q(name__icontains=query) | Q(last_name__icontains=query) | Q(area__icontains=query) 
        )
        return object_list
