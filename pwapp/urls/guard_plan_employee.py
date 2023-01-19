from django.urls import path

from pwapp.views import GuardPlanEmployeeDeleteView, GuardPlanEmployeeCreateView, GuardPlanEmployeeDetailView, GuardPlanEmployeeListView, GuardPlanEmployeeUpdateView

urlpatterns = [
    path('guard_plan_employee', GuardPlanEmployeeListView.as_view(), name='guard_plan_employee-list'),
    path('guard_plan_employee/create', GuardPlanEmployeeCreateView.as_view(), name='guard_plan_employee-create'),
    path('guard_plan_employee/<int:pk>', GuardPlanEmployeeDetailView.as_view(), name='guard_plan_employee-detail'),
    path('guard_plan_employee/<int:pk>/delete', GuardPlanEmployeeDeleteView.as_view(), name='guard_plan_employee-delete'),
    path('guard_plan_employee/<int:pk>/update', GuardPlanEmployeeUpdateView.as_view(), name='guard_plan_employee-update'),
]