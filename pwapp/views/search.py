from django.db.models import Q
from django.views.generic import ListView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from pwapp.models import Student

class SearchResultsView(LoginRequiredMixin, PermissionRequiredMixin, ListView):

    model = Student
    template_name = 'student/list.html'
    context_object_name = 'students'
    paginate_by = 5
    permission_required = 'pwapp.view_student'

    def get_context_data(self, **kwargs):
        context = super(SearchResultsView, self).get_context_data(**kwargs)
        students = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(students, self.paginate_by)
        try:
            students = paginator.page(page)
        except PageNotAnInteger:
            students = paginator.page(1)
        except EmptyPage:
            students = paginator.page(paginator.num_pages)
        context['students'] = students
        return context

    def get_queryset(self):
        query = self.request.GET.get("search")
        object_list = Student.objects.filter(
            Q(name__icontains=query) | Q(last_name__icontains=query) | Q(group__icontains=query) 
        )
        return object_list
