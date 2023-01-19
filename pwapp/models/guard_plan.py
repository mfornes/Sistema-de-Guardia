from django.db import models
from .student import Student
from .employee import Employee

class GuardPlan(models.Model):
    LOCAL = [
        ('R', 'Residencia'),
        ('D', 'Docente'),
    ] 
    date = models.DateField()
    local = models.CharField(max_length=10, choices=LOCAL, default='R')
    employees_first_turn = models.ManyToManyField(Employee, related_name='employee_first_turn')
    employees_second_turn = models.ManyToManyField(Employee, related_name='employee_second_turn')
    students_first_turn = models.ManyToManyField(Student, related_name='student_first_turn')
    students_second_turn = models.ManyToManyField(Student, related_name='student_second_turn')
 
    class Meta:
        ordering = ['id']