from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from pwapp.models import Student

class StudentDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):

    model = Student
    template_name = 'student/detail.html'
    context_object_name = 'student'
    permission_required = 'pwapp.view_student'
