from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import JsonResponse
from pwapp.forms import CreateStudentForm

class StudentCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = CreateStudentForm
    template_name = 'student/create.html'
    success_url = reverse_lazy('student-list')
    permission_required = 'pwapp.add_student'

    def form_invalid(self, form):
        return super(StudentCreateView, self).form_invalid(form)
    
    def form_valid(self, form):  
        form.save()     
        return super(StudentCreateView, self).form_valid(form)