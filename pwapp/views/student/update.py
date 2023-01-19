from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from pwapp.forms import CreateStudentForm
from pwapp.forms import Student

class StudentUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):

    model = Student
    form_class = CreateStudentForm
    template_name = 'student/update.html'
    context_object_name = 'student'
    permission_required = 'pwapp.change_student'

    def get_success_url(self):
        return reverse_lazy('student-detail', kwargs={'pk': self.object.id})

    def form_invalid(self, form):
        return super(StudentUpdateView, self).form_invalid(form)
    
    def form_valid(self, form):  
        form.save()     
        return super(StudentUpdateView, self).form_valid(form)