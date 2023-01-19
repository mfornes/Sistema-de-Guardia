from django.contrib import admin
from .models import CustomUser, Student, Employee, GuardPlan

admin.site.register(CustomUser)
admin.site.register(Student)
admin.site.register(Employee)
admin.site.register(GuardPlan)