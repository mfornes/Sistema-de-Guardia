from django.urls import path

from pwapp.views import EmployeeDeleteView, EmployeeCreateView, EmployeeDetailView, EmployeeListView, EmployeeUpdateView

urlpatterns = [
    path('employee', EmployeeListView.as_view(), name='employee-list'),
    path('employee/create', EmployeeCreateView.as_view(), name='employee-create'),
    path('employee/<int:pk>', EmployeeDetailView.as_view(), name='employee-detail'),
    path('employee/<int:pk>/delete', EmployeeDeleteView.as_view(), name='employee-delete'),
    path('employee/<int:pk>/update', EmployeeUpdateView.as_view(), name='employee-update'),
]