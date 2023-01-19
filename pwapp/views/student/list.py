from django.views.generic import ListView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from pwapp.models import Student

class StudentListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):

    model = Student
    template_name = 'student/list.html'
    context_object_name = 'students'
    paginate_by = 5
    permission_required = 'pwapp.view_student'

    def get_context_data(self, **kwargs):
        context = super(StudentListView, self).get_context_data(**kwargs)
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